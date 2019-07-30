class A(object):
    def __init__(self, name):
        self.name = name
        print(f"Within constructor and {self.name}")

    def afun(self):
        print("The function")

class B(A):
    pass

print(B('Frodo').name)
