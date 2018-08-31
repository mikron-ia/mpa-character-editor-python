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
            self.attributes = Attributes(config['attributes'])
        else:
            raise ConfigError('Missing attribute configuration')

        if 'skills' in config:
            self.skills = Skills(config['skills'])
        else:
            raise ConfigError('Missing skill configuration')

        # @todo Traits
        # @todo Powers
        # @todo Developments
