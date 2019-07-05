secret=5

guess=int(input("Choose a number (between 1 and 10): "))

if guess == secret:
    print("Well done, it's 5!")
else:
    print("Try again! It's not ",str(guess),"- choose a number between 1 and 10.")
