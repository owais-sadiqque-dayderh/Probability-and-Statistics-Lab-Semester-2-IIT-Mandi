import random
class Assign9:
    @staticmethod
    def samples(n,N):
        
        l=[(2*i, (2*i+1)) for i in range(n)]
        l1=[]
        for _ in range(N):
            p=[k for k in range(2*n)]
            random.shuffle(p)
            p.append(p[0])
            count=0
            for j in range(2*n):
                if (p[j],p[j+1]) in l or (p[j+1], p[j]) in l:
                    count+=1
            l1.append(count)
        

        E_T = sum(l1) / N
        Var_T = sum((x - E_T)**2 for x in l1) / N

        return("E(T) and Var(T):", E_T, Var_T)

sol=Assign9()
print(sol.samples(100,500))