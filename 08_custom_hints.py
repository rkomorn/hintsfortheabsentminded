from typing import Dict, List, Tuple

MyCustomType = Dict[str, Dict[int, List[Tuple[int, int, str]]]]

good: MyCustomType = {"1": {2: [(3, 4, "5")]}}

bad: MyCustomType = {"1": {"2": [("3", 4, 5)]}}
