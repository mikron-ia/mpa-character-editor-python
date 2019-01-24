from domain.skill import Skill


class GroupSkill(Skill):
    def __init__(self, name, description: list):
        super().__init__(name, description)
        self.__subject = ''

    @property
    def name(self):
        if self.subject:
            return super().name + ' (' + self.subject + ')'
        else:
            return super().name

    @property
    def subject(self):
        return self.__subject

    @subject.setter
    def subject(self, subject):
        self.__subject = subject  # todo Devise a system to check whether the name is in use, to avoid doubles

    @staticmethod
    def create(name: str, subject: str, description: list):
        skill = GroupSkill(name, description)
        skill.subject = subject
        return skill

    @staticmethod
    def fields_optional() -> dict:
        current = super().fields_required()
        current['subject'] = 'string'
        return current
