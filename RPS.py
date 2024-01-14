import random
def random_choice():
    return random.choice(['rock', 'paper', 'scissors'])
def play_game(player_choice, computer_choice):
    if (player_choice == 'rock' and computer_choice == 'scissors') or \
        (player_choice == 'scissors' and computer_choice == 'paper') or \
        (player_choice == 'paper' and computer_choice == 'rock'):
        return "Player wins!"
    elif player_choice == computer_choice:
        return "It's a tie!"
    else:
        return "Computer wins!"
player_score = 0
computer_score = 0
while player_score < 3 and computer_score < 3:
    player_choice = input("Enter your choice (rock, paper, scissors): ")
    computer_choice = random_choice()
    print(f"Player chose {player_choice}, computer chose {computer_choice}")
    result = play_game(player_choice, computer_choice)
    if "Player wins!" in result:
        player_score += 1
    elif "Computer wins!" in result:
        computer_score += 1
    print(f"Scores: Player {player_score}, Computer {computer_score}")
    print(result)