from TicTacToe import Game
from Assignments import assignments

game_on = True
count_turns = 0
player = 1
symbol = ""

new_game = Game()

while game_on:
    new_game.show_game()

    if count_turns % 2 == 0:
        player = 1
        symbol = "X"
    else:
        player = 2
        symbol = "O"

    field = int(input(f"\nPlayer {player}: Choose a field  "))

    if new_game.validate_entry(field):
        entry = " " + symbol + " "
        new_game.array[assignments[field][0], assignments[field][1]] = entry

        if new_game.check_win():
            print(f"\n#---------------#\n"
                  f"Player {player} has won the game!\n"
                  f"#---------------#")
            new_game.show_game()
            game_on = False

        if new_game.field_full():
            print("\n#---------------#\n"
                  "Tie!\n"
                  "#---------------#")
            new_game.show_game()
            game_on = False

        count_turns += 1

    else:
        print("\nPlease enter a valid field")

print("Hi")
