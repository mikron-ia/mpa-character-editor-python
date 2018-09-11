from tests.test_domain import TestBase
from domain.cost import *


class TestCost(TestBase):
    def test_constant(self):
        self.assertEqual([1, 1, 1, 1, 1], Cost.generate_progress_constant(5))

    def test_linear_simple(self):
        self.assertEqual([1, 2, 3, 4, 5], Cost.generate_progress_linear(5))

    def test_linear_complex(self):
        self.assertEqual([10, 11, 12, 13, 14], Cost.generate_progress_linear(5, 10))

    def test_quadratic_simple(self):
        self.assertEqual([1, 4, 9, 16, 25], Cost.generate_progress_quadratic(5))

    def test_quadratic_complex(self):
        self.assertEqual([9, 16, 25, 36, 49], Cost.generate_progress_quadratic(5, 3))

    def test_fibonacci_simple(self):
        self.assertEqual([1, 2, 3, 5, 8], Cost.generate_progress_fibonacci(5))

    def test_fibonacci_complex(self):
        self.assertEqual([3, 5, 8, 13, 21], Cost.generate_progress_fibonacci(5, 3))

    def test_sum_creation_standard(self):
        progress = [1, 2, 3, 4, 5, 6, 7]
        result = [1, 3, 6, 10, 15, 21, 28]
        self.assertEqual(result, Cost.create_cost_by_level(progress))

    def test_sum_creation_unusual(self):
        progress = [1, -1, 1, -1, 1, -1, 1]
        result = [1, 0, 1, 0, 1, 0, 1]
        self.assertEqual(result, Cost.create_cost_by_level(progress))

    def test_object_creation_simple(self):
        cost = Cost('linear', CostUnit(), limit=5)
        self.assertEqual([1, 2, 3, 4, 5], cost.of_level)
        self.assertEqual([1, 3, 6, 10, 15], cost.total_level)

    def test_object_creation_with_multiplication(self):
        cost = Cost('linear', CostUnit(), limit=5, multiplier=10)
        self.assertEqual([10, 20, 30, 40, 50], cost.of_level)
        self.assertEqual([10, 30, 60, 100, 150], cost.total_level)

    def test_object_creation_with_moved_start(self):
        cost = Cost('linear', CostUnit(), limit=5, start=3)
        self.assertEqual([3, 4, 5, 6, 7], cost.of_level)
        self.assertEqual([3, 7, 12, 18, 25], cost.total_level)

    def test_multiplier_application(self):
        progress = [1, 2, 3, 4, 5, 6, 7]
        result = [10, 20, 30, 40, 50, 60, 70]
        self.assertEqual(result, Cost.apply_multiplier(progress, 10))

    def test_comparison_equal(self):
        original = Cost('linear', CharacterPointAttribute())
        comparison = Cost('linear', CharacterPointAttribute())
        self.assertTrue(original == comparison)

    def test_comparison_not_equal(self):
        original = Cost('linear', CharacterPointAttribute())
        comparison = Cost('linear', CharacterPointAttribute())
        comparison.value = 1
        self.assertFalse(original == comparison)

    def test_comparison_incompatible_units(self):
        original = Cost('linear', CharacterPointAttribute())
        comparison = Cost('linear', CharacterPointSkill())
        self.assertFalse(original == comparison)

    def test_cost_creation_skill_standard(self):
        self.assertEqual(type(CharacterPointSkill()), type(CostUnit.create('SP')))

    def test_cost_creation_skill_lowercase(self):
        self.assertEqual(type(CharacterPointSkill()), type(CostUnit.create('sp')))

    def test_cost_creation_from_config_empty(self):
        cost = Cost.create({})
        self.assertEqual({}, cost)

    def test_cost_creation_from_config_basic(self):
        config = {'attributes': {}}
        cost = Cost.create(config)
        attribute_config = cost['attributes']

        self.assertEqual(CharacterPoint, type(attribute_config.unit))
        self.assertEqual(attribute_config.of_level, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_cost_creation_from_config_complex(self):
        config = {
            'attributes': {
                'progression': 'linear',
                'start': 2,
                'multiplier': 10,
                'limit': 4,
                'unit': 'ap'
            },
            'skills': {}
        }
        cost = Cost.create(config)
        attribute_config = cost['attributes']

        self.assertEqual(CharacterPointAttribute, type(attribute_config.unit))
        self.assertEqual(attribute_config.of_level, [20, 30, 40, 50])
