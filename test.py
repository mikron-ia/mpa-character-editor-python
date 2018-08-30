# Test file until some more state-of-art tests are made

from tests.test_domain import TestAttribute


if __name__ == "__main__":
    attribute_tests = TestAttribute()
    attribute_tests.go()
