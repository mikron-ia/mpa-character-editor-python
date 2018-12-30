import urwid
from domain.character import Character
from domain.state import State

footer_text = [
    ('key', '[PgUp]'), ', ', ('key', '[PgDown]'),
    ': change stage  ',
    ('key', '[arrows]'),
    ': move around  ',
    ('key', '[-]'), ': decrease/deselect  ',
    ('key', '[+]'), ': increase/select  ',
    ('key', '[Enter]'), ': choose  ',
    ('key', '[Q]'), ': exit',
]


class Screen(urwid.Frame):
    def __init__(self, configuration):
        self.character = Character.create(configuration, dict())  # todo: Parameter use, display Character data

        self.state = State(['start', 'basics',  'attributes', 'skills', 'end'])  # todo: Move to configuration

        self.head = urwid.Text(self.make_header(), 'center')  # todo: Use configuration data and add stage
        self.content = urwid.Text(self.stage_description(), align='center')  # todo: split to specific widgets
        self.foot = urwid.Text(footer_text)

        mapping = urwid.AttrMap(self.content, 'streak')

        super().__init__(
            urwid.Filler(mapping),
            urwid.AttrMap(self.head, 'head'),
            urwid.AttrMap(self.foot, 'foot')
        )

    def make_header(self):
        return 'Character Editor - MPA - ' + self.state.current()

    def stage_description(self):
        return 'Current stage: ' + self.state.current()

    def keypress(self, size, key):
        if key in ('q', 'Q'):
            raise urwid.ExitMainLoop()

        if key == 'page up':
            self.state.back()
            self.content.set_text(self.stage_description())
            self.head.set_text(self.make_header())

        if key == 'page down':
            self.state.forward()
            self.content.set_text(self.stage_description())
            self.head.set_text(self.make_header())

        return super().keypress(size, key)
