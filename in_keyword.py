friends = ["Rolf", "Bob", "Jen"]
print("Rolf" in friends)

print(f"Check if rix string is present in Matrix word: {'rix' in 'Matrix'}")

watched_movies = {"matrix", "pink panther"}
user_movie = input("Enter some movie you watched recentlly: ").lower()

if user_movie in watched_movies:
    print("GREAT!!! I watched it too!")
else:
    print("Cool, I never watched this movie before. I'll check it out!")