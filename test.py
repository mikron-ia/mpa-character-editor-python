from tests.test_domain import TestComponent
from tests.test_domain import TestAttribute
from tests.test_domain import TestAttributes

if __name__ == "__main__":
    component_tests = TestComponent()
    component_tests.go()

    attribute_tests = TestAttribute()
    attribute_tests.go()

    attributes_tests = TestAttributes()
    attributes_tests.go()
