# EMACS settings: -*-  tab-width: 2; indent-tabs-mode: t -*-
# vim: tabstop=2:shiftwidth=2:noexpandtab
# kate: tab-width 2; replace-tabs off; indent-width 2;
# =============================================================================
#                  _   _   _        _ _           _
#   _ __  _   _   / \ | |_| |_ _ __(_) |__  _   _| |_ ___  ___
#  | '_ \| | | | / _ \| __| __| '__| | '_ \| | | | __/ _ \/ __|
#  | |_) | |_| |/ ___ \ |_| |_| |  | | |_) | |_| | ||  __/\__ \
#  | .__/ \__, /_/   \_\__|\__|_|  |_|_.__/ \__,_|\__\___||___/
#  |_|    |___/
# =============================================================================
# Authors:            Patrick Lehmann
#
# Python module:      pyAttribute for Python's argparse Package.
#
# Description:
# ------------------------------------
#		TODO
#
# License:
# ============================================================================
# Copyright 2017-2020 Patrick Lehmann - Bötzingen, Germany
# Copyright 2007-2016 Patrick Lehmann - Dresden, Germany
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
#
# SPDX-License-Identifier: Apache-2.0
# ============================================================================
#
# load dependencies
from argparse   import ArgumentParser
from typing     import Callable, Dict, Tuple

from .          import Attribute, AttributeHelperMixin


__api__ = [
	'CommandGroupAttribute',
	'DefaultAttribute',
	'CommandAttribute',
	'ArgumentAttribute',
	'SwitchArgumentAttribute',
	'CommonArgumentAttribute',
	'CommonSwitchArgumentAttribute',
	'ArgParseMixin'
]
__all__ = __api__


class ArgParseAttribute(Attribute):
	pass

class CommandGroupAttribute(ArgParseAttribute):
	__groupName: str = None

	def __init__(self, groupName: str):
		super().__init__()
		self.__groupName = groupName

	@property
	def GroupName(self) -> str:
		return self.__groupName


class _HandlerMixin:
	_handler: Callable = None

	@property
	def Handler(self) -> Callable:
		return self._handler


class _KwArgsMixin:
	_kwargs: Dict = None

	@property
	def KWArgs(self) -> Dict:
		return self._kwargs


class _ArgsMixin(_KwArgsMixin):
	_args: Tuple = None

	@property
	def Args(self) -> Tuple:
		return self._args


class DefaultAttribute(ArgParseAttribute, _HandlerMixin):
	def __call__(self, func: Callable) -> Callable:
		self._handler = func
		return super().__call__(func)


class CommandAttribute(ArgParseAttribute, _HandlerMixin, _KwArgsMixin):
	_command: str =  None

	def __init__(self, command: str, **kwargs):
		super().__init__()
		self._command =  command
		self._kwargs =   kwargs

	def __call__(self, func: Callable) -> Callable:
		self._handler =  func
		return super().__call__(func)

	@property
	def Command(self) -> str:
		return self._command


class ArgumentAttribute(ArgParseAttribute, _ArgsMixin):
	def __init__(self, *args, **kwargs):
		super().__init__()
		self._args =   args
		self._kwargs = kwargs


class SwitchArgumentAttribute(ArgumentAttribute):
	def __init__(self, *args, **kwargs):
		kwargs['action'] =  "store_const"
		kwargs['const'] =   True
		kwargs['default'] = False
		super().__init__(*args, **kwargs)


class CommonArgumentAttribute(ArgumentAttribute):
	pass


class CommonSwitchArgumentAttribute(SwitchArgumentAttribute):
	pass


class ArgParseMixin(AttributeHelperMixin):
	__mainParser: ArgumentParser =  None
	__subParser =   None
	__subParsers =  {}

	def __init__(self, **kwargs):
		super().__init__()

		# create a commandline argument parser
		self.__mainParser = ArgumentParser(**kwargs)
		self.__subParser = self.__mainParser.add_subparsers(help='sub-command help')

		for _, func in CommonArgumentAttribute.GetMethods(self):
			for comAttribute in CommonArgumentAttribute.GetAttributes(func):
				self.__mainParser.add_argument(*(comAttribute.Args), **(comAttribute.KWArgs))

		for _, func in CommonSwitchArgumentAttribute.GetMethods(self):
			for comAttribute in CommonSwitchArgumentAttribute.GetAttributes(func):
				self.__mainParser.add_argument(*(comAttribute.Args), **(comAttribute.KWArgs))

		for _, func in self.GetMethods():
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

	def Run(self):
		try:
			from argcomplete  import autocomplete
			autocomplete(self.__mainParser)
		except ImportError:
			pass

		# parse command line options and process split arguments in callback functions
		args = self.__mainParser.parse_args()
		# because func is a function (unbound to an object), it MUST be called with self as a first parameter
		args.func(self, args)

	@property
	def MainParser(self):
		return self.__mainParser

	@property
	def SubParsers(self):
		return self.__subParsers
