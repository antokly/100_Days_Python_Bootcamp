import json

# Python’s json module does not have a json.update() function — update() is a method for dictionaries.
# In this script, we use standard dictionary operations (like .append() for lists) to modify the loaded data, and then overwrite the file using json.dump() again.

# Sample data to be written to the JSON file
data = {
    "users": [
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"}
    ]
}

# 1. WRITE: Save the initial data to a file
with open("database.json", "w") as f:
    json.dump(data, f, indent=4)  # 'indent=4' makes it human-readable

print("Initial data written to database.json.")

# 2. READ: Load data from the JSON file
with open("database.json", "r") as f:
    loaded_data = json.load(f)

print("\nData read from file:")
print(loaded_data)

# 3. UPDATE: Add a new user to the list
new_user = {"id": 3, "name": "Charlie"}
loaded_data["users"].append(new_user)  # Update the data in memory

# Save the updated data back to the file
with open("database.json", "w") as f:
    json.dump(loaded_data, f, indent=4)

print("\nNew user added and data updated in database.json.")