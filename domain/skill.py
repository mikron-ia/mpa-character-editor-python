from domain.component import Component


class Skill(Component):
    def __init__(self, name, description: list):
        super().__init__(name, description)
        self.level = 0
        self.modifiers = 0  # todo Rework it into a list or set of known modifiers
        self.minimum = 0

    def get_value(self):
        return max(self.minimum, self.level + self.modifiers)

    def __str__(self):
        return self.name + ': ' \
               + str(self.level) + ' + ' \
               + str(self.modifiers) + ' = ' \
               + str(self.get_value()) + ' (' + str(self.minimum) + ')'


class Skills:
    def __init__(self, skill_config: list):
        skills = dict()
        for skill_row in skill_config:
            if 'identifier' in skill_row and 'name' in skill_row:
                skills[skill_row['identifier']] = Skill(
                    skill_row['name'],
                    skill_row['description'] if 'description' in skill_row else '[no description]'
                )
        self.skills = skills

    def __str__(self):
        strings = 'Skill: level + modifiers = value (minimum)\n'
        for identifier, attribute in self.skills.items():
            strings += str(attribute) + '\n'
        return strings
