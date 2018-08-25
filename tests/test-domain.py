from domain.attribute import Attribute

import unittest


class TestAttribute(unittest.TestCase):
    def test_attribute_name(self):
        attribute_name = 'Strength'
        attribute = Attribute(attribute_name)
        self.assertEqual(attribute.name, attribute_name)

    def test_attribute_string_conversion(self):
        attribute_name = 'Strength'
        attribute = Attribute(attribute_name)
        self.assertEqual(str(attribute), attribute_name + ': 0 + 0 = 0')


if __name__ == '__main__':
    unittest.main()
