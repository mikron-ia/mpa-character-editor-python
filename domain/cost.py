class Cost:
    def __init__(self, chosen: str, limit: int):
        self.of_level = {
            'constant': Cost.generate_progress_constant(limit),
            'linear': Cost.generate_progress_linear(limit),
            'quadratic': Cost.generate_progress_quadratic(limit),
            'fibonacci': Cost.generate_progress_fibonacci(limit)
        }.get(chosen, Cost.generate_progress_linear(limit))
        self.total_level = Cost.create_cost_by_level(self.of_level)

    @staticmethod
    def generate_progress_constant(limit: int) -> list:
        progress = []
        for i in range(1, limit + 1):
            progress.append(1)
        return progress

    @staticmethod
    def generate_progress_linear(limit: int) -> list:
        progress = []
        for i in range(1, limit + 1):
            progress.append(i)
        return progress

    @staticmethod
    def generate_progress_quadratic(limit: int) -> list:
        progress = []
        for i in range(1, limit + 1):
            progress.append(pow(i, 2))
        return progress

    @staticmethod
    def generate_progress_fibonacci(limit: int) -> list:
        progress = []
        previous_value = 1
        current_value = 2
        for i in range(1, limit + 1):
            progress.append(previous_value)
            previous_value = current_value
            current_value += i
        return progress

    @staticmethod
    def create_cost_by_level(progress: list) -> list:
        cost = []
        current_value = 0
        for value in progress:
            current_value += value
            cost.append(current_value)
        return cost
