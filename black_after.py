from random import randint


def splurge(
    customer_id, customer_name, num_coffee_cups, coffee_shop_name, total_amount
):
    print(
        "{} ({}) ordered {} cups of coffee at {} for a total of ${}".format(
            customer_name,
            customer_id,
            num_coffee_cups,
            coffee_shop_name,
            total_price * randint(0, 2),
        )
    )


def another_function():
    pass


splurge(6, "Romain", "2", "Starbucks", 120)


class ARandomClass:
    pass
