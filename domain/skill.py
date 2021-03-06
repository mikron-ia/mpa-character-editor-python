from domain.component import ComponentWithLevel
from domain.component import ComponentContainer


class Skill(ComponentWithLevel):
    def __init__(self, name, description: list):
        super().__init__(name, description)
        self.minimum = 0  # todo maybe as modifier?

    def get_value(self):
        return max(self.minimum, self.level + self.modifiers)

    def __str__(self):
        return self.name + ': ' \
               + str(self.level) + ' + ' \
               + str(self.modifiers) + ' = ' \
               + str(self.get_value()) + ' (' + str(self.minimum) + ')'


class Skills(ComponentContainer):
    def __init__(self, content: dict):
        super().__init__()
        self.content = content

    def __str__(self):
        strings = 'Skill: level + modifiers = value (minimum)\n'
        for identifier, attribute in self.content.items():
            strings += str(attribute) + '\n'
        return strings

    def append(self, name: str, skill: Skill):
        self.content[name] = skill

    @staticmethod
    def create(config: list):
        skills = dict()
        for skill_row in config:
            if 'identifier' in skill_row and 'name' in skill_row:
                skills[skill_row['identifier']] = Skill(
                    skill_row['name'],
                    skill_row['description'] if 'description' in skill_row else '[no description]'
                )
        return Skills(skills)

