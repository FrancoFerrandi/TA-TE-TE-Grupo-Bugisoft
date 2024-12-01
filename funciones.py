from ascii import *

def print_logo(logo: str) -> None:
    """Function to print the 'Welcome TIC-TAC-TOE' logo."""
    print(logo)

def print_board(board: list) -> None:
    """Receives the board variable (list) and prints the board."""
    for i in range(3):
        print(" ", board[i * 3], "|", board[i * 3 + 1], "|", board[i * 3 + 2])
        if i < 2:
            print(" ---+---+--- ")

def validate_integer(value: str) -> bool:
    """Validates that the received number is 1, 2, or 3."""
    if len(value) != 1:
        return False
    if value not in "123":
        return False
    return True

def switch_player_name(current_player: str, player_1_name: str, player_2_name: str) -> str:
    """Switches between player names."""
    return player_1_name if current_player == player_2_name else player_2_name

def get_position(current_player: str) -> int:
    """Asks the current player to enter the coordinates to mark a point on the board."""
    column = str(input(f"{current_player}, enter the column (1-3): "))
    while not validate_integer(column):
        print("Invalid value.")
        column = str(input(f"{current_player}, enter the column (1-3): "))
    row = str(input(f"{current_player}, enter the row (1-3): "))
    while not validate_integer(row):
        print("Invalid value.")
        row = str(input(f"{current_player}, enter the row (1-3): "))
    position = (int(row) - 1) * 3 + (int(column) - 1)
    return position

def check_winner(board: list) -> str | None:
    """Checks rows, columns, and diagonals for a win."""
    for i in range(3):
        if board[i * 3] == board[i * 3 + 1] == board[i * 3 + 2] != " ":
            return board[i * 3]
        if board[0 + i] == board[3 + i] == board[6 + i] != " ":
            return board[i]
    if board[0] == board[4] == board[8] != " ":
        return board[0]
    if board[2] == board[4] == board[6] != " ":
        return board[2]
    return None

def board_full(board: list) -> bool:
    """Checks if the board is full."""
    return " " not in board

def play_again_prompt() -> bool:
    """Asks the user if they want to play again."""
    valid_responses = ["s", "n"]
    response = input("Do you want to play again? (s/n): ").lower()
    while response not in valid_responses:
        response = input("Invalid response. Do you want to play again? (s/n): ").lower()
    return response == "s"

def save_score(scores: dict) -> None:
    """Saves the scores in a text file: 'score.txt'."""
    with open("score.txt", "w") as file:
        file.write("Final Score:\n")
        for player, score in scores.items():
            file.write(f"{player}: {score} wins\n")
from ascii import *

def print_logo(logo: str) -> None:
    """Function to print the 'Welcome TIC-TAC-TOE' logo."""
    print(logo)

def print_board(board: list) -> None:
    """Receives the board variable (list) and prints the board."""
    for i in range(3):
        print(" ", board[i * 3], "|", board[i * 3 + 1], "|", board[i * 3 + 2])
        if i < 2:
            print(" ---+---+--- ")

def validate_integer(value: str) -> bool:
    """Validates that the received number is 1, 2, or 3."""
    if len(value) != 1:
        return False
    if value not in "123":
        return False
    return True

def switch_player_name(current_player: str, player_1_name: str, player_2_name: str) -> str:
    """Switches between player names."""
    return player_1_name if current_player == player_2_name else player_2_name

def get_position(current_player: str) -> int:
    """Asks the current player to enter the coordinates to mark a point on the board."""
    column = str(input(f"{current_player}, enter the column (1-3): "))
    while not validate_integer(column):
        print("Invalid value.")
        column = str(input(f"{current_player}, enter the column (1-3): "))
    row = str(input(f"{current_player}, enter the row (1-3): "))
    while not validate_integer(row):
        print("Invalid value.")
        row = str(input(f"{current_player}, enter the row (1-3): "))
    position = (int(row) - 1) * 3 + (int(column) - 1)
    return position

def check_winner(board: list) -> str | None:
    """Checks rows, columns, and diagonals for a win."""
    for i in range(3):
        if board[i * 3] == board[i * 3 + 1] == board[i * 3 + 2] != " ":
            return board[i * 3]
        if board[0 + i] == board[3 + i] == board[6 + i] != " ":
            return board[i]
    if board[0] == board[4] == board[8] != " ":
        return board[0]
    if board[2] == board[4] == board[6] != " ":
        return board[2]
    return None

def board_full(board: list) -> bool:
    """Checks if the board is full."""
    return " " not in board

def play_again_prompt() -> bool:
    """Asks the user if they want to play again."""
    valid_responses = ["s", "n"]
    response = input("Do you want to play again? (y/n): ").lower()
    while response not in valid_responses:
        response = input("Invalid response. Do you want to play again? (s/n): ").lower()
    return response == "s"

def save_score(scores: dict) -> None:
    """
    Saves the scores in a text file: 'score.txt'.
    Appends the scores of each player after each game session.

    Parameters:
    scores (dict): Dictionary with the players' names and their respective scores.
    """
    with open("score.txt", "a") as file:  
        file.write("\nFinal Score:\n")
        for player, score in scores.items():
            file.write(f"{player}: {score} wins\n")
        file.write("--------------\n")  
