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
"""
This module implements attribute-classes and a mixin-class which describe
options to construct a :mod:`argparse`-based command line processor. All
attributes in this module are sub-classes of :class:`Attribute`.
"""

# load dependencies
from argparse   import ArgumentParser
from typing import Callable, Dict, Tuple, List

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
	"""
	Base-class for all attributes to describe a :mod:`argparse`-base command line
	argument parser.
	"""


class CommandGroupAttribute(ArgParseAttribute):
	"""
	*Experimental* attribute to group sub-commands in groups for better readability
	in a ``prog.py --help`` call.
	"""
	__groupName: str = None

	def __init__(self, groupName: str):
		"""
		The constructor expects a 'groupName' which can be used to group sub-commands
		for better readability.
		"""
		super().__init__()
		self.__groupName = groupName

	@property
	def GroupName(self) -> str:
		"""Returns the name of the command group."""
		return self.__groupName


class _HandlerMixin:
	"""
	A mixin-class that offers a class field for a reference to a handler method
	and a matching property.
	"""
	_handler: Callable = None   #: Reference to a method that is called to handle e.g. a sub-command.

	@property
	def Handler(self) -> Callable:
		"""Returns the handler method."""
		return self._handler


class _KwArgsMixin:
	"""
	A mixin-class that offers a class field for named parameters (```**kwargs``)
	and a matching property.
	"""
	_kwargs: Dict = None        #: A dictionary of additional keyword parameters.

	@property
	def KWArgs(self) -> Dict:
		"""
		A dictionary of additional named parameters (``**kwargs``) passed to the
		attribute. These additional parameters are passed without modification to
		:class:`~ArgumentParser`.
		"""
		return self._kwargs


class _ArgsMixin(_KwArgsMixin):
	"""
	A mixin-class that offers a class field for positional parameters (```*args``)
	and a matching property.
	"""

	_args: Tuple = None  #: A tuple of additional positional parameters.

	@property
	def Args(self) -> Tuple:
		"""
		A tuple of additional positional parameters (``*args``) passed to the
		attribute. These additional parameters are passed without modification to
		:class:`~ArgumentParser`.
		"""
		return self._args


class DefaultAttribute(ArgParseAttribute, _HandlerMixin):
	"""
	Marks a handler method is *default* handler. This method is called if no
	sub-command is given. It's an error if more then one method is annotated with
	this attribute.
	"""

	def __call__(self, func: Callable) -> Callable:
		self._handler = func
		return super().__call__(func)


class CommandAttribute(ArgParseAttribute, _HandlerMixin, _KwArgsMixin):
	"""
	Marks a handler method as responsible for the given 'command'. This constructs
	a sub-command parser using :meth:`~ArgumentParser.add_subparsers`.
	"""
	_command: str =  None

	def __init__(self, command: str, **kwargs):
		"""
		The constructor expects a 'command' and an optional list of named parameters
		(keyword arguments) which are passed without modification to :meth:`~ArgumentParser.add_subparsers`.
		"""
		super().__init__()
		self._command =  command
		self._kwargs =   kwargs

	def __call__(self, func: Callable) -> Callable:
		self._handler =  func
		return super().__call__(func)

	@property
	def Command(self) -> str:
		"""Returns the 'command' a sub-command parser adheres to."""
		return self._command


class ArgumentAttribute(ArgParseAttribute, _ArgsMixin):
	"""Base-class for all attributes storing arguments."""

	def __init__(self, *args, **kwargs):
		"""
		The constructor expects positional (``*args``) and/or named parameters
		(``**kwargs``) which are passed without modification to :meth:`~ArgumentParser.add_argument`.
		"""
		super().__init__()
		self._args =   args
		self._kwargs = kwargs


class SwitchArgumentAttribute(ArgumentAttribute):
	"""
	Defines a switch argument like ``--help``.

	Some of the named parameters passed to :meth:`~ArgumentParser.add_argument`
	are predefined (or overwritten) to create a boolean parameter passed to the
	registered handler method. The boolean parameter is ``True`` if the switch
	argument is present in the commandline arguments, otherwise ``False``.
	"""

	def __init__(self, *args, dest:str, **kwargs):
		"""
		The constructor expects positional (``*args``), the destination parameter
		name ``dest`` and/or named parameters	(``**kwargs``) which are passed to
		:meth:`~ArgumentParser.add_argument`.

		To implement a switch argument, the following named parameters are
		predefined:

		* ``action="store_const"``
		* ``const=True``
		* ``default=False``

		This implements a boolean parameter passed to the handler method.
		"""
		kwargs['dest'] =    dest
		kwargs['action'] =  "store_const"
		kwargs['const'] =   True
		kwargs['default'] = False
		super().__init__(*args, **kwargs)


class CommonArgumentAttribute(ArgumentAttribute):
	pass


class CommonSwitchArgumentAttribute(SwitchArgumentAttribute):
	pass


class ArgParseMixin(AttributeHelperMixin):
	"""
	Mixin-class to implement an :mod:`argparse`-base command line argument
	processor.
	"""
	__mainParser: ArgumentParser =  None
	__subParser =   None
	__subParsers =  {}

	def __init__(self, **kwargs):
		"""
		The mixin-constructor expects an optional list of named parameters which
		are passed without modification to the :class:`ArgumentParser` constructor.
		"""
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
	def MainParser(self) -> ArgumentParser:
		"""Returns the main parser."""
		return self.__mainParser

	@property
	def SubParsers(self):
		"""Returns the sub-parsers."""
		return self.__subParsers
