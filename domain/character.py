from domain.attribute import Attributes
from domain.skill import Skills
from domain.errors import *


class Character:
    def __init__(self, attributes, skills):
        self.name = ''
        self.attributes = attributes
        self.skills = skills

    @staticmethod
    def create(config, resources):
        if not resources:
            resources = dict()

        if 'attributes' in config:
            attributes = Attributes.create(config['attributes'])
        else:
            attributes = None

        if 'skills' in config:
            skills = Skills.create(config['skills'])
        else:
            skills = None

        if not attributes and not skills:
            raise ConfigError('Missing skills or attributes')

        return Character(attributes, skills)
