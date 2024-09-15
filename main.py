# my custom version of rock-paper-scissors game
# Copyright (c) 2024 Wiktor Perskawiec

"""
🔥 Fire beats 🌏 Earth and 🌊 Water

🌏 Earth beats 🌊 Water and 💨 Wind

🌊 Water beats 💨 Wind and ⚡️ Ether

💨 Wind beats ⚡️ Ether and 🔥 Fire

⚡️ Ether beats 🔥 Fire and 🌏 Earth
"""

from random import randint

player = 0
computer = 0

player_wins = 0
computer_wins = 0
draws = 0

print("""
===================
Fire, Earth, Water, Wind, Ether
Copyright (c) 2024 Wiktor Perskawiec
===================""")
print("Welcome to the Fire, Earth, Water, Wind, Ether game!")
print("Press CTRL+C to exit the game.")
while True:
    print("===================")
    print("Choose your weapon:")
    print("""
1) 🔥 - Fire
2) 🌏 - Earth
3) 🌊 - Water
4) 💨 - Wind
5) ⚡️ - Ether
        """)
    print("===================")
    player = int(input("Your choice: "))
    computer = randint(1, 5)
    
    if(player not in [1, 2, 3, 4, 5]):
        print("Invalid choice. Please choose a number between 1 and 3.")
        continue
    
    print("===================")

    print("Computer chose: ", end="")
    print("🔥 Fire" if computer == 1 else "🌏 Earth" if computer == 2 else "🌊 Water" if computer == 3 else "💨 Wind" if computer == 4 else "⚡️ Ether")

    print("You chose: ", end="")
    print("🔥 Fire" if player == 1 else "🌏 Earth" if player == 2 else "🌊 Water" if player == 3 else "💨 Wind" if player == 4 else "⚡️ Ether")

    if(player == computer):
        print("It's a draw!")
        draws += 1
    elif ((player == 1 and (computer == 2 or computer == 3)) or \
   (player == 2 and (computer == 3 or computer == 4)) or \
   (player == 3 and (computer == 4 or computer == 5)) or \
   (player == 4 and (computer == 5 or computer == 1)) or \
   (player == 5 and (computer == 1 or computer == 2))):
        print("You win!")
        player_wins += 1
    else:
        print("You lose!")
        computer_wins += 1
    
    print("===================")
    print("Player wins: ", player_wins)
    print("Computer wins: ", computer_wins)
    print("Draws: ", draws)