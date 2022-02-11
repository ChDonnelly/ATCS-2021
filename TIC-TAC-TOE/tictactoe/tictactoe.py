import random

#IMPORTANT NOTE: HARD CODE THE BOARD INTO MAIN AND TEST UR FUNCTIONS!!!!!
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
            print(row_string)


    def is_valid_move(self, row, col):
        # TODO: Check if the move is valid
        if row >= len(self.board) or col >= len(self.board[row]):
            return False
        else:
            return str(self.board[row][col]) == '-'



    def place_player(self, player, row, col):
        # TODO: Place the player on the board
        self.board[row][col] = player




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

        print(str(player) + "'s turn")
        if player == 'X':
            self.take_manual_turn(player)
        else:
            self.take_random_turn(player)




    def check_col_win(self, player):
        # TODO: Check col win

        for col in range(len(self.board)):
            player_counter = 0
            for row in range(len(self.board[col])):
                if self.board[row][col] == player:
                    player_counter += 1
            if player_counter == 3:
                return True
        return False



    def check_row_win(self, player):
        # TODO: Check row win

        for row in range(len(self.board)):
            if (len([val for val in self.board[row] if val == player]) == 3):
                return True
        return False


#CHECK THIS FUNC

    def check_diag_win(self, player):
        # TODO: Check diagonal win


        diag_backward = 0
        diag_forward = 0
        board_indexing = len(self.board) - 1
        for row in range(len(self.board)):
            if self.board[row][row] == player:
                diag_forward += 1
            if self.board[board_indexing - row][row] == player:
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
        if self.check_win('O') == False and self.check_win('X') == False:
            dash_counter = 0
            for row in range(len(self.board)):
                for col in range(len(self.board[0])):
                    if (self.board[row][col] == '-'):
                        dash_counter += 1
            if dash_counter == 0:
                return True
        return False



    def take_random_turn(self,player):
        isValidTurn = False
        random_row = 0
        random_col = 0
        while (isValidTurn == False):
            random_row = random.randint(0,2)
            random_col = random.randint(0,2)
            if self.is_valid_move(random_row,random_col):
                break

        self.place_player(player,random_row,random_col)





    def play_game(self):
        # TODO: Play game
        player = 'X'
        self.print_instructions()
        self.print_board()



        while True:

            self.take_turn(player)
            self.print_board()
            if self.check_tie() == True or self.check_win(player) == True:
                break

            if player == 'O':
                player = 'X'
            elif player == 'X':
                player = 'O'

            #self.print_board()

        if self.check_tie() == True:
            print("Tie!")
        elif self.check_win('X') == True:
            print("X wins!")
        elif self.check_win('O') == True:
            print("O wins!")










