import math
import random


def f(x):
    return x**2 - 4*x + 4


def simulated_annealing():
    
    current = random.uniform(-10, 10)
    current_cost = f(current)
    T = 100          
    T_min = 0.01     
    alpha = 0.9     

    while T > T_min:
        
        new = current + random.uniform(-1, 1)
        new_cost = f(new)

        
        delta = new_cost - current_cost

        
        if delta < 0 or random.random() < math.exp(-delta / T):
            current = new
            current_cost = new_cost

      
        T *= alpha

    return current, current_cost

best_x, best_cost = simulated_annealing()
print("Best solution x:", best_x)
print("Minimum cost:", best_cost)
