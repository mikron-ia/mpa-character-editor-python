class Component:
    def __init__(self, name, description: list):
        self.__name = name
        self.__description = description

    @property
    def value(self):
        raise NotImplementedError

    @property
    def name(self):
        return self.__name

    @property
    def description(self):
        return self.__description

    @property
    def description_formatted(self):
        return '\n\n'.join(self.description)


class ComponentWithLevel(Component):
    def __init__(self, name, description: list):
        super().__init__(name, description)
        self.level = 0
        self.modifiers = 0  # todo Rework it into a list or set of known modifiers

    def increase(self):
        self.level += 1

    def decrease(self):
        self.level -= 1

    @property
    def value(self):
        return self.level + self.modifiers
