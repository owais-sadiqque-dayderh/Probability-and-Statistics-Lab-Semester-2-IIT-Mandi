import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

class Assignmnet7:
    def __init__(self, lam_vals, mu_vals, x_max=10, n_samples=5000):
        self.lam_vals = lam_vals
        self.mu_vals = mu_vals
        self.x_max = x_max
        self.n_samples = n_samples
        self.results_pdf = {}
        self.results_cdf = {}
        self.generate_pdf_cdf()
        self.sample_mean, self.population_mean, self.cdf_x_bar = self.compute_means()
    
    def pdf(self, x, lam, mu):
        return 2 * lam * (x - mu) * math.exp(lam * (x - mu)**2)
    
    def cdf(self, x, lam, mu):
        return math.exp(lam * (x - mu)**2) - 1
    
    def generate_pdf_cdf(self):
        counter = 1
        for mu in self.mu_vals:
            for lam in self.lam_vals:
                key_x = f'list_{counter}_x'
                key_fx_pdf = f'list_{counter}_fx_pdf'
                key_fx_cdf = f'list_{counter}_fx_cdf'
                
                x_vals = np.arange(mu + 0.1, self.x_max, 0.03)
                pdf_vals = [self.pdf(x, lam, mu) for x in x_vals]
                cdf_vals = [self.cdf(x, lam, mu) for x in x_vals]
                
                self.results_pdf[key_x] = x_vals
                self.results_pdf[key_fx_pdf] = pdf_vals
                self.results_cdf[key_x] = x_vals
                self.results_cdf[key_fx_cdf] = cdf_vals
                
                counter += 1
    
    def plot_graphs(self, results, title, ylabel):
        n_rows = len(self.mu_vals)
        n_columns = len(self.lam_vals)
        fig, axs = plt.subplots(n_rows, n_columns, figsize=(n_columns * 4, n_rows * 3), layout='constrained')
        counter = 1
        for i in range(n_rows):
            for j in range(n_columns):
                key_x = f'list_{counter}_x'
                key_fx = f'list_{counter}_fx_{title.lower()}'
                axs[i, j].plot(results[key_x], results[key_fx])
                axs[i, j].set_title(f'{title}: {key_x}')
                axs[i, j].set_xlabel('x')
                axs[i, j].set_ylabel(ylabel)
                axs[i, j].grid(True)
                counter += 1
        plt.show()
    
    def inverse_transform(self, u, lam, mu, Z):
        return mu + math.sqrt((1/lam) * math.log(u * Z + 1))
    
    def compute_means(self):
        lam_true = 1.5
        mu_true = 0.25
        Z = math.exp(lam_true * (self.x_max - mu_true)**2) - 1
        
        u_samples = np.random.uniform(0, 1, self.n_samples)
        x_samples = np.array([self.inverse_transform(u, lam_true, mu_true, Z) for u in u_samples])
        sample_mean = np.mean(x_samples)
        
        numerator, _ = quad(lambda x: x * (2 * lam_true * (x - mu_true) * math.exp(lam_true * (x - mu_true)**2)), mu_true, self.x_max)
        population_mean = numerator / Z
        
        cdf_x_bar, _ = quad(lambda x: (2 * lam_true * (x - mu_true) * math.exp(lam_true * (x - mu_true)**2)), mu_true, population_mean)
        cdf_x_bar /= Z  
        
        return sample_mean, population_mean, cdf_x_bar

dist = Assignmnet7([1, 0.5, 5], [1, 2.5, 0.5])
dist.plot_graphs(dist.results_pdf, 'PDF', 'f(x)')
dist.plot_graphs(dist.results_cdf, 'CDF', 'P(x)')
print(dist.sample_mean, dist.population_mean, dist.cdf_x_bar)
