from typing       import Generator, Dict, TypeVar, Tuple
from unittest     import TestCase

from pyAttributes import Attribute, AttributeHelperMixin


if __name__ == "__main__":
	print("ERROR: you called a testcase declaration file as an executable module.")
	print("Use: 'python -m unitest <testcase module>'")
	exit(1)


K1 = TypeVar("K1")
V1 = TypeVar("V1")
K2 = TypeVar("K2")
V2 = TypeVar("V2")

def zip(dict1: Dict[K1, V1], dict2: Dict[K2, V2]) -> Generator[Tuple[K1, K2, V1, V2], None, None]:
	l1 = len(dict1)
	l2 = len(dict2)

	if (l1 != l2):
		if (l1 < l2):
			raise ValueError("'dict1' (len={}) has less elements than 'dict2' (len={}).".format(l1, l2))
		else:
			raise ValueError("'dict1' (len={}) has more elements than 'dict2' (len={}).".format(l1, l2))

	iter1 = iter(dict1.items())
	iter2 = iter(dict2.items())

	try:
		while True:
			key1, value1 = next(iter1)
			key2, value2 = next(iter2)

			yield (key1, key2, value1, value2)

	except StopIteration:
		return


class Attribute1(Attribute):
	pass


class Attribute2(Attribute1):
	pass


class Attribute3(Attribute):
	pass


class Attribute4(Attribute):
	pass


class Attribute5(Attribute1):
	pass


class NoAttributes(AttributeHelperMixin):
	def __init__(self):
		AttributeHelperMixin.__init__(self)

	def method_1(self):
		pass


class NoMixIn:
	@Attribute1()
	def method_1(self):
		pass


class BaseClass1:
	@Attribute1()
	def method_1(self):
		pass

	@Attribute2()
	def method_2(self):
		pass

	@Attribute2()
	@Attribute3()
	def method_3(self):
		pass


class BaseClass2:
	@Attribute1()
	def method_4(self):
		pass

	@Attribute2()
	def method_5(self):
		pass


class BaseClass3(BaseClass2):
	@Attribute2()
	@Attribute3()
	@Attribute4()
	def method_6(self):
		pass


class MainClass(AttributeHelperMixin, BaseClass1, BaseClass3):
	def __init__(self):
		AttributeHelperMixin.__init__(self)

	def method_0(self):
		pass

	@Attribute4()
	def method_7(self):
		pass

	@Attribute1()
	@Attribute5()
	def method_8(self):
		pass


class HasHelperMixin_NoAttributes(TestCase):
	uut: NoAttributes

	def setUp(self) -> None:
		self.uut = NoAttributes()

	def test_GetAttributesIsAnEmptyList(self):
		attributeList = self.uut.GetAttributes(self.uut.method_1)
		self.assertIsInstance(attributeList, list, "GetAttributes(...) doesn't return a list.")
		self.assertEqual(len(attributeList), 0, "GetAttributes(...) doesn't return an empty list (len=0).")

	def test_HasAttributeIsFalse(self):
		hasAttribute = self.uut.HasAttribute(self.uut.method_1)
		self.assertFalse(hasAttribute, "HasAttribute should be False on a non-attributed method.")

	def test_GetMethodsIsAnEmptyList(self):
		methodList = self.uut.GetMethods()
		# self.assertIsInstance(methodList, dict_items, "GetMethods(...) doesn't return dict_items.")
		self.assertEqual(0, len(methodList), "GetMethods(...) doesn't return an empty list (len=0).")


class NoHelperMixin_HasAttributes(TestCase):
	uut : NoMixIn

	def setUp(self) -> None:
		self.uut = NoMixIn()

	def test_GetMethodsHasOneElement(self):
		methodList = Attribute1.GetMethods(self.uut)

		#self.assertIsInstance(methodList, dict_items, "GetMethods(...) doesn't return list.")
		self.assertEqual(1, len(methodList), "GetMethods(...) doesn't return a list with 1 element (len=1).")
		self.assertIn(NoMixIn.method_1, methodList, "GetMethods didn't list 'method_1'.")

	def test_GetAttributes(self):
		attributeList = Attribute1.GetAttributes(self.uut.method_1)


