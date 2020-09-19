name = "Bob"
age = 25
greeting = "Hello, {}"
with_name = greeting.format(name)

print(with_name)

longer_phrase = "Hello {}, you have {} years!"

formated = longer_phrase.format(name, age)

print(formated)
