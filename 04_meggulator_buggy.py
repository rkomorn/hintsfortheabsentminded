from sys import argv
from typing import Dict


class LectureUpdate:
    def __init__(self, author: str, days_to_lecture: int):
        self.author: str = author
        self.days_to_lecture: int = days_to_lecture


class Meggie:
    name: str = "Meggie"
    base_coffee_need = 2

    def __init__(self, time_in: int):
        self.time_in: int = time_in

    def compute_puns(self, puns: Dict[str, str]):
        pun_factor: int = 1
        pun_cost: int = 0
        for punster, pun in puns.items():
            if punster == "Romain":
                pun_factor += 2
            pun_cost += len(punster) + pun_factor * len(pun)

        self.pun_cost = pun_cost

    def compute_lecture_updates(self, lecture_update: LectureUpdate):
        lecture_cost: float = 2 / (lecture_update.days_to_lecture + 1)
        if lecture_update.author == "Romain":
            lecture_cost += 1
        self.lecture_cost = lecture_cost

    def compute_day_of_week(self, date):
        day = date.weekday()
        if day > 5:
            return 0
        else:
            day_cost = day / 1.5
            self.day_cost = day_cost

    def meggulate(self):
        coffee_needed = self.base_coffee_need
        coffee_needed += max(10 - self.time_in, 0) * 0.25
        coffee_needed += self.pun_cost * 0.01
        coffee_needed += self.lecture_cost
        return coffee_needed


meggie = Meggie(int(argv[1]))
meggie.compute_puns(
    {
        "Henry": "Romain's puns are better percolate than never",
        "Romain": "My coffee jokes have never bean better",
        "Ashley": "Romain's coffee puns are esprecious",
    }
)
meggie.compute_lecture_updates(LectureUpdate("Romain", 2))
coffee_needed = meggie.meggulate()
coffee_needed += meggie.compute_day_of_week("06/21/2019")
coffee_needed = round(coffee_needed, 1)
print(f"{meggie.name} needs {coffee_needed} cups of coffee.")
