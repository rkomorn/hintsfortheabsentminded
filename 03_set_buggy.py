def get_item_lengths(items):
    items_lengths = []
    for item in items:
        items_lengths.append(len(item))

    return items_lengths


print("item lengths: " + get_item_lengths(set(["one", "two", 3])))
