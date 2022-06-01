from subpackage import hello, add

from subpackage2.addons import my_foo

from demo_2 import add as my_add

print(hello("Igor"))

print(add(2, 4))
x = my_foo()

print(my_add(2,4,5,6,7))
