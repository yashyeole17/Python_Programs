

# When a subclass defines a method with the same name as a method in its superclass, it is known as method overriding.


class A:
    def show(self):
        print("Class A")

class B(A):
   # pass
    def show(self):
        print("Class B")

a2 = B()
a2.show()
