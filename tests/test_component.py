from tests.test_domain import TestBase
from domain.component import Component
from domain.component import ComponentWithLevel


class TestComponent(TestBase):
    def test_name(self):
        name = 'Strength'
        component = Component(name, [])
        self.assertEqual(component.name, name)

    def test_description(self):
        description = ['Alpha', 'Beta']
        component = Component('Strength', description)
        self.assertEqual(component.description, description)

    def test_description_concatenation(self):
        description = ['Alpha', 'Beta']
        component = Component('Strength', description)
        self.assertEqual(component.description_formatted, 'Alpha\n\nBeta')


class TestComponentWithLevel(TestBase):
    def test_default_level(self):
        component = ComponentWithLevel('Name', [])
        self.assertEqual(component.level, 0)

    def test_default_modifiers(self):
        component = ComponentWithLevel('Name', [])
        self.assertEqual(component.modifiers, 0)

    def test_increase(self):
        component = ComponentWithLevel('Name', [])
        component.increase()
        self.assertEqual(component.level, 1)

    def test_decrease(self):
        component = ComponentWithLevel('Name', [])
        component.decrease()
        self.assertEqual(component.level, -1)

    def test_setter(self):
        component = ComponentWithLevel('Name', [])
        component.level = 2
        self.assertEqual(component.level, 2)
