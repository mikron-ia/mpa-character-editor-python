from tests.test_domain import TestBase
from domain.skill import Skill
from domain.skill import Skills


class TestSkill(TestBase):
    def test_skill_string_conversion(self):
        skill_name = 'Strength'
        skill = Skill(skill_name, [])
        self.assertEqual(str(skill), skill_name + ': 0 + 0 = 0 (0)')


class TestSkills(TestBase):
    def test_empty_str(self):
        skills = Skills([])
        self.assertEqual('Skill: level + modifiers = value (minimum)\n', str(skills))

    def test_simple_skill_str(self):
        list_of_skills = [{'identifier': 'Fight', 'name': 'Fight'}]
        skills = Skills(list_of_skills)
        self.assertEqual('Skill: level + modifiers = value (minimum)\nFight: 0 + 0 = 0 (0)\n', str(skills))

    def test_incorrect_skill_str(self):
        list_of_attributes = [{'wrong': 'Fight', 'name': 'fight'}]
        skills = Skills(list_of_attributes)
        self.assertEqual({}, skills.skills)
