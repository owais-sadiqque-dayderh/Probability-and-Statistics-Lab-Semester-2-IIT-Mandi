import random
import math

class DistributionSamples:
    def __init__(self):
        pass

    def binomial(self):
        l1 = []
        l2 = []
        
        for i in range(1000):
            l1.append(random.uniform(0.0, 1.0))
        
        for u in l1:
            counter = 0
            k = 0
            while counter < u:
                counter += math.comb(15, k) * ((0.25)**k) * ((0.75)**(15-k))
                k += 1
            l2.append(k - 1)
        mean_binomial = sum(l2) / len(l2)
        print("Binomial's mean", mean_binomial)
    
    def poisson(self, n):
        l3 = []
        l4 = []
        
        for i in range(n):
            l3.append(random.uniform(0.0, 1.0))
        
        for u in l3:
            counter = 0
            k = 0
            while counter < u:
                counter += (math.exp(-0.75) * (0.75**k)) / math.factorial(k)
                k += 1
            l4.append(k - 1)
        
        mean_poisson = sum(l4) / len(l4)
        print("Poisson's mean:", mean_poisson)



ds = DistributionSamples()
ds.binomial()
    
n = int(input("Enter number of samples for Poisson distribution: "))
ds.poisson(n)
