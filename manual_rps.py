#%%

import random

def play():
    def get_computer_choice():
        choices = ['rock', 'paper', 'scissors']
        computer_choice = random.choice(choices)
        return computer_choice

    def get_user_choice():
        user_choice = input("Enter your choice (rock/paper/scissors): ")
        if user_choice != 'rock' and user_choice != 'paper' and user_choice != 'scissors':
            print("Invalid choice. Enter again.")
            get_user_choice()
        return user_choice

    def get_winner(computer_choice, user_choice):
        if computer_choice == user_choice:
            print("It is a tie!")
        elif (computer_choice == 'rock' and user_choice == 'scissors') or \
             (computer_choice == 'paper' and user_choice == 'rock') or \
             (computer_choice == 'scissors' and user_choice == 'paper'):
            print("You lost")
        else:
            print("You won!")
    computer_choice = get_computer_choice()
    user_choice = get_user_choice()

    print("Computer chose:", computer_choice)
    print("User chose:", user_choice)

    get_winner(computer_choice, user_choice)
play()
# %%
