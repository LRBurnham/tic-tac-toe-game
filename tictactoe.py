class Gameboard:
    """Creates a board in the console to play Tic-Tac-Toe, coordinates mapped with a simple dictionary."""
    def __init__(self):
        self.game_active = True
        self.map = {
            "a1": " ", "a2": " ", "a3": " ",
            "b1": " ", "b2": " ", "b3": " ",
            "c1": " ", "c2": " ", "c3": " ",
        }
        self.active_player = "X"
        self.update_board()

    def update_board(self):
        """Creates/Updates the gameboard according to user inputs to place X's and O's using the map dictionary"""
        self.board = f"""
        It's Player {self.active_player}'s turn
           1   2   3
        a  {self.map['a1']} | {self.map['a2']} | {self.map['a3']} 
          -----------
        b  {self.map['b1']} | {self.map['b2']} | {self.map['b3']} 
          -----------
        c  {self.map['c1']} | {self.map['c2']} | {self.map['c3']} 
        """
    
    def check_win(self):
        """Checks board state to see if any sequence of 3 of the same symbol, or if the game is a draw"""
        # Win condition if statements
        if self.map['a1'] != " ":
            if self.map['a1'] == self.map['a2'] and self.map['a2'] == self.map['a3']:
                return print(f"\nPlayer {self.map['a1']} is the winner!\n"), False
            elif self.map['a1'] == self.map['b1'] and self.map['b1'] == self.map['c1']:
                return print(f"\nPlayer {self.map['a1']} is the winner!\n"), False
            elif self.map['a1'] == self.map['b2'] and self.map['b2'] == self.map['c3']:
                return print(f"\nPlayer {self.map['a1']} is the winner!\n"), False
        if self.map['a2'] != " ":
            if self.map['a2'] == self.map['b2'] and self.map['b2'] == self.map['c2']:
                return print(f"\nPlayer {self.map['a2']} is the winner\n"), False
        if self.map['a3'] != " ":
            if self.map['a3'] == self.map['b3'] and self.map['b3'] == self.map['c3']:
                return print(f"\nPlayer {self.map['a3']} is the winner!\n"), False
            elif self.map['a3'] == self.map['b2'] and self.map['b2'] == self.map['c1']:
                return print(f"\nPlayer {self.map['a3']} is the winner!\n"), False
        if self.map['b1'] != " ":
            if self.map['b1'] == self.map['b2'] and self.map['b2'] == self.map['b3']:
                return print(f"\nPlayer {self.map['b1']} is the winner!\n"), False
        if self.map['c1'] != " ":
            if self.map['c1'] == self.map['c2'] and self.map['c2'] == self.map['c3']:
                return print(f"\nPlayer {self.map['c1']} is the winner!\n"), False
        # Draw condition
        if " " not in [value for value in self.map.values()]:
            return print(f"It's a draw!"), False
        

    def place_symbol(self, coord):
        """Places the active player's symbol on the board and updates the game"""
        try:
            if self.map[coord] == " ":
                self.map[coord] = f"{self.active_player}"
                self.swap_active_player()
                self.update_board()
            else:
                new_coord = input("That space is taken, please choose a different one: ").lower()
                self.place_symbol(new_coord)
        except KeyError:
            print("\nThat isn't a valid coordinate, try again.")

    def swap_active_player(self):
        """Changes the active player to X or O depending on currently active player"""
        if self.active_player == "X":
            self.active_player = "O"
        else:
            self.active_player = "X"
        