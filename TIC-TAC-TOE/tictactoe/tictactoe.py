import random


class TicTacToe:
    def __init__(self):
        # TODO: Set up the board to be '-'

        self.board = []
        for i in range(3):
            self.board.append(['-','-','-'])


    def print_instructions(self):
        # TODO: Print the instructions to the game
        print("Welcome to TicTacToe!\nPlayer 1 is X and Player 2 is 0\nTake turns placing your pieces - the first to 3 in a row wins!")

    def print_board(self):
        # TODO: Print the board
        row_string = ""
        for i in range(3):
            row_string += "\t" + str(i)
        print(row_string)

        for row in range(len(self.board)):
            row_string = str(row)
            for col in range(len(self.board[row])):
                row_string += "\t" + str(self.board[row][col])
                #print(str(row) + "\t" + str(self.board[row][col]))
            print(row_string)


    def is_valid_move(self, row, col):
        # TODO: Check if the move is valid
        if row >= len(self.board) or col >= len(self.board[row]):
            return False
        else:
            return str(self.board[row][col]) == '-'



    def place_player(self, player, row, col):
        # TODO: Place the player on the board
        if player == 1:
            self.board[row][col] = 'X'
        elif player == 2:
            self.board[row][col] = 'O'



    def take_manual_turn(self, player):
        # TODO: Ask the user for a row, col until a valid response
        #  is given them place the player's icon in the right spot
        responseValid = False
        row = None
        column = None
        while (responseValid == False):
            row = int(input("Enter a row: "))
            column = int(input("Enter a column: "))
            if self.is_valid_move(row,column):
                responseValid = True
                break
            else:
                print("Please enter a valid move.")

        self.place_player(player,row,column)






    def take_turn(self, player):
        # TODO: Simply call the take_manual_turn function
        if player == 1:
            print("X's Turn")
        else:
            print("O's Turn")
        self.take_manual_turn(player)

    def check_col_win(self, player):
        # TODO: Check col win
        #COME BACK TO THIS
        char_needed = ""
        if player == 1:
            char_needed = "X"
        if player == 2:
            char_needed = "O"
        # chars_needed = []
        for col in range(len(self.board)):
            counter = 0
            for row in range(len(self.board[col])):
                if self.board[row][col] == char_needed:
                    counter += 1
            if counter == 3:
                return True

        return False



    def check_row_win(self, player):
        # TODO: Check row win
        char_needed = ""
        if player == 1:
            char_needed = "X"
        if player == 2:
            char_needed = "O"

        for row in range(len(self.board)):
            if (len([i for i in self.board[row] if i == char_needed]) == 3):
                return True
        return False


#CHECK THIS FUNC

    def check_diag_win(self, player):
        # TODO: Check diagonal win
        if player == 1:
            char_needed = "X"
        if player == 2:
            char_needed = "O"

        diag_backward = 0
        diag_forward = 0
        board_indexing = len(self.board) - 1
        for row in range(len(self.board)):
            if self.board[row][row] == char_needed:
                diag_forward += 1
            if self.board[board_indexing - row][row] == char_needed:
                diag_backward += 1
        if diag_forward == 3 or diag_backward == 3:
            return True
        else:
            return False




    def check_win(self, player):
        # TODO: Check win
        if self.check_diag_win(player) == True or self.check_row_win(player) == True or self.check_col_win(player) == True:
            return True
        else:
            return False


    def check_tie(self):
        # TODO: Check tie
        dash_counter = 0
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                if (self.board[row][col] == '-'):
                    dash_counter += 1
        if dash_counter == 0:
            return True
        else:
            return False



    def play_game(self):
        # TODO: Play game
        player = 1
        self.print_instructions()



        while self.check_tie() == False and self.check_win(player) == False:
            self.print_board()
            self.take_turn(player)
            if self.check_tie() == True or self.check_win(player) == True:
                break

            if player == 1:
                player = 2
            elif player == 2:
                player = 1

        if self.check_tie() == True:
            print("Tie!")
        elif self.check_win(1) == True:
            print("X wins!")
        elif self.check_win(2) == True:
            print("O wins!")








