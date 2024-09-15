# classic version of rock-paper-scissors game
# Copyright (c) 2024 Wiktor Perskawiec

from random import randint

player = 0
computer = 0

player_wins = 0
computer_wins = 0
draws = 0

print("""
===================
Rock Paper Scissors
Copyright (c) 2024 Wiktor Perskawiec
===================""")
print("Welcome to the Rock-Paper-Scissors game!")
print("Press CTRL+C to exit the game.")
while True:
    print("===================")
    print("Choose your weapon:")
    print("""
1) ✊ - Rock
2) ✋ - Paper
3) ✌️ - Scissors
        """)
    print("===================")
    player = int(input("Your choice: "))
    computer = randint(1, 3)
    
    if(player not in [1, 2, 3]):
        print("Invalid choice. Please choose a number between 1 and 3.")
        continue
    
    print("===================")

    print("Computer chose: ", end="")
    print("✊ Rock" if computer == 1 else "✋ Paper" if computer == 2 else "✌️ Scissors")

    print("You chose: ", end="")
    print("✊ Rock" if player == 1 else "✋ Paper" if player == 2 else "✌️ Scissors")

    if(player == computer):
        print("It's a draw!")
        draws += 1
    elif((player == 1 and computer == 3) or \
   (player == 2 and computer == 1) or \
   (player == 3 and computer == 2) or \
   (player == 4 and computer == 5) or \
   (player == 5 and computer == 4)):
        print("You win!")
        player_wins += 1
    else:
        print("You lose!")
        computer_wins += 1
    
    print("===================")
    print("Player wins: ", player_wins)
    print("Computer wins: ", computer_wins)
    print("Draws: ", draws)