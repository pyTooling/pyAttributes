import textwrap
from argparse import ArgumentParser, RawDescriptionHelpFormatter


class ProgramBase():
	HeadLine = "Simple ArgParse Test Program"

	def __init__(self):
		pass

	def PrintHeadline(self):
		print("{line}".format(line="=" * 80))
		print("{headline: ^80s}".format(headline=self.HeadLine))
		print("{line}".format(line="=" * 80))


class Program(ProgramBase):
	MainParser: ArgumentParser = None

	def __init__(self):
		super().__init__()

		self._ConstructParser()

	def _ConstructParser(self):
		# create a commandline argument parser
		self.MainParser = ArgumentParser(
			description=textwrap.dedent('''\
				This is the test program.
				'''),
			epilog=textwrap.fill("Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam."),
			formatter_class=RawDescriptionHelpFormatter,
			add_help=False
		)

		self.MainParser.set_defaults(func=self.HandleDefault)

		self.MainParser.add_argument("-q", "--quiet",   dest="quiet",   action="store_const", const=True, default=False, help="Reduce messages to a minimum.")
		self.MainParser.add_argument("-v", "--verbose", dest="verbose", action="store_const", const=True, default=False, help="Print out detailed messages.")
		self.MainParser.add_argument("-d", "--debug",   dest="debug",   action="store_const", const=True, default=False, help="Enable debug mode.")


		subParsers = self.MainParser.add_subparsers(help='sub-command help')

		# UserManagement commands
		# create the sub-parser for the "create-user" command
		CreateUserParser = subParsers.add_parser('create-user', help='create-user help')
		CreateUserParser.add_argument(metavar='<Username>', dest="Users", type=str, nargs='+', help='todo help')
		CreateUserParser.set_defaults(func=self.HandleCreateUser)

		# create the sub-parser for the "remove-user" command
		RemoveUserParser = subParsers.add_parser('remove-user', help='remove-user help')
		RemoveUserParser.add_argument(metavar='<UserID>', dest="UserIDs", type=str, nargs='+', help='todo help')
		RemoveUserParser.set_defaults(func=self.HandleRemoveUser)

	def Run(self):
		self.MainParser.parse_args()

	def HandleDefault(self, args):
		self.PrintHeadline()

		print("HandleDefault:\n  quiet={0!s}\n  verbose={1!s}\n  debug={2!s}".format(args.quiet, args.verbose, args.debug))

	def HandleCreateUser(self, args):
		print("HandleCreateUser: {0}".format(str(args.Users)))

	def HandleRemoveUser(self, args):
		print("HandleRemoveUser: {0}".format(str(args.UserIDs)))


if __name__ == "__main__":
	prog = Program()
	prog.Run()
