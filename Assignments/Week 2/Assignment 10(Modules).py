from datetime import datetime, timedelta, date
import os

# Task 1
print("\n------------Task 1------------\n") 
orig = datetime(2020, 3, 22, 10, 0, 0)
delta = timedelta(weeks=1, hours=12)
new_dt = orig + delta
print("Original:", orig)
print("New (orig + 1 week + 12 hours):", new_dt)

# Task 2
print("\n------------Task 2------------\n") 
today = date.today()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)
print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)

# Task 3
print("\n------------Task 3------------\n") 
cwd = os.getcwd()
print("CWD:", cwd)

test_dir = os.path.join(cwd, "test")
try:
    os.mkdir(test_dir)
    print("Created folder:", test_dir)
except FileExistsError:
    print("Folder already exists:", test_dir)

print("Contents of CWD:")
for name in os.listdir(cwd):
    print(" -", name)

try:
    os.rmdir(test_dir)
    print("Removed folder:", test_dir)
except OSError as e:
    print("Could not remove folder (maybe not empty):", e)

# Task 4
print("\n------------Task 4------------\n") 
old = os.path.join(cwd, "old_name.txt")
new = os.path.join(cwd, "new_name.txt")

with open(old, "w") as f:
    f.write("temporary file\n")
print("Created", old)

os.replace(old, new)
print(f"Renamed {old} -> {new}")

os.remove(new)
print("Removed", new)

# Task 5
print("\n------------Task 5------------\n") 
example_path = os.path.join(cwd, "example.txt")
with open(example_path, "w") as f:
    f.write("example content\n")
size = os.path.getsize(example_path)
print(f"Size of {example_path}: {size} bytes")

os.remove(example_path) 

# Task 6
print("\n------------Task 6------------\n") 
s = "Feb 25 2020 4:20PM"
parsed = datetime.strptime(s, "%b %d %Y %I:%M%p")
print(parsed)

# Task 7
print("\n------------Task 7------------\n")
d = date(2025, 2, 25)
new_d = d - timedelta(days=7)
print("New date:", new_d)

# Task 8
print("\n------------Task 8------------\n")
df = date(2020, 2, 25)
print(df.strftime("%A %d %B %Y"))
