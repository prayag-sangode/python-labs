# Lab 1.9: Working with Lists in Python

# Create a list of fruits
fruits = ["apple", "banana", "cherry", "mango"]

# Print the entire list
print("Fruits list:", fruits)

# Access elements by index
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# Add a new item
fruits.append("orange")
print("After adding orange:", fruits)

# Remove an item
fruits.remove("banana")
print("After removing banana:", fruits)

# Loop through the list
print("All fruits:")
for fruit in fruits:
    print("-", fruit)
