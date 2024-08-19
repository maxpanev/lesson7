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


def animal_sound(animals):
    for animal in animals:
        animal.make_sound()
        print()


class Employee():
    def __init__(self, name, position):
        self.name = name
        self.position = position


class ZooKeeper(Employee):
    def feed_animal(self, animal):
        print(f"{self.name} кормит животное: {animal.name}")


class Veterinarian(Employee):
    def heal_animal(self, animal):
        print(f"{self.name} лечит животное: {animal.name}")


class Zoo():
    def __init__(self):
        self.animals = []
        self.employees = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"Добавлено животное: {animal.name}")

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"Добавлен сотрудник: {employee.name}")

    def list_animals(self):
        print("Животные в зоопарке:")
        for animal in self.animals:
            print(f"- {animal.name}, возраст: {animal.age}")

    def list_employees(self):
        print("Сотрудники зоопарка:")
        for employee in self.employees:
            print(f"- {employee.name}, должность: {employee.position}")


# Пример использования
zoo = Zoo()

bird = Bird("Гоша", 6)
mammal = Mammal("Соня", 4)
reptile = Reptile("Ранго", 7)

animal_sound([bird, mammal, reptile])



zookeeper = ZooKeeper("Иван", "Зоокипер")
veterinarian = Veterinarian("Мария", "Ветеринар")

zoo.add_animal(bird)
zoo.add_animal(mammal)
zoo.add_animal(reptile)

zoo.add_employee(zookeeper)
zoo.add_employee(veterinarian)

zoo.list_animals()
zoo.list_employees()

zookeeper.feed_animal(bird)
veterinarian.heal_animal(mammal)