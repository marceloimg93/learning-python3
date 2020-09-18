print("Hello, world!")

name = input("Enter your name: ")
age = input("Enter your age: ")
age_as_number = int(age)
months = age_as_number * 12
days = age_as_number * 365
hours = days * 24
seconds = hours * 60 * 60

print(f"Hi {name} \nYour age in MONTHS is: {months}")
print(f"Your age is DAYS is approximately: {days}")
print(f"Your age is HOURS is: {hours}")
print(f"Your age is SECONDS is: {seconds}")
