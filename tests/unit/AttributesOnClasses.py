# ==================================================================================================================== #
#                  _   _   _        _ _           _                                                                    #
#   _ __  _   _   / \ | |_| |_ _ __(_) |__  _   _| |_ ___  ___                                                         #
#  | '_ \| | | | / _ \| __| __| '__| | '_ \| | | | __/ _ \/ __|                                                        #
#  | |_) | |_| |/ ___ \ |_| |_| |  | | |_) | |_| | ||  __/\__ \                                                        #
#  | .__/ \__, /_/   \_\__|\__|_|  |_|_.__/ \__,_|\__\___||___/                                                        #
#  |_|    |___/                                                                                                        #
# ==================================================================================================================== #
# Authors:                                                                                                             #
#   Patrick Lehmann                                                                                                    #
#                                                                                                                      #
# License:                                                                                                             #
# ==================================================================================================================== #
# Copyright 2017-2021 Patrick Lehmann - Bötzingen, Germany                                                             #
# Copyright 2007-2016 Patrick Lehmann - Dresden, Germany                                                               #
#                                                                                                                      #
# Licensed under the Apache License, Version 2.0 (the "License");                                                      #
# you may not use this file except in compliance with the License.                                                     #
# You may obtain a copy of the License at                                                                              #
#                                                                                                                      #
#   http://www.apache.org/licenses/LICENSE-2.0                                                                         #
#                                                                                                                      #
# Unless required by applicable law or agreed to in writing, software                                                  #
# distributed under the License is distributed on an "AS IS" BASIS,                                                    #
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.                                             #
# See the License for the specific language governing permissions and                                                  #
# limitations under the License.                                                                                       #
#                                                                                                                      #
# SPDX-License-Identifier: Apache-2.0                                                                                  #
# ==================================================================================================================== #
#
"""\
Unit tests for attributes attached to methods.

:copyright: Copyright 2007-2021 Patrick Lehmann - Bötzingen, Germany
:license: Apache License, Version 2.0
"""
from unittest     import TestCase

from pyAttributes import Attribute, AttributeHelperMixin

from .            import zip


if __name__ == "__main__": # pragma: no cover
	print("ERROR: you called a testcase declaration file as an executable module.")
	print("Use: 'python -m unitest <testcase module>'")
	exit(1)


class Attribute1(Attribute):
	pass

class Attribute2(Attribute):
	pass

class Attribute3(Attribute):
	pass

@Attribute1()
class Class1():
	pass

@Attribute2()
class Class11(Class1):
	pass

@Attribute2()
class Class12(Class11):
	pass

@Attribute3()
class Class2():
	pass

class Classes(TestCase):
	def test_FindClasses(self):
		self.assertIs(Class1, Attribute1.GetClasses()[0])

	def test_FindSubClasses(self):
		print("Attribute")
		for c in Attribute._classes:
			print(c)
		print("Attribute1")
		for c in Attribute1._classes:
			print(c)
		print("Attribute2")
		for c in Attribute2._classes:
			print(c)
		print("Attribute3")
		for c in Attribute3._classes:
			print(c)

		self.assertIs(Class11, Attribute2.GetClasses(Class1)[0])
		self.assertIs(Class12, Attribute2.GetClasses(Class1)[1])
