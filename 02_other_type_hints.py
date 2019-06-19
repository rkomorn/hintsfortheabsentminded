from typing import Dict, List, Tuple

good_list: List[int] = [1, 2, 3]
bad_list: List[int] = [1, 2, "3"]

good_tuple: Tuple[str, int, str] = ("1", 2, "3")
bad_tuple: Tuple[str, int, str] = (1, 2, 3)

good_wtf: Dict[str, Dict[int, List[Tuple[int, int, str]]]] = {
    "1": {
        2: [
            (3, 4, "5")
        ]
    }
}

bad_wtf: Dict[str, Dict[int, List[Tuple[int, int, str]]]] = {
    "1": {
        "2": [
            ("3", 4, 5)
        ]
    }
}

good_unpack1: int
good_unpack2: str
good_unpack1, good_unpack2 = 1, "2"

# Invalid syntax:
# bad_unpack1: int, bad_unpack2: str = 1, "2"
