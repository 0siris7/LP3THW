class Zelda(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def tot(self, a, b):
        print(f"Hello {self.x} I've got your sum: {a + b}")
        print(f"Goodbye {self.y}")

k = Zelda('Hammond', 'Jones')
l = k
Zelda("James", "may").tot(12, 12)
k.tot(10, 12)
