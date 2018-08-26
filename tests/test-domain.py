from domain.attribute import Attribute

import unittest


class TestAttribute(unittest.TestCase):
    def test_attribute_name(self):
        attribute_name = 'Strength'
        attribute = Attribute(attribute_name, [])
        self.assertEqual(attribute.name, attribute_name)

    def test_attribute_description(self):
        attribute_description = ['Alpha', 'Beta']
        attribute = Attribute('Strength', attribute_description)
        self.assertEqual(attribute.description, attribute_description)

    def test_attribute_description_concatenation(self):
        attribute_description = ['Alpha', 'Beta']
        attribute = Attribute('Strength', attribute_description)
        self.assertEqual(attribute.get_description_formatted(), 'Alpha\n\nBeta')

    def test_attribute_string_conversion(self):
        attribute_name = 'Strength'
        attribute = Attribute(attribute_name, [])
        self.assertEqual(str(attribute), attribute_name + ': 0 + 0 = 0')


if __name__ == '__main__':
    unittest.main()
