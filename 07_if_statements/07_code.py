# if statements
is_day = input("What today? ")

if is_day == "Monday":
    print("Have a great start of week!")
elif is_day == "Friday":
    print("Chill day!")
else:
    print("Fight!")


# if statements with "in" keyword
movies_watched = {"Avatar", "Harry potter", "Avenger end game"}
user_movie = input("Enter your movie watched: ")

if user_movie in movies_watched:
    print(f"I've watched {user_movie} too!")
else:
    print(f"I want this {user_movie}")
