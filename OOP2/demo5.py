class Animal:
    def __init__(self, age):
        self.age = age

    def talk(self):
        return self.__class__.__name__ + ": "

    def info(self):
        return f"{self.__class__.__name__}({self.age})"


class Cat(Animal):

    def talk(self):
        return super().talk() + "Niav-niav"


class Dog(Animal):

    def talk(self):
        return super().talk() + "Bak-bak"


# DRY => don't repeat yourself
cat = Cat(2)
print(cat.talk())
print(cat.info())

dog = Dog(3)
print(dog.talk())
print(dog.info())
