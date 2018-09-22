from domain.attribute import Attributes
from domain.skill import Skills
from domain.errors import *


class Character:
    def __init__(self, config, resources):
        self.name = ''

        if not resources:
            self.resources = dict()
        else:
            self.resources = resources

        if 'attributes' in config:
            self.attributes = Attributes.create(config['attributes'])
        else:
            self.attributes = None

        if 'skills' in config:
            self.skills = Skills.create(config['skills'])
        else:
            self.attributes = None

        if not self.attributes and not self.skills:
            raise ConfigError('Missing skills or attributes')
