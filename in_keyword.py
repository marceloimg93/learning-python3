friends = ["Rolf", "Bob", "Jen"]
print("Rolf" in friends)

print(f"Check if rix string is present in Matrix word: {'rix' in 'Matrix'}")

watched_movies = {"matrix", "pink panther"}
user_movie = input("Enter some movie you watched recentlly: ").lower()

if user_movie in watched_movies:
    print("GREAT!!! I watched it too!")
else:
    print("Cool, I never watched this movie before. I'll check it out!")

secret_number = 7

wants_to_play = input(
    "Would you like to play the Guess Number game? (Press Y to Yes): ").lower()

while wants_to_play != 'n':
    user_number = int(input("Great! Guess a number: "))
    if secret_number == user_number:
        print("THAT IS AMAZING!!! YOU WON!!!")
        break
    # this could be replaced by: abs(user_number - secret_number) == 1, However the purpose of this section is to explore the IN keyword
    elif user_number - secret_number in (1, -1):
        print("WOWWW... so close!!! You missed by one number")
    else:
        print("Sorry, you did not win. =/")
    wants_to_play = input(
        "Would you like to try again? (Y/n): ").lower()
