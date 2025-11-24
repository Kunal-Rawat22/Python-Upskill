# Mutability
list1 = ["History", "Maths", "Physics", "CompSci"]
list2 = list1
print("\n\nOriginal List1:", list1)
print("Original List2 (reference to List1):", list2)

# Modifying
list2[0] = "Art"
print("\nList1 after modifying List2:", list1)  # list1 is also affected
print("List2 after modification:", list2)

# Immutability
tuple1 = ("History", "Maths", "Physics", "CompSci")
tuple2 = tuple1
# Tuples are immutable
# Only have two methods: count() and index()
print("\n\nOriginal Tuple1:", tuple1)
print("Original Tuple2 (reference to Tuple1):", tuple2)
# Attempting to modify
try:
    tuple2[0] = "Art"  # This will raise an error
except TypeError as e:
    print("\nError while modifying Tuple2:", e) 
