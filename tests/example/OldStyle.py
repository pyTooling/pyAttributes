import textwrap
from argparse import ArgumentParser, RawDescriptionHelpFormatter
from typing import List, Dict


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
	SubParsers: Dict[str, ArgumentParser] = None

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

		self.MainParser.add_argument("-q", "--quiet",   dest="quiet",   action="store_const", const=True, default=False, help="Reduce messages to a minimum.")
		self.MainParser.add_argument("-v", "--verbose", dest="verbose", action="store_const", const=True, default=False, help="Print out detailed messages.")
		self.MainParser.add_argument("-d", "--debug",   dest="debug",   action="store_const", const=True, default=False, help="Enable debug mode.")

		# create subparsers
		subParsers = self.MainParser.add_subparsers(help='sub-command help')
		self.SubParsers = {}

		# Default handler
		self.MainParser.set_defaults(func=self.HandleDefault)

		# Help handler
		HelpParser = subParsers.add_parser("help", help = "Display help page(s) for the given command name.")
		HelpParser.add_argument(metavar = "Command", dest = "Command", type = str, nargs = "?", help = "Print help page(s) for a command.")
		HelpParser.set_defaults(func=self.HandleHelp)
		self.SubParsers["help"] = HelpParser

		# UserManagement commands
		CreateUserParser = subParsers.add_parser("new-user", help="Create a new user.")
		CreateUserParser.add_argument(metavar='<UserID>', dest="UserID", type=str, help="UserID - unique identifier")
		CreateUserParser.add_argument(metavar='<Name>', dest="Name", type=str, help="The user's display name.")
		CreateUserParser.set_defaults(func=self.HandleNewUser)
		self.SubParsers["new-user"] = CreateUserParser

		RemoveUserParser = subParsers.add_parser("delete-user", help="Delete a user.")
		RemoveUserParser.add_argument(metavar='<UserID>', dest="UserID", type=str, help="UserID - unique identifier")
		RemoveUserParser.set_defaults(func=self.HandleDeleteUser)
		self.SubParsers["delete-user"] = RemoveUserParser

		RemoveUserParser = subParsers.add_parser("list-user", help="List users.")
		RemoveUserParser.add_argument('--all', dest="all", help='List all users.')
		RemoveUserParser.set_defaults(func=self.HandleListUser)
		self.SubParsers["list-user"] = RemoveUserParser

	def Run(self):
		args = self.MainParser.parse_args()
		args.func(args)

	def HandleDefault(self, args):
		self.PrintHeadline()
		# TODO: use dedent() and multi-line string
		print(f"HandleDefault:\n  quiet={args.quiet!s}\n  verbose={args.verbose!s}\n  debug={args.debug!s}")

	def HandleHelp(self, args):
		self.PrintHeadline()

		# TODO: use dedent() and multi-line string
		print(f"HandleHelp:\n  quiet={args.quiet!s}\n  verbose={args.verbose!s}\n  debug={args.debug!s}\n\n  command={args.Command!s}\n\n")

		if (args.Command is None):
			self.MainParser.print_help()
		elif (args.Command == "help"):
			print("This is a recursion ...")
		else:
			try:
				self.SubParsers[args.Command].print_help()
			except KeyError:
				print(f"Command {args.Command} is unknown.")

	def HandleNewUser(self, args):
		self.PrintHeadline()

		# TODO: use dedent() and multi-line string
		print(f"HandleHelp:\n  quiet={args.quiet!s}\n  verbose={args.verbose!s}\n  debug={args.debug!s}\n\n  UserID={args.UserID!s}  Name={args.Name!s}")

	def HandleDeleteUser(self, args):
		self.PrintHeadline()

		# TODO: use dedent() and multi-line string
		print(f"HandleHelp:\n  quiet={args.quiet!s}\n  verbose={args.verbose!s}\n  debug={args.debug!s}\n\n  UserID={args.UserID!s}")

	def HandleListUser(self, args):
		self.PrintHeadline()

		# TODO: use dedent() and multi-line string
		print(f"HandleHelp:\n  quiet={args.quiet!s}\n  verbose={args.verbose!s}\n  debug={args.debug!s}\n\n  all={args.all!s}")


if __name__ == "__main__":
	prog = Program()
	prog.Run()
