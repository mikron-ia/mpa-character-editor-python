from tests.test_domain import TestBase
from domain.attribute import Attribute
from domain.attribute import Attributes


class TestAttribute(TestBase):
    def test_attribute_string_conversion(self):
        attribute_name = 'Strength'
        attribute = Attribute(attribute_name, [])
        self.assertEqual(str(attribute), attribute_name + ': 0 + 0 = 0')


class TestAttributes(TestBase):
    def test_empty_str(self):
        attributes = Attributes.create([])
        self.assertEqual('Attribute: level + modifiers = value\n', str(attributes))

    def test_simple_attribute_str(self):
        list_of_attributes = [{'identifier': 'STR', 'name': 'Strength'}]
        attributes = Attributes.create(list_of_attributes)
        self.assertEqual('Attribute: level + modifiers = value\nStrength: 0 + 0 = 0\n', str(attributes))

    def test_incorrect_attribute_str(self):
        list_of_attributes = [{'wrong': 'STR', 'name': 'Strength'}]
        attributes = Attributes.create(list_of_attributes)
        self.assertEqual({}, attributes.attributes)
