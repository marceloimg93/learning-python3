def say_hello(name, surname='Bacon'):
    print(f'Hello {surname}, {name}!')


say_hello(surname="Kevin", name="Bacon")


def add_two_numbers(x, y):
    return x + y


numbers_added = add_two_numbers(2, 3)
print(numbers_added)

# lambda functions - functions without a name, however you can name it by signing it to variables
# lambda functions should not do complicated things because it can be hard to read
# lambda functions should have only a single line of code
def double(x):
    return x * 2


sequence = [2, 4, 5, 6, 10]
doubled = [double(x) for x in sequence]
doubled = list(map(double, sequence))  # it does the same thing as the above code
doubled_lambda = list(map(lambda x: x * 2, sequence))
print(doubled)
print(doubled_lambda)
