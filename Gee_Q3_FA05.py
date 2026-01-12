names = ["Me", "Lia", "Jake"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
steps = [
    [4500, 5200, 4800, 5500, 5300],
    [4000, 4100, 3900, 4200, 4600],
    [6000, 5800, 5900, 6100, 6200]
]

day_totals = []

# Loop through each day column
for i in range(len(days)):
    # Calculate the sum for all people on that specific day
    daily_sum = sum(person[i] for person in steps)
    day_totals.append(daily_sum)
    print(f"{days[i]} Total Steps: {daily_sum}")

# Find and print the most active day
max_steps = max(day_totals)
best_day = days[day_totals.index(max_steps)]

print(f"The most active day overall was {best_day} with {max_steps} steps!")
