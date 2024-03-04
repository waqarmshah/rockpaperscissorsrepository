import random
import cv2
import numpy as np
from keras.models import load_model
import time

model = load_model('keras_model.h5')

def play():
    computer_score = 0
    user_score = 0

    while computer_score < 3 and user_score < 3:
        computer_choice = get_computer_choice()
        user_choice = countdown()

        if user_choice is None:
            print("Failed to capture a valid frame. Please try again.")
            continue

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

    if computer_score == 3:
        print("Computer wins the game!")
    else:
        print("You win the game!")

    play_again = input("Do you want to play again? (y/n): ")
    if play_again.lower() == 'y':
        play()

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def get_prediction():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Failed to open the camera.")
        return 'nothing'

    ret, frame = cap.read()
    if not ret:
        print("Failed to capture a frame from the camera.")
        cap.release()
        return 'nothing'

    img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (224, 224))
    img = np.expand_dims(img, axis=0)
    img = img / 255.0

    prediction = model.predict(img)[0]

    cap.release()

    classes = ['rock', 'paper', 'scissors', 'nothing']
    predicted_class = classes[np.argmax(prediction)]
    return predicted_class

def countdown():
    start_time = time.time()
    countdown_duration = 3

    while time.time() - start_time < countdown_duration:
        current_time = time.time()
        remaining_time = countdown_duration - (current_time - start_time)
        print(f"Countdown: {remaining_time:.1f} seconds")

        user_choice = get_prediction()
        if user_choice == 'nothing':
            print("Failed to capture a valid frame. Please try again.")
            return None

        time.sleep(0.1)

    print(f"You chose {user_choice}")
    return user_choice

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