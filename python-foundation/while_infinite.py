# Lab 1.9C3: Demonstrating infinite loop if increment is forgotten

print("WARNING: This will run forever! Press CTRL+C to stop.")

count = 1
while count <= 5:
    print(count)
    # Missing count += 1 → Infinite loop!
