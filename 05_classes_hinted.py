from typing import Union


class Dog:
    def speak(self):
        print("Woof")


class Cow:
    def speak(self):
        print("Moo")


class Apple:
    def grow(self):
        print("I'm gettin' ripe!")


def blab(item: Union[Dog, Cow]) -> None:
    item.speak()


blab(Apple())
blab(Cow())
