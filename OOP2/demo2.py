class A:
    def __init__(self):
        print("== Init A ==")
        self.a = 18
        self.c = 27

    def method(self):
        print("A class: method call")


class B:

    def __init__(self):
        print("== Init B ==")
        self.b = 87

    def method(self):
        print("B: call method.")


class C(B, A):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)
        self.z = 12

    def method(self):
        super(C, self).method()
        print("C is called method.")



c = C()

print(c.a)
print(c.b)
print(c.c)
print(c.z)
c.method()