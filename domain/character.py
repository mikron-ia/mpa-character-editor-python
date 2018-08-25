from domain.attribute import Attributes
from domain.errors import *
import json


class Character:
    def __init__(self, config_file_name, resources):
        self.name = ''

        if not resources:
            self.resources = dict()
        else:
            self.resources = resources

        config = self.prepare_config_file(config_file_name)

        if 'attributes' in config:
            self.attributes = Attributes(config['attributes'])
        else:
            raise ConfigError('Missing attribute configuration')

    @staticmethod
    def prepare_config_file(config_file_name):
        config_file = open(config_file_name, 'r')
        contents = config_file.read()
        config = json.loads(contents)
        return config
