from tests.test_cost import *
from tests.test_component import *
from tests.test_attributes import *
from tests.test_skills import *
from tests.test_group_skills import *

if __name__ == "__main__":
    TestCost().go()
    TestComponent().go()
    TestAttribute().go()
    TestAttributes().go()
    TestSkill().go()
    TestSkills().go()
    TestGroupSkill().go()
