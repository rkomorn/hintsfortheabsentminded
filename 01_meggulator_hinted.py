from sys import argv


class Meggie:
    name: str = "Meggie"
    base_coffee_need = 2

    def __init__(self, time_in: int):
        self.time_in: int = time_in

    def meggulate(self):
        coffee_needed = self.base_coffee_need
        coffee_needed = max(10 - self.time_in, 0) * 0.25
        return coffee_needed


meggie = Meggie(argv[1])
coffee_needed = meggie.meggulate()
print(f"{meggie.name} needs {coffee_needed} cups of coffee.")