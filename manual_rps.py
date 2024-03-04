import random #for random choices

#defining the function play
def play():
    computer_score = 0
    user_score = 0
#while loop to keep the game running
    while True:
        computer_choice = get_computer_choice()
        user_choice = get_user_choice()

        print("Computer chose:", computer_choice)
        print("User chose:", user_choice)

        winner = get_winner(computer_choice, user_choice)
        if winner == "computer":
            computer_score += 1
            print("You lost!")
        elif winner == "user":
            user_score += 1
            print("You won!")
        else:
            print("It is a tie!")

        print("Score: Computer", computer_score, "- User", user_score)
#asking the user if they want to play again
        play_again = input("Do you want to play again? (y/n): ")
        if play_again.lower() != 'y':
            break

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def get_user_choice():
    while True:
        user_choice = input("Enter your choice (rock/paper/scissors): ")
        if user_choice in ['rock', 'paper', 'scissors']:
            return user_choice
        print("Invalid choice. Enter again.")

def get_winner(computer_choice, user_choice):
    winning_combinations = {
        'rock': 'scissors',
        'paper': 'rock',
        'scissors': 'paper'
    }

    if computer_choice == user_choice:
        return "tie"
    elif winning_combinations[computer_choice] == user_choice:
        return "computer"
    else:
        return "user"

if __name__ == '__main__':
    play()
