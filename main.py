class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass

    def eat(self):
        pass


class Bird(Animal):
    def make_sound(self):
        print("Птица поет")

    def eat(self):
        print("Птица ест")


class Mammal(Animal):
    def make_sound(self):
        print("Млекопитающее говорит")


    def eat(self):
        print("Млекопитающее ест")


class Reptile(Animal):
    def make_sound(self):
        print("Рептилия шипит")


    def eat(self):
        print("Рептилия ест")


animals = [Bird("Гоша", 6), Mammal("Соня", 4), Reptile("Ранго", 7)]


def animal_sound(my_list):
    for animal in my_list:
        animal.make_sound()
        print()


animal_sound(animals)
