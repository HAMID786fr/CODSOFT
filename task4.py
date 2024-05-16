#!/usr/bin/env python
# coding: utf-8

# In[7]:


import random

def find_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    print("Rock-Paper-Scissors Game")

    # Initialize scores
    user_score = 0
    computer_score = 0

    while True:
        # Prompt the user to choose rock, paper, or scissors
        user_choice = input("Choose rock, paper, or scissors: ").lower()

        # Generate a random choice for the computer
        choices = ["rock", "paper", "scissors"]
        computer_choice = random.choice(choices)

        print("Your choice:", user_choice)
        print("Computer's choice:", computer_choice)

        # Determine the winner
        result = find_winner(user_choice, computer_choice)
        print(result)

        # Update the scores
        if result == "You win!":
            user_score += 1
        elif result == "Computer wins!":
            computer_score += 1

        print("User Score:", user_score)
        print("Computer Score:", computer_score)

        # Ask the user if they want to play another round
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break

    print("Thank you for playing!")

if __name__ == "__main__":
    play_game()


# In[ ]:





# In[ ]:




