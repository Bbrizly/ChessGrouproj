de = [['⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜'],
     ['⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛'],
     ['⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜'],
     ['⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛'],
     ['⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜'],
     ['⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛'],
     ['⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜'],
     ['⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛']]


def movement(x, xo, y, yo,once): #=-=-THE HOLY GRAIL-=-=  (fyi touching this function is treason)
    if x < 0 or x > 7 or y < 0 or y > 7:  # checks if out of index
        return
    if a[x][y] == de[x][y]:  # add and a[x][y] == enemy
        a[x][y] = 'X'
        print(f'you can move to {x},{y}')
        if once == True:
            return
    else:
        return
    return movement(x + xo, xo, y + yo, yo,once)
class Pieces(object):
    def __init__(self, x, y, color, board,emoji):
        self.x, self.y = x, y
        self.color = color
        self.a = board
        a[self.x][self.y] = self
        self.emoji = emoji

    def __str__(self):
        return f'{self.emoji}'

    def long_poss_moves(self):  # rook
        print("AAA")
        global x1
        global y1
        if isinstance(self,Queen) or isinstance(self, Rook) or isinstance(self, Bishop):
            if isinstance(self, Rook):
                #right 0 +1
                movement(self.x + 0, 0, self.y + 1, 1,False)
                #left 0 -1
                movement(self.x + 0, 0, self.y + -1, -1,False)
                #up -1 0
                movement(self.x + -1, -1, self.y + 0, 0,False)
                #down +1 0
                movement(self.x + 1, 1, self.y + 0, 0,False)
            if isinstance(self, Bishop):
                movement(self.x + -1, -1, self.y + 1, 1,False)
                #upright -1 +1
                movement(self.x + -1, -1, self.y + 1, 1,False)
                #dwnleft +1 -1
                movement(self.x + 1, 1, self.y + -1, -1,False)
                #upleft  -1 -1
                movement(self.x + -1, -1, self.y + -1, -1,False)
                #downright -1 +1
                movement(self.x + -1, -1, self.y + 1, 1, False)
        board()
        player = input("Choose a coordinate: x1,y1 ").split(',')
        x1, y1 = int(player[0]), int(player[1])

    #ALL THE KING NEEDS IS IN HERE
    def short_poss_moves(self):  # pawn                                         #Needs work (might jus separate em)
        global x1
        global y1
        ##### KING:
        movement(self.x + -1, -1, self.y + 1, 1, True)
        # dwnleft +1 -1
        movement(self.x + -1, -1, self.y + -1, -1, True)
        # downright -1 +1
        movement(self.x + -1, -1, self.y + 1, 1, True)
        # right 0 +1
        movement(self.x + 0, 0, self.y + 1, 1, True)
        # left 0 -1
        movement(self.x + -1, -1, self.y + 0, 0, True)
        # down +1 0
        movement(self.x + 1, 1, self.y + 0, 0, True)
        board()
        player = input("Choose a coordinate: x1,y1 ").split(',')
        x1, y1 = int(player[0]), int(player[1])

    def move(self,inpx, inpy):
        if self.a[inpx][inpy] == 'X':
            self.moved = True
            self.a[self.x][self.y] = de[self.x][self.y]     #previous location becomes empty
            a[self.x][self.y] = de[self.x][self.y]          #previous location becomes empty in main board
            self.x, self.y = inpx, inpy                     #object's new coords are inputs
            self.a[inpx][inpy] = self
            a[inpx][inpy] = self
            for i in range(8):
                for j in range(8):
                    if self.a[i][j] == 'X':                 #after movement return all Xs to normal
                        self.a[i][j] = de[i][j]
        else:
            print("invalid input")                          #Invalid input, return all Xs to normal
            for i in range(8):
                for j in range(8):
                    if self.a[i][j] == 'X':
                        self.a[i][j] = de[i][j]
