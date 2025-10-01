import math
import random


def f(x):
    return x**2 - 4*x + 4  

def simulated_annealing():
    
    current_x = random.uniform(-10, 10)
    current_cost = f(current_x)

    T = 100       
    T_min = 0.01  
    alpha = 0.9   

    while T > T_min:
        
        new_x = current_x + random.uniform(-1, 1)
        new_cost = f(new_x)

        
        delta = new_cost - current_cost

        
        if delta < 0 or random.random() < math.exp(-delta / T):
            current_x, current_cost = new_x, new_cost

        
        T *= alpha

    return current_x, current_cost


best_x, best_cost = simulated_annealing()
print("Best solution found: x =", best_x)
print("Function value at best x:", best_cost)
