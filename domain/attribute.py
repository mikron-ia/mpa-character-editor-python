from domain.component import ComponentWithLevel
from domain.component import ComponentContainer


class Attribute(ComponentWithLevel):
    def __init__(self, name, description: list):
        super().__init__(name, description)

    def __str__(self):
        return self.name + ': ' + str(self.level) + ' + ' + str(self.modifiers) + ' = ' + str(self.value)


class Attributes(ComponentContainer):
    def __init__(self, content: dict):
        super().__init__()
        self.content = content

    def __str__(self):
        strings = 'Attribute: level + modifiers = value\n'
        for identifier, attribute in self.content.items():
            strings += str(attribute) + '\n'
        return strings

    @staticmethod
    def create(config: list):
        attributes = dict()
        for attribute_row in config:
            if 'identifier' in attribute_row and 'name' in attribute_row:
                attributes[attribute_row['identifier']] = Attribute(
                    attribute_row['name'],
                    attribute_row['description'] if 'description' in attribute_row else '[no description]'
                )
        return Attributes(attributes)
