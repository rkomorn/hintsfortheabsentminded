from sys import argv


class Meggie:
    name: str = "Meggie"
    base_coffee_need: int = 2

    def __init__(self, time_in: int):
        self.time_in: int = time_in

    def meggulate(self):
        coffee_needed = self.base_coffee_need
        coffee_needed += max(10 - self.time_in, 0) * 0.75
        return coffee_needed


time_in: int = argv[1]
meggie = Meggie(time_in)
coffee_needed = meggie.meggulate()
coffee_needed = round(coffee_needed, 1)
print(f"{meggie.name} needs {coffee_needed} cups of coffee.")
