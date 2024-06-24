import random

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "user"
    else:
        return "computer"

def display_result(user_choice, computer_choice, result):
    print(f"User chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    if result == "tie":
        print("It's a tie!")
    elif result == "user":
        print("You win!")
    else:
        print("Computer wins!")

def play_again():
    while True:
        choice = input("Do you want to play again? (yes/no): ").strip().lower()
        if choice in ['yes', 'no']:
            return choice == 'yes'
        else:
            print("Invalid input, please enter 'yes' or 'no'.")

def main():
    user_score = 0
    computer_score = 0
    
    while True:
        user_choice = input("Enter your choice (rock, paper, or scissors): ").strip().lower()
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice, please choose 'rock', 'paper', or 'scissors'.")
            continue
        
        computer_choice = get_computer_choice()
        result = determine_winner(user_choice, computer_choice)
        display_result(user_choice, computer_choice, result)
        
        if result == "user":
            user_score += 1
        elif result == "computer":
            computer_score += 1
        
        print(f"Score - You: {user_score}, Computer: {computer_score}")
        
        if not play_again():
            break

    print("Thanks for playing!")

if __name__ == "__main__":
    main()
