class A:
    def __init__(self):
        print("== Init A ==")
        self.a = 18
        self.c = 27

    def method(self):
        print("A class: method call")


class B(A):

    def __init__(self):
        # A.__init__(self) # python 2
        super(B, self).__init__()
        super().__init__()
        print("== Init B ==")
        self.b = 87

    def method(self):
        print("B: call method.")


a = A()
a.method()
print(a.a)

print("=" * 100)
b = B()
b.method()
print(b.b)
print(b.a)
