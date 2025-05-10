import pyjokes as a
import random as n

k = ['neutral', 'more_neutral']

print("Welcome to My Joke Simulator ")
print("Select programming joke category by number:")
print("1. Neutral")
print("2. Even More Neutral")

while True:
    i = input("\nEnter the number corresponding to the joke category you like (be sure to be neutral): ").strip()

    if i == '1':
        t = 'neutral'
    elif i == '2':
        t = 'more_neutral'
    else:
        print("Invalid choice selected. Defaulting to 'neutral'.")
        t = 'neutral'

    try:
        j = a.get_joke(language='en', category=t)
    except:
        j = "Oops! Couldn't fetch a joke this time."

    print("\nHere's a joke for you:\n")
    print(f"{j}\n")

    print("Jokes these days are getting easily offensive. So none for you now")

    u = input("\nWant more programming jokes? (yes/no): ").strip().lower()
    if u != 'yes':
        print("Thank you for using my Joke_simulator \n")
        print("Happiness is not something ready made. It comes from your own actions.")
        print("~Dalai Lama")
        break
