# Доработаем задачи 5-6. Создайте класс-фабрику.
# ○ Класс принимает тип животного (название одного из созданных классов)
# и параметры для этого типа.
# ○ Внутри класса создайте экземпляр на основе переданного типа и
# верните его из класса-фабрики.
from enum import Enum
from random import randint
import random

class Animal:
    def __init__(self, name: str, color: str, size: float):
        self.name = name
        self.color = color
        self.size = size

    def show_uniq(self):
        pass

    def to_string(self):
        pass


class Fish(Animal):
    def __init__(self, name: str, color: str, size: float, max_depth: float):
        super().__init__(name, color, size)
        self.max_depth = max_depth

    def show_uniq(self):
        print(self.max_depth)

    def to_string(self):
        print(self.name, self.color, self.size, self.max_depth)


class Cat(Animal):
    def __init__(self, name: str, color: str, size: float, hairy: bool):
        super().__init__(name, color, size)
        self.hairy = hairy

    def show_uniq(self):
        print(self.hairy)

    def to_string(self):
        print(self.name, self.color, self.size, self.hairy)


class Bird(Animal):
    def __init__(self, name: str, color: str, size: float, habitat: str):
        super().__init__(name, color, size)
        self.habitat = habitat

    def show_uniq(self):
        print(self.habitat)

    def to_string(self):
        print(self.name, self.color, self.size, self.habitat)


class Type_animal(Enum):
    cat = 'Cat'
    fish = 'Fish'
    bird = 'Bird'


class Animal_factory:
    def __init__(self, type_animals: Type_animal):
        self.type_animals = type_animals

    def creat_animals(self)->object:
        names = ['Sanek', 'Alex', 'Bobik', 'Kesha']
        colors = ['black', 'white', 'green', 'blue']
        habitat = ['forest', 'desert', 'plain']
        min_size = 1
        max_size = 10
        len_nam: int = len(names)
        len_colors: int = len(colors)
        name = names[randint(0, len_nam - 1)]
        color = colors[randint(0, len_colors - 1)]
        place = habitat[randint(0,len(habitat)-1)]

        min_depth = 1
        max_depth = 15

        if self.type_animals == Cat:
            catze = Cat(name, color, randint(min_size, max_size), True)
            catze.to_string()
            return catze

        if self.type_animals == Fish:
            fish = Fish(name, color, randint(min_size, max_size),round(random.uniform(min_depth, max_depth), 2))
            fish.to_string()
            return fish

        if self.type_animals == Bird:
            bird = Bird(name, color, randint(min_size, max_size), place)
            bird.to_string()
            return bird



if __name__ == '__main__':
    value = Animal_factory(Cat)
    value.creat_animals()

    value2 = Animal_factory(Fish)
    value2.creat_animals()

    value3 = Animal_factory(Bird)
    value3.creat_animals()
