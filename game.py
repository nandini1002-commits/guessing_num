import random
def number_guessing_game():
    # Specify the range
    lower_bound = 1
    upper_bound = 100
    
    # Generate a random number within the range
    number_to_guess = random.randint(lower_bound, upper_bound)
    
    # Initialize the number of attempts
    attempts = 0
    
    print(f"Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between {lower_bound} and {upper_bound}.")
    
    while True:
        # Ask the user for their guess
        user_guess = input("Take a guess: ")
        
        # Check if the user wants to quit
        if user_guess.lower() == "quit":
            print("Thanks for playing!")
            break
        
        # Try to convert the user's guess to an integer
        try:
            user_guess = int(user_guess)
        except ValueError:
            print("Invalid input! Please enter a whole number.")
            continue
        
        # Increment the number of attempts
        attempts += 1
        
        # Check if the user's guess is correct
        if user_guess == number_to_guess:
            print(f"Congratulations! You found the number in {attempts} attempts.")
            break
        elif user_guess < number_to_guess:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

if __name__ == "__main__":
    number_guessing_game()


