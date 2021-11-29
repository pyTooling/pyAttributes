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
# Python package:     pyAttributes Implementation
#
# License:
# ============================================================================
# Copyright 2017-2021 Patrick Lehmann - Bötzingen, Germany
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

This Python module offers the base implementation of .NET-like attributes
realized with Python decorators. This module comes also with a mixin-class
to ease using classes having annotated methods.

The decorators in pyAttributes are implemented as class-based decorators.

The annotated data is stored in an additional ``__dict__`` entry for each
annotated method. By default the entry is called ``__pyattr__``.
"""

__author__ =    "Patrick Lehmann"
__email__ =     "Paebbels@gmail.com"
__copyright__ = "2007-2021, Patrick Lehmann"
__license__ =   "Apache License, Version 2.0"
__version__ =   "2.3.3"

# load dependencies
from typing       import Callable, List, TypeVar, Dict, Any, Iterable, Union
from collections  import OrderedDict

from pyTooling.Decorators import export

# TODO: implement class, method, function attributes
# TODO: implement unique attributes
# TODO: add an attacheHelper methods option
# TODO: implement a static HasAttribute method


Func =  TypeVar("Func")
"""A type variable for functions. Here it's used for methods."""

TAttr = TypeVar("TAttr", bound='Attribute')
"""A type variable for :class:`~pyAttributes.Attribute`."""

TAttributeFilter = Union[TAttr, Iterable[TAttr], None]
"""A type hint for a filter parameter that accepts either a single :class:`~pyAttributes.Attribute` or an iterable of those."""


@export
class Attribute:
	"""Base-class for all pyAttributes."""

	__AttributesMemberName__ = "__pyattr__"   #: Field name on objects to store pyAttributes

	def __call__(self, func: Func) -> Func:
		"""Make all classes derived from ``Attribute`` callable, so they can be used as a decorator."""
		self._AppendAttribute(func, self)
		return func

	@staticmethod
	def _AppendAttribute(func: Callable, attribute: 'Attribute') -> None:
		# inherit attributes and prepend myself or create a new attributes list
		if (Attribute.__AttributesMemberName__ in func.__dict__):
			func.__dict__[Attribute.__AttributesMemberName__].insert(0, attribute)
		else:
			func.__setattr__(Attribute.__AttributesMemberName__, [attribute])


	@classmethod
	def GetMethods(cls, inst: Any, includeDerivedAttributes: bool=True) -> Dict[Callable, List['Attribute']]:
		methods = {}
		# print("-----------------------------------")
		# print(inst)
		classOfInst = inst.__class__
		if (classOfInst is type):
			classOfInst = inst

		mro = classOfInst.mro()

		# print(mro)

		# search in method-resolution-order (MRO)
		for c in mro:
			for function in c.__dict__.values():
				# print(functionName, function)
				if callable(function):
					# try to read '__pyattr__'
					try:
						attributes = function.__dict__[Attribute.__AttributesMemberName__]
						# print(attributes)
						if includeDerivedAttributes:
							for attribute in attributes:
								if isinstance(attribute, cls):
									try:
										methods[function].append(attribute)
									except KeyError:
										methods[function] = [attribute]
						else:
							for attribute in attributes:
								if type(attribute) is cls:
									try:
										methods[function].append(attribute)
									except KeyError:
										methods[function] = [attribute]

					except AttributeError:
						pass
					except KeyError:
						pass

		return methods

	@classmethod
	def GetAttributes(cls, method: Callable, includeSubClasses: bool=True) -> List['Attribute']:
		"""Returns attached attributes for a given method."""
		if (Attribute.__AttributesMemberName__ in method.__dict__):
			attributes = method.__dict__[Attribute.__AttributesMemberName__]
			if isinstance(attributes, list):
				return [attribute for attribute in attributes if isinstance(attribute, cls)]
		return list()


@export
class AttributeHelperMixin:
	"""A mixin class to ease finding methods with attached pyAttributes."""

	def GetMethods(self, filter: TAttributeFilter[TAttr]=Attribute) -> Union[Dict[Callable, List[TAttr]], bool]:
		if (filter is Attribute):
			pass
		elif (filter is None):
			filter = Attribute
		elif isinstance(filter, Iterable):
			filter = tuple([attribute for attribute in filter])

		# print("-----------------------------------")
		mro = self.__class__.mro()
		# print(mro)

		attributedMethods = OrderedDict()
		# search in method-resolution-order (MRO)
		for c in mro:
			for method in c.__dict__.values():
				# print(method)
				if isinstance(method, Callable):
					# print("  is callable")
					try:
						attributeList = method.__dict__[Attribute.__AttributesMemberName__]
						for attribute in attributeList:
							if isinstance(attribute, filter):
								try:
									attributedMethods[method].append(attribute)
								except KeyError:
									attributedMethods[method] = [attribute]

					except AttributeError:
						pass
					except KeyError:
						pass

		return attributedMethods

	@staticmethod
	def HasAttribute(method: Callable, filter: TAttributeFilter[TAttr]=Attribute) -> bool: # TODO: add a tuple based type filter
		"""Returns true, if the given method has pyAttributes attached."""
		try:
			attributeList = method.__dict__[Attribute.__AttributesMemberName__]
			if (len(attributeList) == 0):
				return False
			elif (filter is not None):
				if isinstance(filter, Attribute):
					pass
				elif isinstance(filter, Iterable):
					filter = tuple([attribute for attribute in filter])

				for attribute in attributeList:
					if isinstance(attribute, filter):
						return True
				else:
					return False
			else:
				return False
		except AttributeError:
			return False
		except KeyError:
			return False

	@staticmethod
	def GetAttributes(method: Callable, filter: TAttributeFilter[TAttr]=Attribute) -> List[TAttr]: # TODO: add a tuple based type filter
		"""Returns a list of pyAttributes attached to the given method."""

		try:
			attributeList = method.__dict__[Attribute.__AttributesMemberName__]
			if (filter is Attribute):
				pass
			elif (filter is None):
				filter = Attribute
			elif isinstance(filter, Iterable):
				filter = tuple([attribute for attribute in filter])

			attributes = []
			for attribute in attributeList:
				if isinstance(attribute, filter):
					attributes.append(attribute)

			return attributes

		except AttributeError:
			return list()
		except KeyError:
			return list()
