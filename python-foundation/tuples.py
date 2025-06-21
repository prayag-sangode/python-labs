# Lab 2.0: Working with Tuples in Python

# A tuple is a collection which is ordered and immutable (cannot be changed)

# Creating a tuple
fruits = ("apple", "banana", "cherry", "mango")

# Accessing elements
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# Length of the tuple
print("Total fruits:", len(fruits))

# Loop through the tuple
print("List of fruits:")
for fruit in fruits:
    print("-", fruit)

# Check if item exists
if "banana" in fruits:
    print("Yes, banana is in the tuple")

# Tuples are immutable - this will cause an error if uncommented
# fruits[1] = "orange"  # ❌ TypeError

# Tuples can contain different data types
person = ("Alice", 25, "Engineer")
print("Person info:", person)

# Tuple unpacking
name, age, profession = person
print("Unpacked Name:", name)
print("Unpacked Age:", age)
print("Unpacked Profession:", profession)
