class Cost:
    def __init__(self, chosen: str, limit: int, multiplier: int = 1):
        self.of_level = Cost.adjust({
            'constant': Cost.generate_progress_constant(limit),
            'linear': Cost.generate_progress_linear(limit),
            'quadratic': Cost.generate_progress_quadratic(limit),
            'fibonacci': Cost.generate_progress_fibonacci(limit)
        }.get(chosen, Cost.generate_progress_linear(limit)), multiplier)
        self.total_level = Cost.create_cost_by_level(self.of_level)

    @staticmethod
    def generate_progress_constant(limit: int) -> list:
        return [1 for i in range(1, limit + 1)]

    @staticmethod
    def generate_progress_linear(limit: int) -> list:
        return [i for i in range(1, limit + 1)]

    @staticmethod
    def generate_progress_quadratic(limit: int) -> list:
        return [pow(i, 2) for i in range(1, limit + 1)]

    @staticmethod
    def generate_progress_fibonacci(limit: int) -> list:
        progress = []
        previous,current = 1,2
        for i in range(1, limit + 1):
            progress.append(previous)
            previous,current = current,previous + current
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
    def adjust(progress: list, multiplier: int) -> list:
        return [value * multiplier for value in progress]
