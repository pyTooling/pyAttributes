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
# Python unittest:    Testing the ArgParse module
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
"""
pyAttributes
############

:copyright: Copyright 2007-2020 Patrick Lehmann - Bötzingen, Germany
:license: Apache License, Version 2.0
"""
from unittest     import TestCase

from pyAttributes.ArgParseAttributes import ArgParseMixin, DefaultAttribute, CommandAttribute, ArgumentAttribute, SwitchArgumentAttribute, CommonSwitchArgumentAttribute

from pyAttributes import Attribute, AttributeHelperMixin

from .            import zip


if __name__ == "__main__":
	print("ERROR: you called a testcase declaration file as an executable module.")
	print("Use: 'python -m unitest <testcase module>'")
	exit(1)


class ProgramBase():
	def __init__(self):
		pass


class Program(ProgramBase, ArgParseMixin):
	def __init__(self):
		import argparse
		import textwrap

		# call constructor of the main interitance tree
		super().__init__()

		# Call the constructor of the ArgParseMixin
		ArgParseMixin.__init__(
			self,
		  # prog =	self.program,
		  # usage =	"Usage?",			# override usage string
		  description=textwrap.dedent('''\
				This is the test program.
				'''),
		  epilog=textwrap.fill("Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet."),
		  formatter_class=argparse.RawDescriptionHelpFormatter,
		  add_help=False
		)


	@CommonSwitchArgumentAttribute("-q", "--quiet",   dest="quiet",   help="Reduce messages to a minimum.")
	@CommonSwitchArgumentAttribute("-v", "--verbose", dest="verbose", help="Print out detailed messages.")
	@CommonSwitchArgumentAttribute("-d", "--debug",   dest="debug",   help="Enable debug mode.")
	def Run(self):
		ArgParseMixin.Run(self)


	@DefaultAttribute()
	def HandleDefault(self, args):
		print("DefaultHandler: verbose={0}  debug={1}".format(str(args.verbose), str(args.debug)))


	@CommandAttribute('help', help="Print help page(s).")
	def HandleHelp(self, _):
		print("HandleHelp:")


	@CommandAttribute("new-user", help="Create a new user.")
	@ArgumentAttribute(metavar='<UserID>', dest="UserID", type=str, help="UserID - unique identifier")
	@ArgumentAttribute(metavar='<Name>', dest="Name", type=str, help="The user's display name.")
	def HandleNewUser(self, args):
		print("HandleNewUser: UserID={0}  Name={1}".format(args.UserID, args.Name))


	@CommandAttribute("delete-user", help="Delete a user.")
	@ArgumentAttribute(metavar='<UserID>', dest="UserID", type=str, help="UserID - unique identifier")
	def HandleDeleteUser(self, args):
		print("HandleDeleteUser: all={0}".format(str(args.all)))


	@CommandAttribute("list-user", help="List users.")
	@SwitchArgumentAttribute('--all', dest="all", help='List all users.')
	def HandleListUser(self, args):
		print("HandleListUser: all={0}".format(str(args.all)))


class Test(TestCase):
	prog: Program

	def setUp(self) -> None:
		self.prog = Program()

	def testDefaultAttribute(self):
		pass
