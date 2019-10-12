![PyPI - License](https://img.shields.io/pypi/l/pyAttributes)
![GitHub tag (latest by date)](https://img.shields.io/github/v/tag/Paebbels/pyAttributes) 
![GitHub release (latest by date)](https://img.shields.io/github/v/release/Paebbels/pyAttributes)
[![Documentation Status](https://readthedocs.org/projects/pyattributes/badge/?version=latest)](https://pyattributes.readthedocs.io/en/latest/?badge=latest)  
[![PyPI](https://img.shields.io/pypi/v/pyAttributes)](https://pypi.org/project/pyAttributes/)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pyAttributes)
![PyPI - Wheel](https://img.shields.io/pypi/wheel/pyAttributes)
![PyPI - Status](https://img.shields.io/pypi/status/pyAttributes)

# pyAttributes

**.NET-like Attributes implemented as Python decorators**

I have played a bit with class-based decorators and <del>as far as</del> I can tell it's possible to implement .NET-like attributes in Python.

## So first let's develop a meaningful use case:
Most of us know the Python `argparse` command line argument parser. This parser can handle sub-commands like `git commit -m "message"` where *commit* is a sub-command and `-m <message>` is a parameter of this sub-command parser. It's possible to assign a callback function to each sub-command parser.

> **Python 3.4.2 for Windows** has a bug in handling callback functions. It's fixed in 3.5.0 (I haven't tested other 3.4.x versions).

Here is a classic `argparse` example:

```python
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
```

A better and more descriptive solution could look like this:

```python
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
```

-------

So let's develop a solution step-by-step.

## Step 1 - A common `Attribute` class

So let's develop a common `Attribute` class, which is also a class-based decorator. This decorator adds himself to a list called `__attributes__`, which is registered on the function which is to be decorated.

```python
class Attribute():
	AttributesMemberName =  "__attributes__"
	_debug =                False
	
	def __call__(self, func):
		# inherit attributes and append myself or create a new attributes list
		if (func.__dict__.__contains__(Attribute.AttributesMemberName)):
			func.__dict__[Attribute.AttributesMemberName].append(self)
		else:
			func.__setattr__(Attribute.AttributesMemberName, [self])
		return func
	
	def __str__(self):
		return self.__name__

	@classmethod
	def GetAttributes(self, method):
		if method.__dict__.__contains__(Attribute.AttributesMemberName):
			attributes = method.__dict__[Attribute.AttributesMemberName]
			if isinstance(attributes, list):
				return [attribute for attribute in attributes if isinstance(attribute, self)]
		return list()
```

## Step 2 - User defined attributes

Now we can create custom attributes which inherit the basic decorative functionality from `Attribute`. I'll declare 3 attributes:

 - **DefaultAttribute** - If no sub-command parser recognizes a command, this decorated method will be the fallback handler.
 - **CommandAttribute** - Define a sub-command and register the decorated function as a callback.
 - **ArgumentAttribute** - Add parameters to the sub-command parser.

```python
class DefaultAttribute(Attribute):
	__handler = None
	
	def __call__(self, func):
		self.__handler = func
		return super().__call__(func)
	
	@property
	def Handler(self):
		return self.__handler
```

```python
class CommandAttribute(Attribute):
	__command = ""
	__handler = None
	__kwargs =  None

	def __init__(self, command, **kwargs):
		super().__init__()
		self.__command =  command
		self.__kwargs =   kwargs
	
	def __call__(self, func):
		self.__handler = func
		return super().__call__(func)
	
	@property
	def Command(self):
		return self.__command
	
	@property
	def Handler(self):
		return self.__handler
	
	@property
	def KWArgs(self):
		return self.__kwargs
```

```python
class ArgumentAttribute(Attribute):
	__args =   None
	__kwargs = None

	def __init__(self, *args, **kwargs):
		super().__init__()
		self.__args =   args
		self.__kwargs = kwargs
	
	@property
	def Args(self):
		return self.__args
	
	@property
	def KWArgs(self):
		return self.__kwargs
```

## Step 3 - Building a helper mixin class to handle attributes on methods

To ease the work with attributes I implemented a `AttributeHelperMixin` class, that can:

 - retrieve all methods of a class
 - check if a method has attributes and
 - return a list of attributes on a given method.

```python
class AttributeHelperMixin():
	def GetMethods(self):
		return {funcname: func
						for funcname, func in self.__class__.__dict__.items()
						if hasattr(func, '__dict__')
					 }.items()

	def HasAttribute(self, method):
		if method.__dict__.__contains__(Attribute.AttributesMemberName):
			attributeList = method.__dict__[Attribute.AttributesMemberName]
			return (isinstance(attributeList, list) and (len(attributeList) != 0))
		else:
			return False
				
	def GetAttributes(self, method):
		if method.__dict__.__contains__(Attribute.AttributesMemberName):
			attributeList = method.__dict__[Attribute.AttributesMemberName]
			if isinstance(attributeList, list):
				return attributeList
		return list()
```

## Step 4 - Build an application class

Now it's time to build an application class that inherits from `MyBase` and from `ArgParseMixin`. I'll discuss `ArgParseMixin` later. The class has a normal constructor, which calls both base-class constructors. It also adds 2 arguments for *verbose* and *debug* to the main-parser. All callback handlers are decorated with the new Attributes.

```python
class MyBase():
	def __init__(self):
		pass

class prog(MyBase, ArgParseMixin):
	def __init__(self):
		import argparse
		import textwrap
		
		# call constructor of the main interitance tree
		MyBase.__init__(self)
		
		# Call the constructor of the ArgParseMixin
		ArgParseMixin.__init__(self,
			description = textwrap.dedent('''\
				This is the Admin Service Tool.
				'''),
			formatter_class = argparse.RawDescriptionHelpFormatter,
			add_help=False)

		self.MainParser.add_argument('-v', '--verbose',  dest="verbose",  help='print out detailed messages',  action='store_const', const=True, default=False)
		self.MainParser.add_argument('-d', '--debug',    dest="debug",    help='enable debug mode',            action='store_const', const=True, default=False)
	
	def Run(self):
		ArgParseMixin.Run(self)
	
	@DefaultAttribute()
	def HandleDefault(self, args):
		print("DefaultHandler: verbose={0}  debug={1}".format(str(args.verbose), str(args.debug)))
	
	@CommandAttribute("create-user", help="my new command")
	@ArgumentAttribute(metavar='<Username>', dest="Users", type=str, help='todo help')
	def HandleCreateUser(self, args):
		print("HandleCreateUser: {0}".format(str(args.Users)))
	
	@CommandAttribute("remove-user", help="my new command")
	@ArgumentAttribute(metavar='<UserID>', dest="UserIDs", type=str, help='todo help')
	def HandleRemoveUser(self, args):
		print("HandleRemoveUser: {0}".format(str(args.UserIDs)))
	
p = prog()
p.Run()
```

## Step 5 - The `ArgParseMixin` helper class.

This class constructs the `argparse` based parser with the provided data from attributes. The parsing process is invoked by `Run()`.

```python
class ArgParseMixin(AttributeHelperMixin):
	__mainParser = None
	__subParser =  None
	__subParsers = {}

	def __init__(self, **kwargs):
		super().__init__()
		
		# create a commandline argument parser
		import argparse
		self.__mainParser = argparse.ArgumentParser(**kwargs)
		self.__subParser =  self.__mainParser.add_subparsers(help='sub-command help')
		
		for funcname,func in self.GetMethods():
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
```

## Contributors:

* [Patrick Lehmann](https://github.com/Paebbels) (Maintainer)


## License

This library is licensed under [Apache License 2.0](LICENSE.md)

-------------------------

SPDX-License-Identifier: Apache-2.0
