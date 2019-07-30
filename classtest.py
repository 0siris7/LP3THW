class sample(object): #(object) not necessary.Used to pass arguments to self var in __init__
    """docstring for sample."""
    def __init__(self, ob1, ob2): #init not necessary either
        self.a = ob1
        self.b = ob2

    def summ(self):
        print(self.a + self.b)


k = sample(2, 3)

k.summ()
