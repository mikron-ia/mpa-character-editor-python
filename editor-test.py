# Test file until some more state-of-art tests are made

import json
from domain.character import Character


def prepare_config_file(config_file_name):
    config_file = open(config_file_name, 'r')
    contents = config_file.read()
    configuration = json.loads(contents)
    return configuration


if __name__ == "__main__":
    config = prepare_config_file('config/basic.json')
    parameters = dict()  # Parameter handling
    character = Character(config, parameters)
    print(character.attributes)
