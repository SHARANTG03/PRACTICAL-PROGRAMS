def hill_climbing(start, max_iterations=100):
    current = start
    steps = [current]  

    for i in range(max_iterations):
        current_value = current ** 2

        
        neighbors = [current - 1, current + 1]

       
        best_neighbor = min(neighbors, key=lambda x: x ** 2)
        best_value = best_neighbor ** 2

        print(f"Step {i}: Current={current} (Cost={current_value})")

        
        if best_value < current_value:
            current = best_neighbor
            steps.append(current)
        else:
            
            break

    return current, steps


solution, path = hill_climbing(start=15)

print("\nPath Taken:", path)
print("Final Solution:", solution)
