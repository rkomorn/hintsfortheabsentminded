from typing import Dict, List, Tuple

good_wtf: Dict[str, Dict[int, List[Tuple[int, int, str]]]] = {
    "1": {2: [(3, 4, "5")]}
}

bad_wtf: Dict[str, Dict[int, List[Tuple[int, int, str]]]] = {
    "1": {"2": [("3", 4, 5)]}
}
