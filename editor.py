import urwid
import sys
import json
from domain.errors import ConfigError
from domain.character import Character
from domain.state import State

header_text = [
    ('title', 'MPA Character Editor')
]

footer_text = [
    ('key', '[PgUp]'), ', ', ('key', '[PgDown]'),
    ': change stage  ',
    ('key', '[Q]'), ': exit',
]


def exit_on_quit(key):
    if key in ('q', 'Q'):
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
    character = Character.create(configuration, dict())
    state = State(['start', 'attributes', 'skills', 'end'])  # todo: Move to configuration

    content = urwid.Text(('banner', 'Current state: ' + state.current()), align='center')
    map = urwid.AttrMap(content, 'streak')
    fill = urwid.Filler(map)

    main_screen = urwid.Frame(
        urwid.AttrMap(fill, 'body'),
        urwid.AttrMap(urwid.Text(header_text, 'center'), 'head'),
        urwid.AttrMap(urwid.Text(footer_text), 'foot')
    )

    loop = urwid.MainLoop(main_screen, (), handle_mouse=False, unhandled_input=exit_on_quit)
    loop.run()


if __name__ == '__main__':
    try:
        main_loop()
    except Exception as e:
        print(str(e))
        exit()
