from argparse import ArgumentDefaultsHelpFormatter

from pyAttributes.ArgParseAttributes import ArgParseMixin, CommonSwitchArgumentAttribute, DefaultAttribute, CommandAttribute, CommonArgumentAttribute, ArgumentAttribute, SwitchArgumentAttribute


class ProgramBase():
	HeadLine = "Simple ArgParse Test Program"

	def __init__(self):
		pass

	def PrintHeadline(self):
		print("{line}".format(line="="*80))
		print("{headline: ^80s}".format(headline=self.HeadLine))
		print("{line}".format(line="="*80))


class Program(ProgramBase, ArgParseMixin):
	def __init__(self):
		import textwrap

		# call constructor of the main inheritance tree
		super().__init__()

		# Call the constructor of the ArgParseMixin
		ArgParseMixin.__init__(
			self,
			description=textwrap.dedent('''\
        This is the test program.
        '''),
			epilog=textwrap.fill("Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam."),
			formatter_class=ArgumentDefaultsHelpFormatter,
			add_help=False
		)

	@CommonSwitchArgumentAttribute("-q", "--quiet",   dest="quiet",   help="Reduce messages to a minimum.")
	@CommonSwitchArgumentAttribute("-v", "--verbose", dest="verbose", help="Print out detailed messages.")
	@CommonSwitchArgumentAttribute("-d", "--debug",   dest="debug",   help="Enable debug mode.")
	def Run(self):
		ArgParseMixin.Run(self)


	@DefaultAttribute()
	def HandleDefault(self, args):
		self.PrintHeadline()

		print(f"HandleDefault:\n  quiet={args.quiet!s}\n  verbose={args.verbose!s}\n  debug={args.debug!s}")


	@CommandAttribute("help", help="Display help page(s) for the given command name.")
	@ArgumentAttribute(metavar="Command", dest="Command", type=str, nargs="?", help="Print help page(s) for a command.")
	def HandleHelp(self, args):
		self.PrintHeadline()

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


	@CommandAttribute("new-user", help="Create a new user.")
	@ArgumentAttribute(metavar='<UserID>', dest="UserID", type=str, help="UserID - unique identifier")
	@ArgumentAttribute(metavar='<Name>', dest="Name", type=str, help="The user's display name.")
	def HandleNewUser(self, args):
		self.PrintHeadline()

		print(f"HandleNewUser:\n  quiet={args.quiet!s}\n  verbose={args.verbose!s}\n  debug={args.debug!s}\n\n  UserID={args.UserID!s}  Name={args.Name!s}  Limit={args.Limit!s}")


	@CommandAttribute("delete-user", help="Delete a user.")
	@ArgumentAttribute(metavar='<UserID>', dest="UserID", type=str, help="UserID - unique identifier")
	def HandleDeleteUser(self, args):
		self.PrintHeadline()

		print(f"HandleDeleteUser:\n  quiet={args.quiet!s}\n  verbose={args.verbose!s}\n  debug={args.debug!s}\n\n  UserID={args.UserID!s}")


	@CommandAttribute("list-user", help="List users.")
	@SwitchArgumentAttribute('--all', dest="all", help='List all users.')
	def HandleListUser(self, args):
		self.PrintHeadline()

		print(f"HandleListUser:\n  quiet={args.quiet!s}\n  verbose={args.verbose!s}\n  debug={args.debug!s}\n\n  all={args.all!s}")


if __name__ == "__main__":
	prog = Program()
	prog.Run()
