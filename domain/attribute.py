class Attribute:
    def __init__(self, name, description=''):
        self.name = name
        self.description = description
        self.level = 0
        self.modifiers = 0  # @todo Rework it into a list or set of known modifiers

    def get_value(self):
        return self.level + self.modifiers

    def __str__(self):
        return self.name + ': ' + str(self.level) + ' + ' + str(self.modifiers) + ' = ' + str(self.get_value())


class Attributes:
    def __init__(self, attribute_config: list):
        attributes = dict()
        for attribute_row in attribute_config:
            if 'id' in attribute_row and 'name' in attribute_row:
                attributes[attribute_row['id']] = Attribute(
                    attribute_row['name'],
                    attribute_row['description'] if 'description' in attribute_row else '[no description]'
                )
        self.attributes = attributes

    def list_attributes(self):
        for id, attribute in self.attributes.items():
            print(attribute)
