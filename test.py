from tests.test_domain import TestComponent
from tests.test_domain import TestAttribute
from tests.test_domain import TestAttributes
from tests.test_domain import TestSkill
from tests.test_domain import TestSkills

if __name__ == "__main__":
    component_tests = TestComponent()
    component_tests.go()

    attribute_tests = TestAttribute()
    attribute_tests.go()

    attributes_tests = TestAttributes()
    attributes_tests.go()

    skill_test = TestSkill()
    skill_test.go()

    skills_test = TestSkills()
    skills_test.go()
