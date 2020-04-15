from typing import Dict, List, Tuple

MyCustomType = Dict[str, Dict[int, List[Tuple[int, int, str]]]]

good_wtf: MyCustomType = {"1": {2: [(3, 4, "5")]}}

bad_wtf: MyCustomType = {"1": {"2": [("3", 4, 5)]}}
