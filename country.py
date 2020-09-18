countries = []

print("Welcome to your visited countries list")
print(f"So far you have visited {len(countries)} countries.")

user_input = ""

while user_input != "Q":
    user_input = input(
        "Press Q to quit, A to add or L to list all countries: ")
    if user_input == "A":
        visited_country = input("Enter a country name: ").lower()

        if visited_country in countries:
            print("We have visited this country already")
        else:
            countries.append(visited_country)
    elif user_input == "L":
        print(f"You have visited {len(countries)} countries: ")
        for country in countries:
            print(f" ----> {country.upper()}")
