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


# dictionary comprehensions
users = [
    (1, "Bob", "password"),
    (2, "Michael", "Secret"),
    (3, "Bacon", "shhhhh123")
]

# Easy to access a data from a user
# the alternative should be loop for each user and add if statement user[1] == <name>
username_mapping = {user[1]: user for user in users}
input_username = input("Enter your username: ")
input_password = input("Enter your password: ")

_, username, password = username_mapping[input_username]
if input_password == password:
    print("You are logged in!")
else:
    print("Ops... wrong username or password")