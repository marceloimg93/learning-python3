print("Hello, world!")

name = input("Enter your name: ")
age = input("Enter your age: ")
age_as_number = int(age)
months = age_as_number * 12
months_as_string = str(months)

print(f"Hi {name} \nYour age in months is: {months}")
