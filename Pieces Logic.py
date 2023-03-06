def check_piece(x,y):
    if a[x][y] not in ['⬜', '⬛']:
        if isinstance(a[x][y], Pawn):
            print("Pawn")
        elif isinstance(a[x][y], Rook):
            print("Rook")
        elif isinstance(a[x][y], Bishop):
            print("Bishop")
        elif isinstance(a[x][y], Queen):
            print("Queen")
        elif isinstance(a[x][y], Horse):
            print("Horse")

class Pawn:
    def __init__(self, x: int, y: int, color: str, board: list):
        self.x, self.y = x, y
        self.color = color
        self.moved = False
        self.guarding = False
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
            if n < 0 or m < 0 or n > 7 or n > 7: #make sure is in grid
                return
            if self.a[n][m] == de[n][m]:
                self.a[n][m] = 'X'
                print(f'you can move to {n},{m}')
                if self.moved == False:
                    try:
                        n, m = (self.x - 2), self.y
                        if n < 0 or m < 0 or n > 8 or n > 8: #make sure is in grid
                            raise IndexError
                        if self.a[n][m] == de[n][m]:
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
            self.a[self.x][self.y] = de[self.x][self.y]
            for i in range(8):
                for j in range(8):
                    if self.a[i][j] == 'X':
                        self.a[i][j] = de[i][j]
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
            self.a[self.x][self.y] = de[self.x][self.y]
            for i in range(8):
                for j in range(8):
                    if self.a[i][j] == 'X':
                        self.a[i][j] = de[i][j]
        else:
            print("invalid input")
class Bishop:
    def __init__(self,x:int,y:int,color:str,board:list):
        self.x, self.y = x,  y
        self.color = color
        self.a = board
        a[self.x][self.y] = self

    def __str__(self):
        return f'{"♗"}'
    def poss_moves(self):  # bishop
        def upright(x, y):
            if x < 0 or x > 7 or y < 0 or y > 7:  # out of index
                return
            if a[x][y] == '⬛' or a[x][y] == '⬜':
                a[x][y] = 'X'
                print(f'you can move to {x},{y}')
            return upright(x - 1, y + 1)
        upright(self.x - 1, self.y + 1)
        def dwnleft(x, y):
            if x < 0 or x > 7 or y < 0 or y > 7:  # out of index
                return
            if a[x][y] == '⬛' or a[x][y] == '⬜':
                a[x][y] = 'X'
                print(f'you can move to {x},{y}')
            return dwnleft(x+1, y-1)
        dwnleft(self.x+1, self.y-1)
        def upleft(x,y):
            if x < 0 or x > 7 or y < 0 or y > 7: #out of index
                return
            if a[x][y] == '⬛' or a[x][y] == '⬜':
                a[x][y] = 'X'
                print(f'you can move to {x},{y}')
            return upleft(x-1,y-1)
        upleft((self.x-1),self.y-1)
        def downright(x,y):
            if x < 0 or x > 7 or y < 0 or y > 7: #out of index
                return
            if a[x][y] == '⬛' or a[x][y] == '⬜':
                a[x][y] = 'X'
                print(f'you can move to {x},{y}')
            return downright(x+1,y+1)
        downright((self.x+1),self.y+1)
    def move(self,inpx, inpy):
        if self.a[inpx][inpy] == 'X':
            self.moved = True
            self.a[inpx][inpy] = '♗'
            self.a[self.x][self.y] = de[self.x][self.y]
            for i in range(8):
                for j in range(8):
                    if self.a[i][j] == 'X':
                        self.a[i][j] = de[i][j]
        else:
            print("invalid input")
