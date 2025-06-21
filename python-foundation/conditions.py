# Using if, elif, and else to check age category

# Take age as input from the user and convert to integer
age = int(input("Enter your age: "))

# Apply conditional logic
if age < 13:
    print("You are a child.")
elif age < 20:
    print("You are a teenager.")
elif age < 60:
    print("You are an adult.")
else:
    print("You are a senior citizen.")
