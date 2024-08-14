import time
import random
from colorama import init, Fore, Style

def blink_string(input_str, duration_seconds=0.5, blink_count=3):
    init(autoreset=True)  # Automatically reset color settings for colorama

    for i in range(blink_count):
        print(Fore.WHITE + input_str, end="\r", flush=True)  # "\r" brings you back to the beginning of the line
        time.sleep(duration_seconds)  # Wait for the duration specified
        print(' ' * len(input_str), end='\r', flush=True)
        time.sleep(duration_seconds / 3)
    print(input_str)

def blink_counter(input_str):
    init(autoreset=True)
    print(input_str, end='')

    for count in range(3, 0, -1):
        print(Fore.WHITE + " " + str(count), end="", flush=True)
        time.sleep(0.8)  # Wait for 0.8 seconds
        print(end='\b')  # Remove the printed count
        time.sleep(0.8)  # Wait for another 0.8 seconds
        
    print('\r' + ' ' * len(input_str))  # Move to the beginning of the line and print spaces

# Rock-Paper-Scissors Game
init(autoreset=True)
print(Fore.BLUE + Style.BRIGHT + "Rock-Paper-Scissors Game: \n")
options = ["ROCK", "PAPER", "SCISSORS"]
winning_combinations = [("ROCK", "SCISSORS"), ("PAPER", "ROCK"), ("SCISSORS", "PAPER")]
scoreboard = {"player 1": 0, "player 2": 0}
congratulations_emoji = "\U0001F38A\U0001F389\U0001F38A\U0001F44F\U0001F44F"
draw_emoji = "\U0001f640\U0001f640\U0001f640\U0001f640"

player1_name = input("Enter the first player's name: ").upper()
player2_name = input("Enter the second player's name: ").upper()

while True:
    limit = input("What should be the winning score? ")
    if limit.isnumeric():
        limit = int(limit)
        break
        
while scoreboard["player 1"] < limit and scoreboard["player 2"] < limit:
    
    blink_counter("Rock-Paper-Scissors selection will be made in 3 seconds:")
    
    player1_choice = options[random.randint(0, 2)]
    player2_choice = options[random.randint(0, 2)]
    
    if (player1_choice, player2_choice) in winning_combinations:
        
        scoreboard["player 1"] += 1
        
        print(f"{player1_name}: {Fore.RED + player1_choice} <===> {player2_name}: {Fore.BLUE + player2_choice} Winner of this round: {player1_name} {congratulations_emoji}")
        print()
        blink_string(f'Score: {player1_name}: {scoreboard["player 1"]} - {player2_name}: {scoreboard["player 2"]}', 0.8, 2)
        print()
        time.sleep(1) 
    elif (player2_choice, player1_choice) in winning_combinations:
        scoreboard["player 2"] += 1
        print(f"{player1_name}: {Fore.RED + player1_choice} <===> {player2_name}: {Fore.BLUE + player2_choice} Winner of this round: {player2_name} {congratulations_emoji}")
        print()
        blink_string(f'Score: {player1_name}: {scoreboard["player 1"]} - {player2_name}: {scoreboard["player 2"]}', 0.8, 2)
        print()
        time.sleep(1) 
    else:
        print(f"{player1_name}: {Fore.CYAN + player1_choice} - {player2_name}: {Fore.CYAN + player2_choice} Draw! {draw_emoji}\n")
        
if scoreboard["player 1"] == limit:
    winner = player1_name
else:
    winner = player2_name

print(f"\033[91m \033[1m Game Over... \nThe winner is: {winner}")