def check_piece(x,y):
    if a[x][y] not in ['⬜', '⬛']:                  #Needs optimization
        if isinstance(a[x][y], Pawn):
            if a[x][y] == pawn0:
                pawn0.short_poss_moves()
                pawn0.move(x1,y1)
            elif a[x][y] == pawn1:
                pawn1.short_poss_moves()
                pawn1.move(x1,y1)
            elif a[x][y] == pawn2:
                pawn2.short_poss_moves()
                pawn2.move(x1,y1)
            elif a[x][y] == pawn3:
                pawn3.short_poss_moves()
                pawn3.move(x1,y1)
            elif a[x][y] == pawn4:
                pawn4.short_poss_moves()
                pawn4.move(x1,y1)
            elif a[x][y] == pawn5:
                pawn5.short_poss_moves()
                pawn5.move(x1,y1)
            elif a[x][y] == pawn6:
                pawn6.short_poss_moves()
                pawn6.move(x1,y1)
            elif a[x][y] == pawn7:
                pawn7.short_poss_moves()
                pawn7.move(x1,y1)
        elif isinstance(a[x][y], Rook):
            if a[x][y] == rook0:
                rook0.long_poss_moves()
                rook0.move(x1,y1)
            elif a[x][y] == rook1:
                rook1.long_poss_moves()
                rook1.move(x1,y1)
        elif isinstance(a[x][y], Bishop):
            if a[x][y] == bishop0:
                bishop0.long_poss_moves()
                bishop0.move(x1,y1)
            elif a[x][y] == bishop1:
                bishop1.long_poss_moves()
                bishop1.move(x1,y1)
        elif isinstance(a[x][y], Queen):
            if a[x][y] == queen:
                queen.long_poss_moves()
                queen.move(x1,y1)
        elif isinstance(a[x][y], Horse):
            if a[x][y] == hrus:
                hrus.poss_moves()
                hrus.move(x1,y1)
            elif a[x][y] == hrus1:
                hrus1.poss_moves()
                hrus1.move(x1,y1)
class Pawn(Pieces):
    def __init__(self, x: int, y: int, color: str, board: list,emoji):
        super().__init__(x,y,color,board,emoji)
        self.moved = False
        #once moved can only go up in ones

    def short_poss_moves(self):
        super().short_poss_moves()
        if self.moved == False:
            movement(x - 2, -2, y, 0, True)

    #pawn functions:
    # movement(self.x + 0, 0, self.y + -1, -1, True)
    # # up -1 0
    # movement(self.x + -1, -1, self.y + 1, 1, True)
    # # upright -1 +1
    # movement(self.x + 1, 1, self.y + -1, -1, True)
    # # upleft  -1 -1
    # movement(x - 2, -2, y, 0, True)
    # # double up
class Rook(Pieces):
    def __init__(self,x:int,y:int,color:str,board:list,emoji):
        super().__init__(x,y,color,board,emoji)
class Bishop(Pieces):
    def __init__(self,x:int,y:int,color:str,board:list,emoji):
        super().__init__(x, y, color, board,emoji)
class Queen(Pieces):
    def __init__(self,x:int,y:int,color:str,board:list,emoji):
        super().__init__(x, y, color, board,emoji)
class Horse(Pieces):
    def __init__(self,x:int,y:int,color:str,board:list,emoji):
        super().__init__(x, y, color, board,emoji)

    def poss_moves(self):  # Horse
        global x1
        global y1
        #upright -2 1
        movement(self.x + -2, -2, self.y + 1, 1,True)
        #up left -2 -1
        movement(self.x + -2, -2, self.y + -1, -1,True)
        #down right 2 1
        movement(self.x + 2, 2, self.y + 1, 1,True)
        #down left 2 -1
        movement(self.x + 2, 2, self.y + -1, -1,True)
        #right up -1 2
        movement(self.x + -1, -1, self.y + 2, 2,True)
        #right down 1 +1
        movement(self.x + 1, 1, self.y + 1, 1,True)
        #left up -1 -2
        movement(self.x + -1, -1, self.y + -2, -2,True)
        #left down +1 -2
        movement(self.x + 1, 1, self.y + -2, -2,True)

        board()
        player = input("Choose a coordinate: x1,y1 ").split(',')
        x1, y1 = int(player[0]), int(player[1])

def board():
    x = 0
    print("  0 12 34 5 67")
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

# test cases:
pawn0 = Pawn(5,0,'w',a, "♟")
pawn1 = Pawn(5,1,'w',a,"♟")
pawn2 = Pawn(5,2,'w',a,"♟")
pawn3 = Pawn(5,3,'w',a,"♟")
pawn4 = Pawn(5,4,'w',a,"♟")
pawn5 = Pawn(5,5,'w',a,"♟")
pawn6 = Pawn(5,6,'w',a,"♟")
pawn7 = Pawn(5,7,'w',a,"♟")

rook0 = Rook(7,0,'w',a,"♜")
rook1 = Rook(7,7,'w',a,"♜")

bishop0 = Bishop(7,1,"w",a,"♗")
bishop1 = Bishop(7,6,"w",a,"♗")

queen = Queen(7,3, "w", a,"♕")

hrus = Horse(7,2,'w',a,"♞")
hrus1 = Horse(7,5,'w',a,"♞")
board()
print()

while True:
    player = input("Choose a coordinate: x,y ").split(',')
    x,y = int(player[0]),int(player[1])
    while  0 > x or x > 7 or y > 7 or 0 > y:
        player = input("Choose a coordinate: x,y maximum 7").split(',')
        x, y = int(player[0]), int(player[1])
    #Check piece func
    check_piece(x,y)
    board()