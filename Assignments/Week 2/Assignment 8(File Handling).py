# Task 1
try:
    with open("sample.txt", "r") as f:
        content = f.read()
    print("\n--- Task 1: sample.txt content ---\n")
    print(content)
except FileNotFoundError:
    print("sample.txt not found.")

# Task 2
try:
    with open("words.txt", "r") as f:
        text = f.read()
    word_count = len(text.split())
    print("\n--- Task 2: word count in words.txt ---")
    print("Word count:", word_count)
except FileNotFoundError:
    print("words.txt not found.")

# Task 3
with open("output.txt", "w") as f:
    f.write("Hello, Python!")
print("\n--- Task 3: wrote to output.txt ---")

# Task 4
import csv
data = [
    ["Name", "Roll Number", "Marks"],
    ["Alice", "101", "85"],
    ["Bob", "102", "90"],
    ["Charlie", "103", "88"]
]
with open("students.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)
print("\n--- Task 4: created students.csv ---")

# Task 5
def read_lines_generator(path):
    try:
        with open(path, "r") as f:
            for line in f:
                yield line.rstrip("\n")
    except FileNotFoundError:
        return

print("\n--- Task 5: streaming lines from large_file.txt ---")
for i, line in enumerate(read_lines_generator("large_file.txt")):
    print(line)