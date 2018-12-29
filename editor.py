import urwid
import sys
import json
from domain.errors import ConfigError
from domain.character import Character


def exit_on_quit(key):
    if key in ('q', 'Q', 'x', 'X'):
        raise urwid.ExitMainLoop()


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
    character = Character(configuration, dict())

    # todo: Config tally - how many skills, how does it look, etc.

    title = 'MPA Character Editor'
    header = urwid.Text(('banner', title), align='center')
    map1 = urwid.AttrMap(header, 'streak')
    fill = urwid.Filler(map1)
    map2 = urwid.AttrMap(fill, 'bg')
    loop = urwid.MainLoop(map2, (), unhandled_input=exit_on_quit)
    loop.run()


if __name__ == '__main__':
    try:
        main_loop()
    except Exception as e:
        print(str(e))
        exit()
