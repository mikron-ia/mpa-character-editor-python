from domain.skill import Skill


class GroupSkill(Skill):
    def __init__(self, name, description: list):
        super().__init__(name, description)
        self.__subject = ''

    @property
    def name(self):
        return super().name() + ' (' + self.subject + ')'

    @property
    def subject(self):
        return self.__subject

    @subject.setter
    def subject(self, subject):
        self.__subject = subject  # todo Devise a system to check whether the name is in use, to avoid doubles

    # todo Write create()
