class Animal:
    def speak(self):
        print("I'm an animal")


class Dog(Animal):
    def speak(self):
        print("Woof")


class Cow(Animal):
    def speak(self):
        print("Moo")


class Apple:
    def grow(self):
        print("I'm gettin' ripe!")


def blab(item: Animal):
    item.speak()


blab(Apple())
blab(Cow())
