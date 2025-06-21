# Lab 2.2: Working with Sets in Python

# Creating sets
fruits = {"apple", "banana", "cherry", "apple"}  # 'apple' is duplicated

# Print the set
print("Fruits Set:", fruits)  # Notice no duplicates

# Add an item
fruits.add("mango")
print("After adding mango:", fruits)

# Remove an item
fruits.remove("banana")
print("After removing banana:", fruits)

# Check membership
if "cherry" in fruits:
    print("Yes, cherry is in the set")

# Set operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print("Union:", set1 | set2)
print("Intersection:", set1 & set2)
print("Difference (set1 - set2):", set1 - set2)

# Loop through set
print("All fruits:")
for fruit in fruits:
    print("-", fruit)
