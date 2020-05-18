class Dog:
    def __init__(self):
        print("woof woof")

    def pee(self):
        print("I will Pee")


class Puppy(Dog):
    def __init__(self):
        print("go to the park")
        super().__init__()


p = Puppy()
