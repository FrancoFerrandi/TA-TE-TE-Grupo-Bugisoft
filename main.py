from funciones import *

scores = {}  # Diccionario para almacenar las puntuaciones de cada jugador
play_again = True

print_logo(logo)

# Solicitar nombres de jugadores
player_1_name = input("Enter the name of Player 1 (X): ")
player_2_name = input("Enter the name of Player 2 (O): ")

# Inicializar puntuaciones si no existen
if player_1_name not in scores:
    scores[player_1_name] = 0
if player_2_name not in scores:
    scores[player_2_name] = 0
if "Tie" not in scores:
    scores["Tie"] = 0

starting_player = player_1_name  # Comienza con el jugador 1

while play_again:
    board = [" "] * 9
    current_player = starting_player
    current_symbol = "X" if current_player == player_1_name else "O"
    game_in_progress = True

    while game_in_progress:
        print_board(board)
        position = get_position(current_player)

        if board[position] != " ":
            print("That position is already taken. Try again.")
            continue

        board[position] = current_symbol
        winner = check_winner(board)

        if winner:
            print_board(board)
            print(f"Player {current_player} ({winner}) wins!")
            scores[current_player] += 1
            game_in_progress = False

        elif board_full(board):
            print_board(board)
            print("It's a tie!")
            scores["Tie"] += 1
            game_in_progress = False

        else:
            current_player = switch_player_name(current_player, player_1_name, player_2_name)
            current_symbol = "X" if current_player == player_1_name else "O"

    starting_player = switch_player_name(starting_player, player_1_name, player_2_name)
    play_again = play_again_prompt()

save_score(scores)
print("\nFinal Score:")
print(f"{player_1_name}: {scores[player_1_name]} wins")
print(f"{player_2_name}: {scores[player_2_name]} wins")
print(f"Ties: {scores['Tie']} times")
