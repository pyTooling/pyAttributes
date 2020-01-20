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


class NoAttributes(AttributeHelperMixin):
	def __init__(self):
		AttributeHelperMixin.__init__(self)

	def method_1(self):
		pass

class NoMixIn:
	@Attribute_1()
	def method_1(self):
		pass


class Class_1:
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


class Class_2(AttributeHelperMixin, Class_1):
	def __init__(self):
		AttributeHelperMixin.__init__(self)

	@Attribute_4()
	def method_4(self):
		pass

	@Attribute_1()
	def method_5(self):
		pass


class HasHelperMixin_NoAttributes(TestCase):
	def test_GetAttributesIsAnEmptyList(self):
		i = NoAttributes()

		attributeList = i.GetAttributes(i.method_1)
		self.assertIsInstance(attributeList, list, "GetAttributes(...) doesn't return a list.")
		self.assertEqual(len(attributeList), 0, "GetAttributes(...) doesn't return an empty list (len=0).")

	def test_HasAttributeIsFalse(self):
		i = NoAttributes()

		hasAttribute = i.HasAttribute(i.method_1)
		self.assertFalse(hasAttribute, "HasAttribute should be False on a non-attributed method.")

	def test_GetMethodsIsAnEmptyList(self):
		i = NoAttributes()

		methodList = i.GetMethods()
		# self.assertIsInstance(methodList, dict_items, "GetMethods(...) doesn't return dict_items.")
		self.assertEqual(0, len(methodList), "GetMethods(...) doesn't return an empty list (len=0).")


class NoHelperMixin_HasAttributes(TestCase):
	def test_GetMethodsHasOneElement(self):
		i = NoMixIn()
		methodList = Attribute_1.GetMethods(i)

		#self.assertIsInstance(methodList, dict_items, "GetMethods(...) doesn't return list.")
		self.assertEqual(1, len(methodList), "GetMethods(...) doesn't return a list with 1 element (len=1).")
		self.assertIn(NoMixIn.method_1, methodList, "GetMethods didn't list 'method_1'.")

	def test_GetAttributes(self):
		i = NoMixIn()
		attributeList = Attribute_1.GetAttributes(i.method_1)
