from domain.attribute import Attributes
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

        # @todo Skills
        # @todo Traits
        # @todo Powers
        # @todo Developments
