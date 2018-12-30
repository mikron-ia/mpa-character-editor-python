from domain.errors import ConfigError


class State:
    possible_states = {
        'start': 'Beginning',
        'basics': 'Basic information',
        'attributes': 'Attributes',
        'attributes_create': 'Attributes at creation',
        'attributes_develop': 'Attributes at development',
        'skills': 'Skills',
        'skills_create': 'Skills at creation',
        'skills_develop': 'Skills at development',
        'abilities': 'Abilities',
        'abilities_create': 'Abilities at creation',
        'abilities_develop': 'Abilities at development',
        'powers': 'Powers',
        'powers_create': 'Powers at creation',
        'powers_develop': 'Powers at development',
        'end': 'End'
    }

    def __init__(self, allowed_states) -> None:
        illegal_states = set(allowed_states) - set(self.possible_states.keys())
        if illegal_states:
            raise ConfigError('Illegal values in screen configuration: ' + ', '.join(illegal_states))

        self.states = allowed_states
        self.state = 0

    def forward(self):
        if self.state < len(self.states) - 1:
            self.state += 1

    def back(self):
        if self.state > 0:
            self.state -= 1

    def current(self) -> str:
        return self.possible_states.get(self.states[self.state])

    def __str__(self) -> str:
        return self.current()
