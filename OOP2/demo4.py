class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def new_born(cls):
        return Person("noname", 0)

    @staticmethod
    def add(x, y):
        return x + y

    def get_info(self):
        return f"{self.name} has {self.age} years."


user = Person("Taras", 20)
print(user.get_info())

print(user.add(23, 100))

baby = Person.new_born()
print(baby.get_info())


