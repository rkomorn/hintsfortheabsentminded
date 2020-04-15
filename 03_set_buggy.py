def print_item_lengths(items):
    for item in items:
        print(f"{item}: {len(item)}")


print_item_lengths(set(["one", "two", 3]))
