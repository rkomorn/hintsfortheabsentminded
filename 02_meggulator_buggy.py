from sys import argv


class Meggie:
    name: str = "Meggie"
    base_coffee_need = 2

    def __init__(self, time_in: int):
        self.time_in: int = time_in

    def compute_puns(self, puns):
        pun_factor: int = 1
        pun_cost: int = 0
        for punster, pun in puns.items():
            if punster == "Romain":
                pun_factor += "2"
            pun_cast += len(punster) + pun_factor * len(pun)

        self.pun_cost = pun_cost

    def meggulate(self):
        coffee_needed = self.base_coffee_need
        coffee_needed += max(10 - self.time_in, 0) * 0.25
        coffee_needed += self.pun_cost * 0.01
        return coffee_needed


meggie = Meggie(int(argv[1]))
meggie.compute_puns(
    {
        3: "Romain's puns are better percolate than never",
        "Romain": "My coffee jokes have never bean better",
        "Ashley": "Romain's coffee puns are esprecious",
    }
)
coffee_needed = meggie.meggulate()
coffee_needed = round(coffee_needed, 1)
coffee_needed = round(coffee_needed, 1)
print(f"{meggie.name} needs {coffee_needed} cups of coffee.")
