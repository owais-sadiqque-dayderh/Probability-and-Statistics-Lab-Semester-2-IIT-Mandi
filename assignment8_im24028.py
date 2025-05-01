class assign8:
        def solution(self):
            import numpy as np
            import math
            from scipy.integrate import quad
            import matplotlib.pyplot as plt
            u1=np.random.uniform(0,1,10000)
            u2=np.random.uniform(0,1,10000)
            x1=[-(1/2)*math.log(1-u) for u in u1]
            x2=[-(1/2)*math.log(1-u) for u in u2]

            print('sample mean of x1', sum(x1)/len(x1))
            print('sample mean of x2', sum(x2)/len(x2))
            m1=quad(lambda u: (-(1/2)*math.log(1-u)), 0,1)
            print("population mean is", m1)

            def marginal_cdf(data, limit):
                return np.sum(data <= limit) / len(data)

            def joint_cdf(data1, data2, limit1, limit2):
                return np.sum((data1 <= limit1) & (data2 <= limit2)) / len(data1)

            limit_x1 = np.percentile(x1, [25, 50])
            limit_x2 = np.percentile(x2, [25, 50])

            for lx1 in limit_x1:
                for lx2 in limit_x2:
                    Fx = marginal_cdf(x1, lx1)
                    Fy = marginal_cdf(x2, lx2)
                    Fxy = joint_cdf(x1, x2, lx1, lx2)
                    print(f"For limits x <= {lx1:.2f} and y <= {lx2:.2f}:")
                    print(f"  CDF X1: {Fx:.4f}")
                    print(f"  CDF X2: {Fy:.4f}")
                    print(f"  Joint CDF: {Fxy:.4f}")
                    print(f"  Product of Marginals: {Fx * Fy:.4f}")

            cov = sum((x1[i] - 0.5) * (x2[i] - 0.5) for i in range(len(x1))) / len(x1)
            std_x1 = (sum((x - 0.5)**2 for x in x1) / len(x1)) ** 0.5
            std_x2 = (sum((x - 0.5)**2 for x in x2) / len(x2)) ** 0.5
            correlation = cov / (std_x1 * std_x2)
            print(f"Correlation: {(correlation):.4f}")
            plt.figure(figsize=(8,6))
            plt.scatter(x1,x2,color='blue')
            plt.grid(True)
            plt.title('Scatter Plot')
            plt.show()



sol=assign8()
sol.solution()