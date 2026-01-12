# Create the dataset
step_data = [
    [4500, 5200, 4800, 5000, 5300], # Me
    [4000, 4100, 3900, 4200, 4600], # Lia
    [6000, 5800, 5900, 6100, 6200]  # Jake
]

# Print Jake's Wednesday steps
print("Jake's steps on Wednesday:", step_data[2][2])

# Print all of my steps
print("My steps...", step_data[0])

# Update Thursday steps
print("Updating my Thursday steps to 5500.")
step_data[0][3] = 5500

# Print updated steps
print("My updated steps:", step_data[0])
