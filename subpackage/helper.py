from subpackage.another import add
from subpackage2.addons import my_foo


def hello(name=None):
    my_foo()
    return f"Hello {name if name else 'user'}!"


if __name__ == '__main__':
    print(hello())
    print(hello("Taras"))

    print(add(3, 5))
