import csv

# Define the ranges for each letter
ranges = {
    'A': 24,
    'B': 24,
    'C': 24,
    'D': 24,
    'E': 24,
    'F': 30,
    'G': 30,
    'H': 39,
    'I': 39
}

# Create the combinations
combinations = []

for letter, r in ranges.items():
    for i in range(1, r + 1):
        prefix = "FG"
        # Change prefix to RGA for the last number of each letter
        if i == r:
            prefix = "RGA"
        for side in ['1L', '1R', '2L', '2R', '3L', '3R', '4L', '4R', '5L', '5R']:
            combinations.append(f"{prefix}{letter}.{i}.{side}")

# Write to CSV
with open('output.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for entry in combinations:
        writer.writerow([entry])

print("CSV file created successfully!")

