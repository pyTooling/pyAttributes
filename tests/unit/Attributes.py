from unittest import TestCase

from pyAttributes import Attribute, AttributeHelperMixin


if __name__ == "__main__":
	print("ERROR: you called a testcase declaration file as an executable module.")
	print("Use: 'python -m unitest <testcase module>'")
	exit(1)


class Attribute_1(Attribute):
	pass

class Attribute_2(Attribute_1):
	pass

class Attribute_3(Attribute):
	pass

class Attribute_4(Attribute):
	pass

class Attribute_5(Attribute_1):
	pass


class NoAttributes(AttributeHelperMixin):
	def __init__(self):
		AttributeHelperMixin.__init__(self)

	def method_1(self):
		pass

class NoMixIn:
	@Attribute_1()
	def method_1(self):
		pass


class BaseClass_1:
	@Attribute_1()
	def method_1(self):
		pass

	@Attribute_2()
	def method_2(self):
		pass

	@Attribute_2()
	@Attribute_3()
	def method_3(self):
		pass


class BaseClass_2:
	@Attribute_1()
	def method_4(self):
		pass

	@Attribute_2()
	def method_5(self):
		pass


class BaseClass_3(BaseClass_2):
	@Attribute_2()
	@Attribute_3()
	@Attribute_4()
	def method_6(self):
		pass


class MainClass(AttributeHelperMixin, BaseClass_1, BaseClass_3):
	def __init__(self):
		AttributeHelperMixin.__init__(self)

	def method_0(self):
		pass

	@Attribute_4()
	def method_7(self):
		pass

	@Attribute_1()
	@Attribute_5()
	def method_8(self):
		pass


class HasHelperMixin_NoAttributes(TestCase):
	uut : NoAttributes

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
		methodList = Attribute_1.GetMethods(self.uut)

		#self.assertIsInstance(methodList, dict_items, "GetMethods(...) doesn't return list.")
		self.assertEqual(1, len(methodList), "GetMethods(...) doesn't return a list with 1 element (len=1).")
		self.assertIn(NoMixIn.method_1, methodList, "GetMethods didn't list 'method_1'.")

	def test_GetAttributes(self):
		attributeList = Attribute_1.GetAttributes(self.uut.method_1)


class TestFromClassInstance(TestCase):
	uut : MainClass

	def setUp(self) -> None:
		self.uut = MainClass()

	def test_GetMethods_IncludeDevicedAttributes(self):
		for attribute, count in ((Attribute_1, 7), (Attribute_2, 4), (Attribute_3, 2), (Attribute_4, 2), (Attribute_5, 1)):
			methodList = attribute.GetMethods(self.uut)

			self.assertEqual(count, len(methodList), "GetMethods(...) doesn't return a list of {count} elements.".format(count=count))

	def test_GetMethods_ExcludeDerivedAttributes(self):
		for attribute, count in ((Attribute_1, 3), (Attribute_2, 4), (Attribute_3, 2), (Attribute_4, 2), (Attribute_5, 1)):
			methodList = attribute.GetMethods(self.uut, includeDerivedAttributes=False)

			self.assertEqual(count, len(methodList), "GetMethods(...) doesn't return a list of {count} elements.".format(count=count))

	def test_GetAttributes_Method1(self):
		attributeList = self.uut.GetAttributes(self.uut.method_1)

		attributes = [attribute.__class__ for attribute in attributeList]
		self.assertListEqual(attributes, [Attribute_1])

	def test_GetAttributes_Method2(self):
		attributeList = self.uut.GetAttributes(self.uut.method_2)

		attributes = [attribute.__class__ for attribute in attributeList]
		self.assertListEqual(attributes, [Attribute_2])

	def test_GetAttributes_Method6_DefaultFilter(self):
		attributeList = self.uut.GetAttributes(self.uut.method_6)

		attributes = [attribute.__class__ for attribute in attributeList]
		self.assertListEqual(attributes, [Attribute_4, Attribute_3, Attribute_2])

	def test_GetAttributes_Method6_FilterNone(self):
		attributeList = self.uut.GetAttributes(self.uut.method_6, None)

		attributes = [attribute.__class__ for attribute in attributeList]
		self.assertListEqual(attributes, [Attribute_4, Attribute_3, Attribute_2])

	def test_GetAttributes_Method6_FilterAttribute5(self):
		attributeList = self.uut.GetAttributes(self.uut.method_6, Attribute_5)

		attributes = [attribute.__class__ for attribute in attributeList]
		self.assertListEqual(attributes, [])

	def test_GetAttributes_Method6_FilterAttribute2(self):
		attributeList = self.uut.GetAttributes(self.uut.method_6, Attribute_2)

		attributes = [attribute.__class__ for attribute in attributeList]
		self.assertListEqual(attributes, [Attribute_2])

	def test_GetAttributes_Method6_FilterAttribute3OrAttribute4(self):
		attributeList = self.uut.GetAttributes(self.uut.method_6, (Attribute_3, Attribute_4))

		attributes = [attribute.__class__ for attribute in attributeList]
		self.assertListEqual(attributes, [Attribute_4, Attribute_3])

	def test_GetMethods_aaa(self):
		methodList = self.uut.GetMethods()

		methods = [method for method in methodList.keys()]
		# self.assertListEqual(methods, [self.uut.method_1, self.uut.method_2, self.uut.method_3, self.uut.method_4, self.uut.method_5, self.uut.method_6, self.uut.method_7, self.uut.method_8])

		for method, attributes in methodList.items():
			print(method)

			for attribute in attributes:
				print(" ", attribute)

