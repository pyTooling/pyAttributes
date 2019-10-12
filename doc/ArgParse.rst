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

   class MyProg():
     def __init__(self):
       self.BuildParser()
       # ...

     def BuiltParser(self):
       # 1. search self for methods (potential handlers)
       # 2. search this methods for attributes
       # 3. extract Command and Argument attributes
       # 4. create the parser with that provided metadata

     # UserManagement commads
     @CommandAttribute('create-user', help="create-user help")
     @ArgumentAttribute(metavar='<Username>', dest="Users", type=str, nargs='+', help='todo help')
     def HandleCreateUser(self, args):
       print("HandleCreateUser: {0}".format(str(args.Users)))

     @CommandAttribute('remove-user',help="remove-user help")
     @ArgumentAttribute(metavar='<UserID>', dest="UserIDs", type=str, nargs='+', help='todo help')
     def HandleRemoveUser(self, args):
       print("HandleRemoveUser: {0}".format(str(args.UserIDs)))

.. note:: Missing Documentation

   Port more documentation from README to Sphinx documentation.
