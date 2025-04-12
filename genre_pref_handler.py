# Netflix Genre Preference Handler

def handle_genre_preference(user_input):
    if user_input == "Sci-Fi":
        print("Yes - Sci-Fi is the best genre ever!")
    elif user_input == "sci-fi":
        print("Did you mean Sci-Fi?")
    else:
        print(f"{user_input}, was not found.") 

# input() for interactive testing)
user_input = input("Enter your favorite genre: ")
handle_genre_preference(user_input)