class Queen:
    def __init__(self,x:int,y:int,color:str,board:list):
        self.x, self.y = x,  y
        self.color = color
        self.a = board
        a[self.x][self.y] = self
    def __str__(self):
        return f'{"♕"}'
    def poss_moves(self):  # Queen
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
        def upright(x, y):
            if x < 0 or x > 7 or y < 0 or y > 7:  # out of index
                return
            if a[x][y] == '⬛' or a[x][y] == '⬜':
                a[x][y] = 'X'
                print(f'you can move to {x},{y}')
            return upright(x - 1, y + 1)
        upright(self.x - 1, self.y + 1)
        def dwnleft(x, y):
            if x < 0 or x > 7 or y < 0 or y > 7:  # out of index
                return
            if a[x][y] == '⬛' or a[x][y] == '⬜':
                a[x][y] = 'X'
                print(f'you can move to {x},{y}')
            return dwnleft(x+1, y-1)
        dwnleft(self.x+1, self.y-1)
        def upleft(x,y):
            if x < 0 or x > 7 or y < 0 or y > 7: #out of index
                return
            if a[x][y] == '⬛' or a[x][y] == '⬜':
                a[x][y] = 'X'
                print(f'you can move to {x},{y}')
            return upleft(x-1,y-1)
        upleft((self.x-1),self.y-1)
        def downright(x,y):
            if x < 0 or x > 7 or y < 0 or y > 7: #out of index
                return
            if a[x][y] == '⬛' or a[x][y] == '⬜':
                a[x][y] = 'X'
                print(f'you can move to {x},{y}')
            return downright(x+1,y+1)
        downright((self.x+1),self.y+1)
    def move(self,inpx, inpy):
        if self.a[inpx][inpy] == 'X':
            self.moved = True
            self.a[inpx][inpy] = '♕'
            self.a[self.x][self.y] = de[self.x][self.y]
            for i in range(8):
                for j in range(8):
                    if self.a[i][j] == 'X':
                        self.a[i][j] = de[i][j]
        else:
            print("invalid input")
class Horse:
    def __init__(self,x:int,y:int,color:str,board:list):
        self.x, self.y = x,  y
        self.color = color
        self.a = board
        a[self.x][self.y] = self
    def __str__(self):
        return f'{"♞"}'
    def poss_moves(self):  # Horse
        try: # right up
            n, m = self.x-1, self.y+2
            if a[n][m] == de[n][m]:
                a[n][m] = 'X'
                print(f'you can move to {n},{m}')
        except Exception as e:
            print(e)
        try: # right down
            n, m = self.x+1, self.y+2
            if a[n][m] == de[n][m]:
                a[n][m] = 'X'
                print(f'you can move to {n},{m}')
        except Exception as e:
            print(e)
        try: # left down
            n, m = self.x+1, self.y-2
            if a[n][m] == de[n][m]:
                a[n][m] = 'X'
                print(f'you can move to {n},{m}')
        except Exception as e:
            print(e)
        try: #left up
            n, m = self.x-1, self.y-2
            if a[n][m] == de[n][m]:
                a[n][m] = 'X'
                print(f'you can move to {n},{m}')
        except Exception as e:
            print(e)
        try: #up right
            n, m = self.x-2, self.y-1
            if a[n][m] == de[n][m]:
                a[n][m] = 'X'
                print(f'you can move to {n},{m}')
        except Exception as e:
            print(e)
        try: #up left
            n, m = self.x-2, self.y+1
            if a[n][m] == de[n][m]:
                a[n][m] = 'X'
                print(f'you can move to {n},{m}')
        except Exception as e:
            print(e)
        try: #down right
            n, m = self.x+2, self.y-1
            if a[n][m] == de[n][m]:
                a[n][m] = 'X'
                print(f'you can move to {n},{m}')
        except Exception as e:
            print(e)
        try: #down right
            n, m = self.x+2, self.y+1
            if a[n][m] == de[n][m]:
                a[n][m] = 'X'
                print(f'you can move to {n},{m}')
        except Exception as e:
            print(e)

    def move(self,inpx, inpy):
        if self.a[inpx][inpy] == 'X':
            self.moved = True
            self.a[inpx][inpy] = '♞'
            self.a[self.x][self.y] = de[self.x][self.y]
            for i in range(8):
                for j in range(8):
                    if self.a[i][j] == 'X':
                        self.a[i][j] = de[i][j]
        else:
            print("invalid input")

def board():
    x = 0
    print("  12 34 5 6 7")
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
de = a

#test cases:
hrus = Horse(2,4,'w',a)
hrus1 = Horse(7,7,'w',a)

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



print("\nbishop has been selected\n")
hrus.poss_moves()
hrus1.poss_moves()
board()
player = input("Choose a coordinate: x,y ").split(',')
x,y = int(player[0]),int(player[1])
#Check piece func
board()
hrus.move(x,y)
hrus1.move(x,y)

board()