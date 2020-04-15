from typing import Dict, List


def process_dict(my_dict: Dict[str, List[int]]) -> None:
    for key, value in my_dict.items():
        if key.startswith("melon"):
            print(sorted(value))


process_dict({"elon": [3, 1, 2], "melon": [1, 2, "3"]})
