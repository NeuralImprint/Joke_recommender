import pyjokes
import random

# Available categories
available_categories = ['neutral', 'more_neutral']

print("Welcome to My Joke Simulator ")
print("Select programming joke category by number:")
print("1. Neutral")
print("2. Even More Neutral")

while True:
    # Step 1: Ask user for preference using numbers
    entry = input("\nEnter the number corresponding to the joke category you like(be sure to be neutral): ").strip()

    # Step 2: Validate input and assign category
    if entry == '1':
        user_category = 'neutral'
    elif entry == '2':
        user_category = 'more_neutral'
    else:
        print("Invalid choice selected. Defaulting to 'neutral'.")
        user_category = 'neutral'

    # Step 3: Fetch jokes based on user preference
    jokes_list = []
    for _ in range(20):  # Fetch 20 jokes
        try:
            # Fetch jokes based on the selected category
            joke = pyjokes.get_joke(language='en', category=user_category)
            jokes_list.append(joke)
        except:
            pass  # Ignore errors

    # Step 4: Recommend jokes
    print("\nHere are some jokes for you :\n")
    recommended_jokes = random.sample(jokes_list, k=min(5, len(jokes_list)))

    for idx, joke in enumerate(recommended_jokes, 1):
        print(f"{idx}. {joke}\n")

    # Step 5: Add message about jokes
    print("\nJokes these days are getting easily offensive. So none for you now")

    # Step 6: Ask if user wants more jokes
    again = input("\n Want more programming jokes? (yes/no): ").strip().lower()
    if again != 'yes':
        print("Thank you for using my Joke_simulator \n")
        print("Happiness is not something ready made. It comes from your own actions.")
        print("~Dalai Lama")
        break
