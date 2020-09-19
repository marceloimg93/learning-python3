print("Hello, world!")

name = input("Enter your name: ")
age = int(input("Enter your age: "))
months = age * 12
days = age * 365
hours = days * 24
seconds = hours * 60 * 60

print(f"Hi {name} \nYour age in MONTHS is: {months}")
print(f"Your age is DAYS is approximately: {days}")
print(f"Your age is HOURS is: {hours}")
print(f"Your age is SECONDS is: {seconds}")