class TestFromClassInstance(TestCase):
	uut : MainClass

	def setUp(self) -> None:
		self.uut = MainClass()

	def test_GetMethods_IncludeDevicedAttributes(self):
		for attribute, count in ((Attribute1, 7), (Attribute2, 4), (Attribute3, 2), (Attribute4, 2), (Attribute5, 1)):
			methodList = attribute.GetMethods(self.uut)

			self.assertEqual(count, len(methodList), "GetMethods(...) doesn't return a list of {count} elements.".format(count=count))

	def test_GetMethods_ExcludeDerivedAttributes(self):
		for attribute, count in ((Attribute1, 3), (Attribute2, 4), (Attribute3, 2), (Attribute4, 2), (Attribute5, 1)):
			methodList = attribute.GetMethods(self.uut, includeDerivedAttributes=False)

			self.assertEqual(count, len(methodList), "GetMethods(...) doesn't return a list of {count} elements.".format(count=count))

	def test_GetAttributes_Method1(self):
		attributeList = self.uut.GetAttributes(self.uut.method_1)

		attributes = [attribute.__class__ for attribute in attributeList]
		self.assertListEqual(attributes, [Attribute1])

	def test_GetAttributes_Method2(self):
		attributeList = self.uut.GetAttributes(self.uut.method_2)

		attributes = [attribute.__class__ for attribute in attributeList]
		self.assertListEqual(attributes, [Attribute2])

	def test_GetAttributes_Method6_DefaultFilter(self):
		attributeList = self.uut.GetAttributes(self.uut.method_6)

		attributes = [attribute.__class__ for attribute in attributeList]
		self.assertListEqual(attributes, [Attribute4, Attribute3, Attribute2])

	def test_GetAttributes_Method6_FilterNone(self):
		attributeList = self.uut.GetAttributes(self.uut.method_6, None)

		attributes = [attribute.__class__ for attribute in attributeList]
		self.assertListEqual(attributes, [Attribute4, Attribute3, Attribute2])

	def test_GetAttributes_Method6_FilterAttribute5(self):
		attributeList = self.uut.GetAttributes(self.uut.method_6, Attribute5)

		attributes = [attribute.__class__ for attribute in attributeList]
		self.assertListEqual(attributes, [])

	def test_GetAttributes_Method6_FilterAttribute2(self):
		attributeList = self.uut.GetAttributes(self.uut.method_6, Attribute2)

		attributes = [attribute.__class__ for attribute in attributeList]
		self.assertListEqual(attributes, [Attribute2])

	def test_GetAttributes_Method6_FilterAttribute3OrAttribute4(self):
		attributeList = self.uut.GetAttributes(self.uut.method_6, (Attribute3, Attribute4))

		attributes = [attribute.__class__ for attribute in attributeList]
		self.assertListEqual(attributes, [Attribute4, Attribute3])

	def test_GetMethods_DefaultFilter(self):
		methodList = self.uut.GetMethods()

		self.assertIsNot(methodList, False, "GetMethods(...) doesn't return a dict.")

		expected = {
			MainClass.method_7:  [Attribute4],
			MainClass.method_8:  [Attribute5, Attribute1],
			BaseClass1.method_1: [Attribute1],
			BaseClass1.method_2: [Attribute2],
			BaseClass1.method_3: [Attribute3, Attribute2],
			BaseClass3.method_6: [Attribute4, Attribute3, Attribute2],
			BaseClass2.method_4: [Attribute1],
			BaseClass2.method_5: [Attribute2]
		}

		for actualMethod, expectedMethod, actualAttributes, expectedAttributes in zip(methodList, expected):
			self.assertIs(actualMethod, expectedMethod)

			attributes = [attribute.__class__ for attribute in actualAttributes]
			self.assertListEqual(attributes, expectedAttributes)

	def test_GetMethods_FilterNone(self):
		methodList = self.uut.GetMethods(None)

		self.assertIsNot(methodList, False, "GetMethods(...) doesn't return a dict.")

		expected = {
			MainClass.method_7:  [Attribute4],
			MainClass.method_8:  [Attribute5, Attribute1],
			BaseClass1.method_1: [Attribute1],
			BaseClass1.method_2: [Attribute2],
			BaseClass1.method_3: [Attribute3, Attribute2],
			BaseClass3.method_6: [Attribute4, Attribute3, Attribute2],
			BaseClass2.method_4: [Attribute1],
			BaseClass2.method_5: [Attribute2]
		}

		for actualMethod, expectedMethod, actualAttributes, expectedAttributes in zip(methodList, expected):
			self.assertIs(actualMethod, expectedMethod)

			attributes = [attribute.__class__ for attribute in actualAttributes]
			self.assertListEqual(attributes, expectedAttributes)

	def test_GetMethods_FilterAttribute1(self):
		methodList = self.uut.GetMethods(Attribute1)

		self.assertIsNot(methodList, False, "GetMethods(...) doesn't return a dict.")

		expected = {
			MainClass.method_8:  [Attribute5, Attribute1],
			BaseClass1.method_1: [Attribute1],
			BaseClass1.method_2: [Attribute2],
			BaseClass1.method_3: [Attribute2],
			BaseClass3.method_6: [Attribute2],
			BaseClass2.method_4: [Attribute1],
			BaseClass2.method_5: [Attribute2]
		}

		for m in methodList:
			print(m)

		for actualMethod, expectedMethod, actualAttributes, expectedAttributes in zip(methodList, expected):
			self.assertIs(actualMethod, expectedMethod)

			attributes = [attribute.__class__ for attribute in actualAttributes]
			self.assertListEqual(attributes, expectedAttributes)

	def test_GetMethods_FilterAttribute2(self):
		methodList = self.uut.GetMethods(Attribute2)

		self.assertIsNot(methodList, False, "GetMethods(...) doesn't return a dict.")

		expected = {
			BaseClass1.method_2: [Attribute2],
			BaseClass1.method_3: [Attribute2],
			BaseClass3.method_6: [Attribute2],
			BaseClass2.method_5: [Attribute2]
		}

		for actualMethod, expectedMethod, actualAttributes, expectedAttributes in zip(methodList, expected):
			self.assertIs(actualMethod, expectedMethod)

			attributes = [attribute.__class__ for attribute in actualAttributes]
			self.assertListEqual(attributes, expectedAttributes)

	def test_GetMethods_FilterAttribute3(self):
		methodList = self.uut.GetMethods(Attribute3)

		self.assertIsNot(methodList, False, "GetMethods(...) doesn't return a dict.")

		expected = {
			BaseClass1.method_3: [Attribute3],
			BaseClass3.method_6: [Attribute3]
		}

		for actualMethod, expectedMethod, actualAttributes, expectedAttributes in zip(methodList, expected):
			self.assertIs(actualMethod, expectedMethod)

			attributes = [attribute.__class__ for attribute in actualAttributes]
			self.assertListEqual(attributes, expectedAttributes)

	def test_GetMethods_FilterAttribute4(self):
		methodList = self.uut.GetMethods(Attribute4)

		self.assertIsNot(methodList, False, "GetMethods(...) doesn't return a dict.")

		expected = {
			MainClass.method_7:  [Attribute4],
			BaseClass3.method_6: [Attribute4]
		}

		for actualMethod, expectedMethod, actualAttributes, expectedAttributes in zip(methodList, expected):
			self.assertIs(actualMethod, expectedMethod)

			attributes = [attribute.__class__ for attribute in actualAttributes]
			self.assertListEqual(attributes, expectedAttributes)

	def test_GetMethods_FilterAttribute5(self):
		methodList = self.uut.GetMethods(Attribute5)

		self.assertIsNot(methodList, False, "GetMethods(...) doesn't return a dict.")

		expected = {
			MainClass.method_8:   [Attribute5]
		}

		for actualMethod, expectedMethod, actualAttributes, expectedAttributes in zip(methodList, expected):
			self.assertIs(actualMethod, expectedMethod)

			attributes = [attribute.__class__ for attribute in actualAttributes]
			self.assertListEqual(attributes, expectedAttributes)
