import random

rock = """
    _______
---'  ____)
      (_____)
      (_____)
      (____)
---.__(___)"""

paper = """
    _______
---'  ____)____
         ______)
        _______)
       _______)
---.__________)"""

scissors = """
    _______
---'  ____)____
         ______)
      __________)
      (____)
---.__(___)"""

choices = [rock, paper, scissors]
names = ["Rock", "Paper", "Scissors"]

def get_user_choice():
    while True:
        try:
            choice = int(input("Enter 0 for Rock, 1 for Paper, 2 for Scissors: "))
            if choice in [0, 1, 2]:
                return choice
            else:
                print("Invalid input. Please enter 0, 1, or 2.\n")
        except ValueError:
            print("Invalid input. Please enter a number.\n")

def get_computer_choice():
    return random.randint(0, 2)

def determine_winner(user, computer):
    if user == computer:
        return "Draw!"
    elif (user == 0 and computer == 2) or \
         (user == 1 and computer == 0) or \
         (user == 2 and computer == 1):
        return "You win!"
    else:
        return "Computer wins!"

def display_result(user, computer):
    print("\nYou chose:")
    print(choices[user])
    print(f"\nComputer chose:")
    print(choices[computer])
    print(f"\n{determine_winner(user, computer)}\n")
    print("="*40)

def main():
    print("\nRock Paper Scissors")
    print("="*40)

    wins = 0
    losses = 0
    draws = 0

    while True:
        user = get_user_choice()
        computer = get_computer_choice()
        result = determine_winner(user, computer)

        display_result(user, computer)

        if result == "You win!":
            wins += 1
        elif result == "Computer wins!":
            losses += 1
        else:
            draws += 1

        play_again = input("Play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            print("\n--- Game Over ---")
            print(f"Wins   : {wins}")
            print(f"Losses : {losses}")
            print(f"Draws  : {draws}")
            print("Thanks for playing! Goodbye!\n")
            break

main()
