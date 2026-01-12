names = ["Me", "Lia", "Jake"]
steps = [
    [4500, 5200, 4800, 5500, 5300],
    [4000, 4100, 3900, 4200, 4600],
    [6000, 5800, 5900, 6100, 6200]
]

# Calculate totals for everyone
totals = [sum(person) for person in steps]

# Find the stats
highest_total = max(totals)
lowest_total = min(totals)
difference = highest_total - lowest_total

# Find the winner
top_index = totals.index(highest_total)
top_performer = names[top_index]

# Print results
print(f"Top Performer: {top_performer} with {highest_total} steps!")
print(f"The difference between the highest and lowest total is: {difference}")
