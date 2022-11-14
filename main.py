import tictactoe

def main():
    game = tictactoe.Gameboard()
    while game.game_active:
        print(game.board)
        player_choice = input("Please choose a space to place your symbol: ").lower()
        game.place_symbol(player_choice)
        game_complete = game.check_win()
        if game_complete != None:
            print(game.board)
            game.game_active = False

if __name__ == "__main__":
    main()