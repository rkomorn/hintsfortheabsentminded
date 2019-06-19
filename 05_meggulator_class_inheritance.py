from datetime import datetime
from sys import argv
from typing import Dict


class ContentUpdate:

    multiplier: float = 1

    def __init__(self, author: str, days_to_event: int) -> None:
        self.author: str = author
        self.days_to_event: int = days_to_event


class LectureUpdate(ContentUpdate):
    pass


class LabUpdate(ContentUpdate):

    multiplier = 0.5


class Meggie:
    name: str = "Meggie"
    base_coffee_need: int = 2
    total_content_cost: float = 0

    def __init__(self, time_in: int) -> None:
        self.time_in: int = time_in

    def compute_puns(self, puns: Dict[str, str]) -> None:
        pun_factor: int = 1
        pun_cost: int = 0
        for punster, pun in puns.items():
            if punster == "Romain":
                pun_factor += 2
            pun_cost += len(punster) + pun_factor * len(pun)

        self.pun_cost = pun_cost

    def compute_content_update(self, content_update: ContentUpdate) -> None:
        content_cost: float = 2 / (content_update.days_to_event + 1)
        if content_update.author == "Romain":
            content_cost += 1
        content_cost = content_cost * content_update.multiplier
        self.total_content_cost = content_cost

    def compute_day_of_week(self, date: datetime) -> float:
        day: int = date.weekday()
        if day > 5:
            return 0
        else:
            day_cost: float = day / 1.5
            return day_cost

    def meggulate(self) -> float:
        coffee_needed: float = float(self.base_coffee_need)
        coffee_needed += max(10 - self.time_in, 0) * 0.75
        coffee_needed += self.pun_cost * 0.01
        coffee_needed += self.total_content_cost
        return coffee_needed


meggie: Meggie = Meggie(int(argv[1]))
meggie.compute_puns(
    {
        "Henry": "Romain's puns are better percolate than never",
        "Romain": "My coffee jokes have never bean better",
        "Ashley": "Romain's coffee puns are esprecious",
    }
)
meggie.compute_content_update(LectureUpdate("Romain", 2))
meggie.compute_content_update(LabUpdate("Ashley", 7))
coffee_needed: float = meggie.meggulate()
coffee_needed += meggie.compute_day_of_week(datetime.today())
coffee_needed = round(coffee_needed, 1)
print(f"{meggie.name} needs {coffee_needed} cups of coffee.")
