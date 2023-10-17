import csv

# Define the ranges for each letter - number of pallet bays per warehouse row
ranges = {
    'A': 5,
    'B': 5,
    'C': 5,
    'D': 55,
    'E': 55,
    'F': 55,
    'G': 55,
    'H': 555,
    'I': 555
}

# Create the combinations
combinations = []

for letter, r in ranges.items():
    for i in range(1, r + 1):
        prefix = "YY" # each entry has "YY" to begin the lets
        # Change prefix to XX for the last number of each letter
        if i == r:
            prefix = "XX"
        for side in ['1L', '1R', '2L', '2R', '3L', '3R', '4L', '4R', '5L', '5R']: #Denoting 5 layers per bay, with a left and right position
            combinations.append(f"{prefix}{letter}.{i}.{side}")

# Example output is YYA.3.5L

# Write to CSV
with open('output.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for entry in combinations:
        writer.writerow([entry])

print("CSV file created successfully!")

