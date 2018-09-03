from tests.test_domain import TestBase
from domain.cost import Cost


class TestCost(TestBase):
    def test_constant(self):
        self.assertEqual([1, 1, 1, 1, 1], Cost.generate_progress_constant(5))

    def test_linear(self):
        self.assertEqual([1, 2, 3, 4, 5], Cost.generate_progress_linear(5))

    def test_quadratic(self):
        self.assertEqual([1, 4, 9, 16, 25], Cost.generate_progress_quadratic(5))

    def test_fibonacci(self):
        self.assertEqual([1, 2, 3, 5, 8], Cost.generate_progress_fibonacci(5))

    def test_sum_creation(self):
        progress = [1, 2, 3, 4, 5, 6, 7]
        result = [1, 3, 6, 10, 15, 21, 28]
        self.assertEqual(result, Cost.create_cost_by_level(progress))
