import math, pandas
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad
a="/home/owais-sadiqque/Downloads/simulated_data.csv"
def pdf1(x,lam=1.5,k=2):
    if x>0 and lam>0 and k>0:
        return(k / lam) * ((x / lam) ** (k - 1)) * math.exp(- (x / lam) ** k)
    return 0
def pdf2(x,lam=1.5,k=2):

    if x>0 and lam>0 and k>0:
        return(lam * k * (x ** (k - 1))) / ((1 + x ** k) ** (lam + 1))
    return 0
x=[]
pd1=[]
pd2=[]
data=pandas.read_csv(a)
main_column=data["Simulated_Data"]
for i in main_column:
    x.append(i)
x.sort()
for j in x:
    pd1.append(pdf1(j))
    pd2.append(pdf2(j))

plt.plot(x,pd1,color='orange')
plt.plot(x,pd2,color='green')
plt.hist(x, bins=7, density=True,color='blue')
plt.xlabel("x")
plt.ylabel("Density")
plt.show()
sample_mean = np.mean(x)
sample_var = np.var(x, ddof=1)
lam = 1.5
k = 2
mean_pdf1, _ = quad(lambda x: x * pdf1(x, lam, k), 0, np.inf)
second_moment_pdf1, _ = quad(lambda x: x**2 * pdf1(x, lam, k), 0, np.inf)
var_pdf1 = second_moment_pdf1 - mean_pdf1**2
print("PDF-1 Mean:      ", mean_pdf1)
print("PDF-1 Variance:  ", var_pdf1)
print("sample mean: ",sample_mean)
print("sample variance: ",sample_var)


