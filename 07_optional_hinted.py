from typing import Optional


def my_sum(items: Optional[list] = None):
    if items is None:
        return 0
    else:
        return sum(items)


print(my_sum())
print(my_sum([1, 3, 2]))
print(my_sum("a"))
