import random

class Gifts:
    def __init__(self, n, j, trials):
        self.n = n
        self.j = j
        self.trials = trials

    def Exp(self):
        a = list(range(1, self.n + 1))
        b = list(range(1, self.j + 1))
        c = 0
        for _ in range(self.trials):
            i = random.sample(a, self.j)
            if i == b:
                c += 1
        return c / self.trials

z = Gifts(10, 4, 10000)
print(z.Exp())

        