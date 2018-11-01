#You can use this program to get relevant help for your programming projects.

board = [[' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ']]

#displays the game board
def display(board):
        for i in range(6):
                print("+-"*7 +"+")
                temp = ["|"+board[i][x] for x in range(7)]
                print(''.join(temp)+"|")
        print("+-"*7+"+")
        col_info = ""
        for i in range(7):
                col_info+= "|{}".format(i)
        print(col_info+"|")
        print("+-"*7+"+")
                
        
        
#checks the game for winnner after every move
def check(b):
        for i in range(6):
                for j in range(7):

                        p = [i,j]
                        if  j + 3 <= 6:
                            if b[i][j] == b[i][j+1] == b[i][j+2] == b[i][j+3] != ' ':
                                return True
                        if i +3 <= 5:
                            if b[i][j] == b[i+1][j] == b[i+2][j] == b[i+3][j] != ' ':
                                return True
                        if i -3 >=0 and j + 3 <= 6:
                            if b[i][j] == b[i-1][j+1] == b[i-2][j+2] == b[i-3][j+3] != ' ':
                                return True
                        if i -3 >=0 and j - 3 >= 0:
                                if b[i][j] == b[i-1][j-1] == b[i-2][j-2] == b[i-3][j-3] != ' ':
                                        return True
                                
        return False

print("Welcome to Connect four game")
print("Player wins a game, when he/she makes 4 consecutive matches either horizontally , vertically or diagnolly")
print("Enter the column number to make move")

win = False
i = 0
display(board)
while win == False:

        if i%2 == 0:
                choice = int(input("player 1 turn, enter column: "))
                arr = [ board[x][choice] for x in range(6)]
                arr.reverse()
                row = arr.index(' ')
                board[5-row][choice] = 'x'

        if i%2 != 0:
                choice = int(input("player 2 turn, enter column: "))
                arr = [ board[x][choice] for x in range(6)]
                arr.reverse()
                row = arr.index(' ')
                board[5-row][choice] = 'o'

        if check(board) == True :
                win = True
                if i%2 == 0:
                        print("player 1 WON the game")
                else:
                        print("player 2 WON the game")
        i+=1
        display(board)

#programmer: syed hissaan (NUST)
#project_group: haish
        

                             
        

    

