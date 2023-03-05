class Pawn:
    def __init__(self,x:int,y:int,color:str,board:list):
        self.x, self.y = x,  y
        self.color = color
        self.moved = False
        self.a = board
        a[self.x][self.y] = '♟'
        #once moved can only go up in ones
    def poss_moves(self):  # pawn
        # up 2 or 1
        # if up 2 == #enemy or 0: can do so highlight
        try:
            #if white -1
            #if black +1
            n, m = (self.x - 1), self.y
            if n < 0 or m < 0 or n > 8 or n > 8:
                raise IndexError
            if self.a[n][m] == '⬛' or self.a[n][m] == '⬜':
                self.a[n][m] = 'X'
                print(f'you can move to {n},{m}')
                try:
                    n, m = (self.x - 2), self.y
                    if n < 0 or m < 0 or n > 8 or n > 8:
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
            self.a[inpx][inpy] = '♟'
            self.a[self.x][self.y] = 0
            for i in range(8):
                for j in range(8):
                    if self.a[i][j] == 'X' or self.a[i][j] == 0:
                        self.a[i][j] = '⬛'
        else:
            print("invalid input")


print()
a = [['⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜'],
     ['⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛'],
     ['⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜'],
     ['⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛'],
     ['⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜'],
     ['⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛'],
     ['⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜'],
     ['⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛']]

def board():
    z = ''
    x = 0
    print("  01 23 45 67 y")
    for i in range(8):
        z+= (str(x)+ ' ')
        x+=1
        for j in range(8):
            z+=(a[i][j])
        print(z)
        z=''

pawn1 = Pawn(7,0,'w',a)
pawn2 = Pawn(7,1,'w',a)
pawn3 = Pawn(7,2,'w',a)
pawn4 = Pawn(7,3,'w',a)
pawn5 = Pawn(7,4,'w',a)
pawn6 = Pawn(7,5,'w',a)
pawn7 = Pawn(7,6,'w',a)
pawn8 = Pawn(7,7,'w',a)

board()
print()


print("\npawn 1 has been selected\n")

pawn5.poss_moves()
board()

x,y = int(input("x:")),int(input("y:"))
pawn5.move(x,y)

board()



















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