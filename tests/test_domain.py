from domain.component import Component
from domain.attribute import Attribute
from domain.attribute import Attributes
from domain.skill import Skill
from domain.skill import Skills

import unittest


class TestBase(unittest.TestCase):
    @staticmethod
    def go():
        unittest.main()


class TestComponent(TestBase):
    def test__name(self):
        name = 'Strength'
        component = Component(name, [])
        self.assertEqual(component.name, name)

    def test__description(self):
        description = ['Alpha', 'Beta']
        component = Component('Strength', description)
        self.assertEqual(component.description, description)

    def test__description_concatenation(self):
        description = ['Alpha', 'Beta']
        component = Component('Strength', description)
        self.assertEqual(component.get_description_formatted(), 'Alpha\n\nBeta')


class TestAttribute(TestBase):
    def test_attribute_string_conversion(self):
        attribute_name = 'Strength'
        attribute = Attribute(attribute_name, [])
        self.assertEqual(str(attribute), attribute_name + ': 0 + 0 = 0')


class TestAttributes(TestBase):
    def test_empty_str(self):
        attributes = Attributes([])
        self.assertEqual('Attribute: level + modifiers = value\n', str(attributes))

    def test_simple_attribute_str(self):
        list_of_attributes = [{'identifier': 'STR', 'name': 'Strength'}]
        attributes = Attributes(list_of_attributes)
        self.assertEqual('Attribute: level + modifiers = value\nStrength: 0 + 0 = 0\n', str(attributes))

    def test_incorrect_attribute_str(self):
        list_of_attributes = [{'wromng': 'STR', 'name': 'Strength'}]
        attributes = Attributes(list_of_attributes)
        self.assertEqual({}, attributes.attributes)


class TestSkill(TestBase):
    def test_skill_string_conversion(self):
        skill_name = 'Strength'
        skill = Skill(skill_name, [])
        self.assertEqual(str(skill), skill_name + ': 0 + 0 = 0')


class TestSkills(TestBase):
    def test_empty_str(self):
        skills = Skills([])
        self.assertEqual('Skill: level + modifiers = value\n', str(skills))

    def test_simple_skill_str(self):
        list_of_skills = [{'identifier': 'Fight', 'name': 'Fight'}]
        skills = Skills(list_of_skills)
        self.assertEqual('Skill: level + modifiers = value\nFight: 0 + 0 = 0\n', str(skills))

    def test_incorrect_skill_str(self):
        list_of_attributes = [{'wrong': 'Fight', 'name': 'fight'}]
        skills = Skills(list_of_attributes)
        self.assertEqual({}, skills.skills)
