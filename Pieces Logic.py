def check_peice(x,y):
    if a[x][y] in ['⬜', '⬛']:
        print("another coordinate")
    else:
        if isinstance(a[x][y], Pawn):
            print("pawn")
        elif isinstance(a[x][y], Rook):
            print("rook")
class Pawn:
    def __init__(self, x: int, y: int, color: str, board: list):
        self.x, self.y = x, y
        self.color = color
        self.moved = False
        self.a = board
        a[self.x][self.y] = self
        #once moved can only go up in ones

    def __str__(self):
        return f'{"♟"}'
    def poss_moves(self):  # pawn
        # up 2 or 1
        # if up 2 == #enemy or 0: can do so highlight
        try:
            #if white -1
            #if black +1
            n, m = (self.x - 1), self.y
            if n < 0 or m < 0 or n > 8 or n > 8: #make sure is in grid
                raise IndexError
            if self.a[n][m] == '⬛' or self.a[n][m] == '⬜':
                self.a[n][m] = 'X'
                print(f'you can move to {n},{m}')
                if self.moved == False:
                    try:
                        n, m = (self.x - 2), self.y
                        if n < 0 or m < 0 or n > 8 or n > 8: #make sure is in grid
                            raise IndexError
                        if self.a[n][m] == '⬛' or self.a[n][m] == '⬜':
                            self.a[n][m] = 'X'
                            print(f'you can move to {n},{m}')
                    except IndexError as e:
                        print(e)
        except IndexError as e:
            print(e)
    def move(self,inpx, inpy):
        if self.a[inpx][inpy] == 'X':
            self.moved = True
            self.a[inpx][inpy] = '♟'
            self.a[self.x][self.y] = 0
            for i in range(8):
                for j in range(8):
                    if self.a[i][j] == 'X':
                        self.a[i][j] = '⬛'
        else:
            print("invalid input")

class Rook:
    def __init__(self,x:int,y:int,color:str,board:list):
        self.x, self.y = x,  y
        self.color = color
        self.a = board
        a[self.x][self.y] = self

    def __str__(self):
        return f'{"♜"}'
    def poss_moves(self):  # rook
        def right(x, y):
            if y < 0 or y > 7:  # out of index
                return
            if a[x][y] == '⬛' or a[x][y] == '⬜':
                a[x][y] = 'X'
                print(f'you can move to {x},{y}')
            return right(x, y - 1)

        right((self.x), self.y - 1)
        def left(x, y):
            if y < 0 or y > 7:  # out of index
                return
            if a[x][y] == '⬛' or a[x][y] == '⬜':
                a[x][y] = 'X'
                print(f'you can move to {x},{y}')
            return left(x, y+1)

        left((self.x), self.y+1)
        def up(x,y):
            if x < 0 or x > 7: #out of index
                return
            if a[x][y] == '⬛' or a[x][y] == '⬜':
                a[x][y] = 'X'
                print(f'you can move to {x},{y}')
            return up(x-1,y)
        up((self.x-1),self.y)
        def down(x,y):
            if x < 0 or x > 7: #out of index
                return
            if a[x][y] == '⬛' or a[x][y] == '⬜':
                a[x][y] = 'X'
                print(f'you can move to {x},{y}')
            return down(x+1,y)
        down((self.x+1),self.y)
    def move(self,inpx, inpy):
        if self.a[inpx][inpy] == 'X':
            self.moved = True
            self.a[inpx][inpy] = '♜'
            self.a[self.x][self.y] = 0
            for i in range(8):
                for j in range(8):
                    if self.a[i][j] == 'X' or self.a[i][j] == 0:
                        self.a[i][j] = '⬛'
        else:
            print("invalid input")

def board():
    x = 0
    print("  12 34 5 6 7")
    print("  01 23 45 67 y")
    for i in range(8):
        x+=1
        print(i, end=" ")
        for j in range(8):
            print(a[i][j], end="")
        print()
    print('-✖')
a = [['⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜'],
     ['⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛'],
     ['⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜'],
     ['⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛'],
     ['⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜'],
     ['⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛'],
     ['⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜'],
     ['⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛']]

# pawn0 = Pawn(6,0,'w',a)
# pawn1 = Pawn(6,1,'w',a)
# pawn2 = Pawn(6,2,'w',a)
# pawn3 = Pawn(6,3,'w',a)
# pawn4 = Pawn(6,4,'w',a)
# # pawn5 = Pawn(6,5,'w',a)
# pawn6 = Pawn(6,6,'w',a)
pawn7 = Pawn(6,7,'w',a)

# rook0 = Rook(5,6,'w',a)

board()
print()
# while True:
#     player = input("Choose a coordinate: x,y ").split(',')
#     n, m, q = int(player[0]), int(player[1]), a[n][n]
#     #perform checks for inside or outside index
#
#     if q != '⬜' and q != '⬛': # and if enemy that isn't highlighted
#         #get whats in grid location from dictionary
#         #run the moves
#         break

print("\nrook0 has been selected\n")
pawn7.poss_moves()
# pawn1.poss_moves()
board()
player = input("Choose a coordinate: x,y ").split(',')
x,y = int(player[0]),int(player[1])
board()
pawn7.move(x,y)

board()





#each piece has 3 functions:
#possible moves

#move
#ignore moves














'''
def poss_moves(currx,curry): #pawn
    #up 2 or 1
    #if up 2 == #enemy or 0: can do so highlight
    try:
        n, m = (currx - 1), curry
        if n < 0 or m < 0 or n > 8 or n > 8:
            raise IndexError
        if a[n][m] == '⬛' or a[n][m] =='⬜':
            a[n][m] = 'X'
            print(f'you can move to {n},{m}')
            try:
                n, m = (currx - 2), curry
                if n < 0 or m < 0 or n > 8 or n > 8:
                    raise IndexError
                if a[n][m] == '⬛' or a[n][m] =='⬜':
                    a[n][m] = 'X'
                    print(f'you can move to {n},{m}')
            except IndexError as e:
                print(e)
    except IndexError as e:
        print(e)
def move(inpx,inpy,currx,curry):
    if a[inpx][inpy] == 'X':
        a[inpx][inpy] = '♟'
        a[currx][curry] = 0
        for i in range(8):
            for j in range(8):
                if a[i][j] == 'X' or a[i][j] == 0:
                    a[i][j] = '⬛'
    else:
        print("invalid input")
'''
'''
class Rook:
    def __init__(self,color:str):
        self.color = color

    def spawn(self):
        #if we want to create specific boards we can spawn in each piece in its location according to name
        #not necessary
        return
    def movement(self):
        #is clicked on
        #goes through each grid box until occupied or end of board
        #^ 4 times cuz each direction
        #run ifs for color of piece that occupies box
        #[highlight those boxes] with UI
        if self.color == "w":
            print("white")
        else:
            print("black")
        print("Moves vertically and horizontally")

#warook
#w = white
#a = a on the grid (check chess board grid coordinates, a)
#rook = piece name
warook = Rook("w")
warook.movement()

class Bishop:
    def __init__(self,color:str):
        self.color = color
    def movement(self):
        # goes through each grid box until occupied or end of board
        # ^ 4 times cuz each direction
        # run ifs for color of piece that occupies box
        if self.color == "w":
            print("white")
        else:
            print("black")
        print("Moves diagonally in all directions")

bcbishop = Bishop("b")
bcbishop.movement()

class Horse:
    def __init__(self, color: str):
        self.color = color

    def movement(self):
        #moves in L shape
        if self.color == "w":
            print("white")
        else:
            print("black")
        print("Moves diagonally in all directions")

#queen and king
'''