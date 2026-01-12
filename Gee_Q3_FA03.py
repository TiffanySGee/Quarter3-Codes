names = ["Me", "Lia", "Jake"]
step_data = [
    [4500, 5200, 4800, 5500, 5300],
    [4000, 4100, 3900, 4200, 4600],
    [6000, 5800, 5900, 6100, 6200]
]

# Using zip lets us loop through names and steps at the same time
for name, steps in zip(names, step_data):
    total = sum(steps)
    average = total / len(steps)
    low = min(steps)
    high = max(steps)
    
    print(f"{name} - Total Steps: {total} | Average: {average} | Min: {low} | Max: {high}")
