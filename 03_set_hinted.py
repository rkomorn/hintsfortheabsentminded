from typing import Set


def get_item_lengths(items: Set[str]) -> str:
    items_lengths: list = []
    for item in items:
        items_lengths.append(len(items))

    return items_lengths


print("item lengths: " + get_item_lengths(set(["one", "two", 3])))
