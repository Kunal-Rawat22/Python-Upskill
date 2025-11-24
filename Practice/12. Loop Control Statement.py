# Loop Control Statement = Statements that alter the execution flow of loops.
# Break Statement = Used to terminate the loop prematurely when a certain condition is met.
# Continue Statement = Skips the current iteration and moves to the next iteration of the loop.
# Pass Statement = Does nothing, acts as placeholder; A null operation; it is used when a statement is syntactically required but no action is needed.

# Example of Break Statement
print("Example of Break Statement:")
for i in range(1, 11):
    if i == 6:
        print("Breaking the loop at i =", i)
        break
    print("Current value of i:", i)

# Example of Continue Statement
print("\nExample of Continue Statement:")
for i in range(1, 11):
    if i % 2 == 0:
        print("Skipping even number i =", i)
        continue
    print("Current odd value of i:", i)

# Example of Pass Statement
print("\nExample of Pass Statement:")
for i in range(1, 6):
    if i == 3:
        print("Passing at i =", i)
        pass  # No action taken here
    print("Current value of i:", i)
# Note: The pass statement is often used as a placeholder for future code.
