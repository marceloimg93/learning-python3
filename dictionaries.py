friends = {"Rolf": 24, "Adam": 30, "Anne": 24}

# access key and values in for loop
for friend, age in friends.items():
    print(f"{friend}: {age}")

# check if key exists on dictionary
if "Rolf" in friends:
    print("Rolf is present")
else:
    print("Rolf is not present")

# get only the values
friends_ages = friends.values()
print(f"Sum of ages: {sum(friends_ages)}")