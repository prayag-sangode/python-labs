# Lab 2.0: Working with Dictionaries in Python

# Create a dictionary of student details
student = {
    "name": "Alice",
    "age": 20,
    "course": "Python"
}

# Print the entire dictionary
print("Student Dictionary:", student)

# Access individual values using keys
print("Name:", student["name"])
print("Age:", student["age"])

# Add a new key-value pair
student["email"] = "alice@example.com"
print("After adding email:", student)

# Update an existing value
student["age"] = 21
print("After updating age:", student)

# Delete a key-value pair
del student["course"]
print("After removing course:", student)

# Loop through dictionary items
print("Student details:")
for key, value in student.items():
    print(f"{key}: {value}")
