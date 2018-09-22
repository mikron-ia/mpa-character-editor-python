from tests.test_domain import TestBase
from domain.group_skill import GroupSkill


class TestGroupSkill(TestBase):
    def test_skill_subject(self):
        skill_name = 'Craft'
        skill_subject = 'Knitting'

        skill = GroupSkill(skill_name, [])
        skill.subject = skill_subject

        self.assertEqual(skill.name, skill_name + ' (' + skill_subject + ')')

    def test_skill_string_conversion(self):
        skill_name = 'Art'
        skill = GroupSkill(skill_name, [])
        self.assertEqual(str(skill), skill_name + ': 0 + 0 = 0 (0)')
