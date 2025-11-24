# Match Case (Switch Case) = A control flow statement that allows a value to be tested for equality against a list of values.
# Introduced in Python 3.10
command = input("Enter a command (start, stop, pause, resume): ").lower()

match command:
    case "start":
        print("Starting...")
    case "stop":
        print("Stopping...")
    case "pause":
        print("Pausing...")
    case "resume":
        print("Resuming...")
    case _:
        print("Invalid command.")
# Note: The match-case statement is similar to switch-case statements in other programming languages.
# It provides a more readable and organized way to handle multiple conditions based on the value of a single variable.


def is_weekend(day):
    match day.lower():
        case "saturday" | "sunday":
            return True
        case "monday" | "tuesday" | "wednesday" | "thursday" | "friday":
            return False
        case _:
            return "Invalid day"
        
print(is_weekend("Saturday"))  # Output: True
print(is_weekend("Wednesday"))  # Output: False
print(is_weekend("Funday"))     # Output: Invalid day