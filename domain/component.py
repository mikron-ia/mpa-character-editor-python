class Component:
    def __init__(self, name, description: list):
        self.name = name
        self.description = description

    def get_description_formatted(self):
        return '\n\n'.join(self.description)

    def get_value(self):
        raise NotImplementedError


class ComponentWithLevel(Component):
    def __init__(self, name, description: list):
        super().__init__(name, description)
        self.level = 0
        self.modifiers = 0  # todo Rework it into a list or set of known modifiers

    def increase(self):
        self.level += 1

    def decrease(self):
        self.level -= 1

    def set(self, level):
        self.level = level

    def get_value(self):
        return self.level + self.modifiers
