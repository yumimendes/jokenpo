# Jokenpô (Rock, Paper, Scissors) game in Python!
# Play against the computer with colorful terminal output :)

from random import choice
from time import sleep
import emoji

# Dictionary with color codes for terminal text formatting.
cor = {
    'blue': '\033[36m',
    'green': '\033[32m',
    'yellow': '\033[33m',
    'standard': '\033[m',
    'purple': '\033[35m',
    'red': '\033[31m'
}

# Possible options for the game.
options = ('rock', 'paper', 'scissors')

def play_pc():
    # Randomly selects the computer's move.

    return choice(options)

def evaluate_result(player, computer):
    # Determines the outcome of the game.
    # Returns 'draw' if tie, 'victory' if player wins, 'defeat' if player loses.

    if player == computer:
        return 'draw'
    elif player == 'rock' and computer == 'paper' or \
        player == 'paper' and computer == 'scissors' or \
        player == 'scissors' and computer == 'rock':
        return 'defeat'
    else:
        return 'victory'

def play_jokenpo():
    # Main function to run the game loop.

    # Game intro.
    print(f"{cor['blue']}*-" * 20, end="*")
    print(f"{cor['purple']}\n*-*-*-*-*- Let's play JOKENPÔ? -*-*-*-*-*")
    print(f"{cor['blue']}*-" * 20, end="*\n")
    sleep(0.5)

    while True:
        # Get player input
        player = input(f"{cor['purple']}Choose ROCK, PAPER ou SCISSORS: ").strip().lower()

        # Validate input
        if player not in options:
            print(f"{cor['red']}Invalid response, please try again!")
            continue

        # Get computer move
        computer = play_pc()

        # Countdown animation
        print(f"{cor['blue']}JO✊")
        sleep(1 / 2)
        print("KEN✋")
        sleep(1 / 2)
        print("PÔ!!✌️️")
        print("=-" * 20)

        # Determine result
        result = evaluate_result(player, computer)

        # Show result to player
        if result == 'draw':
            print(f"{cor['yellow']}IT'S A TIE!\n{cor['standard']}I also played {player.upper()}.")
        elif result == 'victory':
            print(f"{cor['green']}CONGRATS, YOU WON!\n{cor['standard']}I played {computer.upper()}.")
        else:
            print(f"{cor['red']}HÁ-HÁ, YOU LOSE!\n{cor['standard']}I played {computer.upper()}!")

        print(f"{cor['blue']}=-" * 20)
        sleep(0.5)

        # Ask to play again
        again = str(input(f"{cor['purple']}Would you like to play again? {cor['standard']}(yes/no) ").strip().lower())
        if 'no' in again or 'n' in again:
            print(f"{cor['blue']}Alrighty then! It was fun to play with you, have a nice day! 😊✌️")
            break

play_jokenpo()