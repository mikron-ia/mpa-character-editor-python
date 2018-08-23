import urwid


def exit_on_quit(key):
    if key in ('q', 'Q', 'x', 'X'):
        raise urwid.ExitMainLoop()


if __name__ == "__main__":
    title = u" MPA Character Editor"
    txt = urwid.Text(('banner', title), align='center')
    map1 = urwid.AttrMap(txt, 'streak')
    fill = urwid.Filler(map1)
    map2 = urwid.AttrMap(fill, 'bg')
    loop = urwid.MainLoop(map2, (), unhandled_input=exit_on_quit)
    loop.run()