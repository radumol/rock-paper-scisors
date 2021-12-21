import random

possible_actions = ["r", "p", "s"]
possible_actions_ext = {
  "r": "Rock",
  "p": "Paper",
  "s": "Scissors"
}

def user_input():
    user_input = input("Choose Rock, Paper or Scissors by typing the letter 'r', 'p' or 's': ")
    while (user_input not in possible_actions):
        print("Wrong input, please try again")
        user_input = input("Choose Rock, Paper or Scissors by typing the letter 'r', 'p' or 's': ")
    print("You have selected " + possible_actions_ext[user_input])
    return user_input

def computer_action():
    computer_action = random.choice(possible_actions)
    print("Computer selected " + possible_actions_ext[computer_action])
    return computer_action

def decide_result(user_action, computer_action):
    if user_action == computer_action:
        return "DRAW"
    elif user_action == "r":
        if computer_action == "s":
            return "WIN"
        else:
            return "LOSE"
    elif user_action == "p":
        if computer_action == "r":
            return "WIN"
        else:
            return "LOSE"
    elif user_action == "s":
        if computer_action == "p":
            return "WIN"
        else:
            return "LOSE"


def print_result(result):
    if result == "DRAW":
        print("Game ended in a tie!")
    elif result == "WIN":
        print("You won the game!")
    elif result == "LOSE":
        print("You lost the game!")

def run_game():
    user_move = user_input()
    computer_move = computer_action()
    game_result = decide_result(user_move, computer_move)
    print_result(game_result)


if __name__ == "__main__":
    run_game()
    print("=============")
