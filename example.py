# =============================================================================
#                  _   _   _        _ _           _
#   _ __  _   _   / \ | |_| |_ _ __(_) |__  _   _| |_ ___  ___
#  | '_ \| | | | / _ \| __| __| '__| | '_ \| | | | __/ _ \/ __|
#  | |_) | |_| |/ ___ \ |_| |_| |  | | |_) | |_| | ||  __/\__ \
#  | .__/ \__, /_/   \_\__|\__|_|  |_|_.__/ \__,_|\__\___||___/
#  |_|    |___/
# =============================================================================
# Authors:						Patrick Lehmann
#
# Python Executable:	pyAttributes - Testcase 1
#
# License:
# ============================================================================
# Copyright 2007-2015 Patrick Lehmann - Dresden, Germany
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ============================================================================
#
from pyAttribute import AttributeHelperMixin
from pyAttribute.ArgParseAttributes import DefaultAttribute, CommandAttribute, ArgumentAttribute, SwitchArgumentAttribute


class MyBase():
	def __init__(self) -> None:
		pass


class ArgParseMixin(AttributeHelperMixin):
	__mainParser = 	None
	__subParser =		None
	__subParsers =	{}

	def __init__(self, **kwargs) -> None:
		super().__init__()

		# create a commandline argument parser
		import argparse
		self.__mainParser = argparse.ArgumentParser(**kwargs)
		self.__subParser = self.__mainParser.add_subparsers(help='sub-command help')

		for _,func in self.GetMethods():
			defAttributes = DefaultAttribute.GetAttributes(func)
			if (len(defAttributes) != 0):
				defAttribute = defAttributes[0]
				self.__mainParser.set_defaults(func=defAttribute.Handler)
				continue

			cmdAttributes = CommandAttribute.GetAttributes(func)
			if (len(cmdAttributes) != 0):
				cmdAttribute = cmdAttributes[0]
				subParser = self.__subParser.add_parser(cmdAttribute.Command, **(cmdAttribute.KWArgs))
				subParser.set_defaults(func=cmdAttribute.Handler)

				for argAttribute in ArgumentAttribute.GetAttributes(func):
					subParser.add_argument(*(argAttribute.Args), **(argAttribute.KWArgs))

				self.__subParsers[cmdAttribute.Command] = subParser
				continue

	def Run(self) -> None:
		# parse command line options and process splitted arguments in callback functions
		args = self.__mainParser.parse_args()
		# because func is a function (unbound to an object), it MUST be called with self as a first parameter
		args.func(self, args)

	@property
	def MainParser(self):
		return self.__mainParser

	@property
	def SubParsers(self):
		return self.__subParsers


class prog(MyBase, ArgParseMixin):
	def __init__(self) -> None:
		import argparse
		import textwrap

		# call constructor of the main interitance tree
		MyBase.__init__(self)

		# Call the constructor of the ArgParseMixin
		ArgParseMixin.__init__(self,
			# prog =	self.program,
			# usage =	"Usage?",			# override usage string
			description = textwrap.dedent('''\
				This is the Admin Service Tool.
				'''),
			epilog =	"Epidingsbums",
			formatter_class = argparse.RawDescriptionHelpFormatter,
			add_help=False)

		self.MainParser.add_argument('-v', '--verbose',	dest="verbose",	help='print out detailed messages',	action='store_const', const=True, default=False)
		self.MainParser.add_argument('-d', '--debug',		dest="debug",		help='enable debug mode',						action='store_const', const=True, default=False)

	def Run(self) -> None:
		ArgParseMixin.Run(self)

	@DefaultAttribute()
	def HandleDefault(self, args) -> None:
		print(f"DefaultHandler: verbose={args.verbose!s}  debug={args.debug!s}")

	@CommandAttribute('help', help="help help")
	def HandleHelp(self, _) -> None:
		print("HandleHelp:")

	@CommandAttribute("prog", help="my new command")
	@ArgumentAttribute(metavar='<DeviceID>', dest="DeviceID", type=str, help='todo help')
	@ArgumentAttribute(metavar='<BitFile>', dest="Filename", type=str, help='todo help')
	def HandleProg(self, args) -> None:
		print(f"HandleProg: DeviceID={args.DeviceID}  BitFile={args.Filename}")

	@CommandAttribute("list", help="my new command")
	@SwitchArgumentAttribute('--all', dest="all", help='show all devices, otherwise only available')
	def HandleList(self, args) -> None:
		print(f"HandleList: all={args.all}")


p = prog()
p.Run()
