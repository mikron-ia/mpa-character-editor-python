from tests.test_domain import TestBase
from domain.component import Component


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
