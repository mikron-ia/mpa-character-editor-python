from domain.errors import IncorrectValue


class CostUnit:  # Experimental class, not sure whether it will stay
    unit = None  # None for the base class

    possible_values = {  # More to be added as options and complexity grow
        'P': 'Point',  # Points - the basic, generic value
        'AP': 'Attribute Point',  # Attribute Points
        'SP': 'Skill Point',  # Skill Points
        'TP': 'Trait Point',  # Trait Points
        'POW': 'Power Point',  # Power
        'DEV': 'Development',  # Development
    }

    def get_short_name(self):
        return self.unit

    def get_long_name(self):
        return self.possible_values[self.unit]

    def __str__(self):
        return self.get_long_name()

    def __eq__(self, o) -> bool:
        return type(self) == type(o) and self.unit == o.unit

    @staticmethod
    def create(unit: str):
        unit_normalized = unit.upper()
        unit_class = {
            'P': CharacterPoint(),
            'AP': CharacterPointAttribute(),
            'SP': CharacterPointSkill(),
            'TP': CharacterPointTrait(),
            'POW': CharacterPointPower(),
            'DEV': CharacterPointDevelopment(),
        }.get(unit_normalized, None)
        if unit_class is None:
            raise IncorrectValue
        else:
            return unit_class


class CharacterPoint(CostUnit):
    unit = 'P'


class CharacterPointAttribute(CostUnit):
    unit = 'AP'


class CharacterPointSkill(CostUnit):
    unit = 'SP'


class CharacterPointTrait(CostUnit):
    unit = 'TP'


class CharacterPointPower(CostUnit):
    unit = 'POW'


class CharacterPointDevelopment(CostUnit):
    unit = 'DEV'


class Cost:
    def __init__(self, chosen: str, unit: CostUnit, limit: int = 10, multiplier: int = 1, start: int = 1):
        self.of_level = Cost.apply_multiplier({
                                                  'constant': Cost.generate_progress_constant(limit, start),
                                                  'linear': Cost.generate_progress_linear(limit, start),
                                                  'quadratic': Cost.generate_progress_quadratic(limit, start),
                                                  'fibonacci': Cost.generate_progress_fibonacci(limit, start)
                                              }.get(chosen, Cost.generate_progress_linear(limit, start)), multiplier)
        self.total_level = Cost.create_cost_by_level(self.of_level)
        self.value = 0
        self.unit = unit

    def __str__(self):
        return str(self.value) + ' ' + str(self.unit)

    def __eq__(self, o) -> bool:
        return type(self) == type(o) and self.unit == o.unit and self.value == o.value

    def __coerce__(self, other):
        if type(self) != type(other) or self.unit != other.unit:
            return None
        else:
            return self, other

    @staticmethod
    def generate_progress_constant(limit: int, start: int = 1) -> list:
        return [1 for i in range(start, limit + start)]

    @staticmethod
    def generate_progress_linear(limit: int, start: int = 1) -> list:
        return [i for i in range(start, limit + start)]

    @staticmethod
    def generate_progress_quadratic(limit: int, start: int = 1) -> list:
        return [pow(i, 2) for i in range(start, limit + start)]

    @staticmethod
    def generate_progress_fibonacci(limit: int, start: int = 1) -> list:
        progress = []
        previous, current = 1, 2
        for i in range(1, limit + start):
            if i >= start:
                progress.append(previous)
            previous, current = current, previous + current
        return progress

    @staticmethod
    def create_cost_by_level(progress: list) -> list:
        cost = []
        current_value = 0
        for value in progress:
            current_value += value
            cost.append(current_value)
        return cost

    @staticmethod
    def apply_multiplier(progress: list, multiplier: int) -> list:
        return [value * multiplier for value in progress]

    @staticmethod
    def create(config: dict) -> dict:
        costs = dict()
        for key, row in config.items():
            costs[key] = Cost(
                row['progression'] if 'progression' in row else 'linear',
                CostUnit.create(row['unit']) if 'unit' in row else CostUnit.create('P'),
                int(row['limit']) if 'limit' in row else 10,
                int(row['multiplier']) if 'multiplier' in row else 1,
                int(row['start']) if 'start' in row else 1
            )
        return costs


class CompleteCost:
    def __init__(self, allowed_costs_at_creation: dict, allowed_costs_at_development: dict) -> None:
        super().__init__()