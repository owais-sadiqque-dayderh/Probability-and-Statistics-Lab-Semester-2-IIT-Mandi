import random
from matplotlib import pyplot as plt
class Experiment:
    def Trials():
        results=[]
        simulations=10000
        urn=['w','w','w','w','b','b','b','b','b','b']
        final_prob=1
        for i in range(1,simulations+1):
            choosen=random.sample(urn,5)
            p=choosen.count('w')
            results.append(p)
            prob={f"P=[X={j}]":results.count(j)/simulations for j in range(0,5)}
        print(prob)
        plt.bar(prob.keys(),prob.values(),tick_label=list(prob.keys()))
        plt.xlabel("Prob. dist. of white balls(k)")
        plt.ylabel("Prob. for respective k")
        plt.show()
        
obj=Experiment
obj.Trials()
