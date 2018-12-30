import urwid
import sys
import json
from domain.errors import ConfigError
from interface.screen import Screen


def prepare_config_file():
    if len(sys.argv) < 2:
        raise ConfigError('Provide config file name as the first parameter.')

    config_file_name = './config/' + str(sys.argv[1]).rstrip('.json') + '.json'
    config_file = open(config_file_name, 'r')

    contents = config_file.read()
    configuration = json.loads(contents)

    if not configuration:
        raise ConfigError('File not found')

    return configuration


def main_loop():
    configuration = prepare_config_file()
    main_screen = Screen(configuration)
    loop = urwid.MainLoop(main_screen, (), handle_mouse=False)
    loop.run()


if __name__ == '__main__':
    try:
        main_loop()
    except Exception as e:
        print(str(e))
        exit()
