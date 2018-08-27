class Component:
    def __init__(self, name, description: list):
        self.name = name
        self.description = description

    def get_description_formatted(self):
        return '\n\n'.join(self.description)

    def get_value(self):
        return '?'
