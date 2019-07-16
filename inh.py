class A:
    def m1(self):
        return "m1 method"
    def m2(self):
        return "m2 method"

class B(A):
    def m3(self):
        return "m3 method"
    def m4(self):
        return "m4 method"

class C(A):
    def m5(self):
        return "m5 method"
    def m6(self):
        return "m6 method"

class D(B,C):
    def m7(self):
        return "m7 method"
    def m8(self):
        return "m8 method"
print(issubclass(C,A))
a = A()
print(a.m1())
print(a.m2())
b = B()
print(b.m1())
print(b.m2())
print(b.m3())
print(b.m4())
c = C()
print(c.m1())
print(c.m2())
print(c.m5())
print(c.m6())

d= D()
print(d.m1())
print(d.m2())
print(d.m3())
print(d.m4())
print(d.m5())
print(d.m6())
print(d.m7())
print(d.m8())
