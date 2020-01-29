ArgParse
########

Many people use Python's ``argparse`` command line argument parser. This parser
can handle sub-commands like ``git commit -m "message"`` where *commit* is a
sub-command and ``-m <message>`` is a parameter of this sub-command parser. It's
possible to assign a callback function to each sub-command parser.

.. warning:: Python 3.4.x on Windows

   **Python 3.4.2 for Windows** has a bug in handling callback functions. It's
   fixed in Python 3.5.x. I haven't tested other 3.4.x versions.

Classic ``argparse`` Example
****************************

.. code-block:: python

   class MyProg():
     def Run(self):
       # create a commandline argument parser
       MainParser = argparse.ArgumentParser(
         description = textwrap.dedent('''This is the User Service Tool.'''),
         formatter_class = argparse.RawDescriptionHelpFormatter,
         add_help=False)

       MainParser.add_argument('-v', '--verbose', dest="verbose", help='print out detailed messages', action='store_const', const=True, default=False)
       MainParser.add_argument('-d', '--debug', dest="debug", help='enable debug mode', action='store_const', const=True, default=False)
       MainParser.set_defaults(func=self.HandleDefault)
       subParsers = MainParser.add_subparsers(help='sub-command help')

       # UserManagement commads
       # create the sub-parser for the "create-user" command
       CreateUserParser = subParsers.add_parser('create-user', help='create-user help')
       CreateUserParser.add_argument(metavar='<Username>', dest="Users", type=str, nargs='+', help='todo help')
       CreateUserParser.set_defaults(func=self.HandleCreateUser)

       # create the sub-parser for the "remove-user" command
       RemoveUserParser = subParsers.add_parser('remove-user', help='remove-user help')
       RemoveUserParser.add_argument(metavar='<UserID>', dest="UserIDs", type=str, nargs='+', help='todo help')
       RemoveUserParser.set_defaults(func=self.HandleRemoveUser)

     def HandleDefault(self, args):
       print("HandleDefault:")

     def HandleCreateUser(self, args):
       print("HandleCreateUser: {0}".format(str(args.Users)))

     def HandleRemoveUser(self, args):
       print("HandleRemoveUser: {0}".format(str(args.UserIDs)))

   my = MyProg()
   my.Run()


New ``pyAttributes`` Approach
*****************************

A better and more descriptive solution could look like this:

.. code-block:: python

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

.. note:: Missing Documentation

   Port more documentation from README to Sphinx documentation.
