class A: # abstract
    pass
    # def m(self):
    #     print("A m-call")
    #     raise NotImplemented


class B(A):
    pass


class C(A):
    pass
    # def m(self):
    #     print("C m-call.")


class D(B, C):
    pass


d = D()
# d.m()

print(D.__mro__)
print(D.mro())


