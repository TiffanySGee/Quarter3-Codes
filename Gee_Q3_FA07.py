# Dataset: Rows are Students, Columns are Test Scores (Math, Science, English)
# Student 0: [85, 90, 88]
# Student 1: [78, 82, 80]
# Student 2: [92, 95, 94]

scores = [
    [85, 90, 88],
    [78, 82, 80],
    [92, 95, 94]
]

print("--- Student Data Summary ---")

# Variable to keep track of the overall highest score
overall_max = 0

# Loop through each row in the 2D array
for i in range(len(scores)):
    student_scores = scores[i]
    
    # Calculate Total and Average for the row
    total = sum(student_scores)
    average = total / len(student_scores)
    
    # Check for the overall maximum
    if max(student_scores) > overall_max:
        overall_max = max(student_scores)
    
    # Print the results clearly
    print(f"Student {i+1} Scores: {student_scores}")
    print(f" > Total: {total}")
    print(f" > Average: {average:.2f}")
    print("-" * 25)

print(f"Highest Score in Class: {overall_max}")
