import pygame as pg

#ui
#the properties of the window
width, height = 300, 300
width_8, height_8 = int(width / 8), int(height / 8)
window = pg.display.set_mode((width, height))
pg.display.set_caption("chess")
#import the assets
knight_white1 = pg.image.load("chess images/knight white1.png")
knight_white1 = pg.transform.scale(
    knight_white1, (knight_white1.get_width() / 1.6 * width / 800,
                    knight_white1.get_height() / 1.6 * height / 800))
knight_white2 = pg.image.load("chess images/knight white2.png")
knight_white2 = pg.transform.scale(
    knight_white2, (knight_white2.get_width() / 1.6 * width / 800,
                    knight_white2.get_height() / 1.6 * height / 800))
pawn_white = pg.image.load("chess images/pawn white.png")
pawn_white = pg.transform.scale(pawn_white,
                                (pawn_white.get_width() / 1.7 * width / 800,
                                 pawn_white.get_height() / 1.7 * height / 800))
bishop_white = pg.image.load("chess images/bishop white.png")
bishop_white = pg.transform.scale(
    bishop_white, (bishop_white.get_width() / 1.7 * width / 800,
                   bishop_white.get_height() / 1.7 * height / 800))
queen_white = pg.image.load("chess images/queen white.png")
queen_white = pg.transform.scale(
    queen_white, (queen_white.get_width() / 1.7 * width / 800,
                  queen_white.get_height() / 1.7 * height / 800))
king_white = pg.image.load("chess images/king white.png")
king_white = pg.transform.scale(king_white,
                                (king_white.get_width() / 1.7 * width / 800,
                                 king_white.get_height() / 1.7 * height / 800))
rook_white = pg.image.load("chess images/rock white.png")
rook_white = pg.transform.scale(rook_white,
                                (rook_white.get_width() / 1.7 * width / 800,
                                 rook_white.get_height() / 1.7 * height / 800))

#Segregation
#pawn_black
#knight_black1
#knight_black2
#rook_black
#bishop_black
#queen_black
#king_black
knight_black1 = pg.image.load("chess images/knight white1.png")
knight_black1 = pg.transform.scale(
    knight_black1, (knight_black1.get_width() / 1.6 * width / 800,
                    knight_black1.get_height() / 1.6 * height / 800))
knight_black2 = pg.image.load("chess images/knight white2.png")
knight_black2 = pg.transform.scale(
    knight_black2, (knight_black2.get_width() / 1.6 * width / 800,
                    knight_black2.get_height() / 1.6 * height / 800))
pawn_black = pg.image.load("chess images/pawn white.png")
pawn_black = pg.transform.scale(pawn_black,
                                (pawn_black.get_width() / 1.7 * width / 800,
                                 pawn_black.get_height() / 1.7 * height / 800))
bishop_black = pg.image.load("chess images/bishop white.png")
bishop_black = pg.transform.scale(
    bishop_black, (bishop_black.get_width() / 1.7 * width / 800,
                   bishop_black.get_height() / 1.7 * height / 800))
queen_black = pg.image.load("chess images/queen white.png")
queen_black = pg.transform.scale(
    queen_black, (queen_black.get_width() / 1.7 * width / 800,
                  queen_black.get_height() / 1.7 * height / 800))
king_black = pg.image.load("chess images/king white.png")
king_black = pg.transform.scale(king_black,
                                (king_black.get_width() / 1.7 * width / 800,
                                 king_black.get_height() / 1.7 * height / 800))
rook_black = pg.image.load("chess images/rock white.png")
rook_black = pg.transform.scale(rook_black,
                                (rook_black.get_width() / 1.7 * width / 800,
                                 rook_black.get_height() / 1.7 * height / 800))



poss_places = pg.image.load("chess images/dot.png")
poss_places = pg.transform.scale(poss_places, (width_8, height_8))


def update_window():
    brown = (100, 65, 30)
    window.fill(brown)

    #draw the grid area
    for i in range(8):
        for j in range(8):
            if (i % 2 == 0 and j % 2 == 0) or (i % 2 == 1 and j % 2 == 1):
                white_box = pg.Rect(i * width_8, j * height_8, width_8,
                                    height_8)
                pg.draw.rect(window, (255, 255, 255), white_box)

    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j] not in ['⬛', '⬜', "❌"]:
                window.blit(a[i][j].image, tuple(a[i][j].placement))
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j] == '❌':
                window.blit(poss_places, (int(j * height_8), int(i * width_8)))
    pg.display.update()


de = [['⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜'],
      ['⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛'],
      ['⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜'],
      ['⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛'],
      ['⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜'],
      ['⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛'],
      ['⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜'],
      ['⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛']]
#♔♕♖♗♘♙♚♛♜♝♞♟


def movement(x, xo, y, yo, once,clr):  #=-=-THE HOLY GRAIL-=-=  (fyi touching this function is treason)
    if x < 0 or x > 7 or y < 0 or y > 7:  # checks if out of index
        return
    if a[x][y] == de[x][y]:  # add and a[x][y] == enemy
        a[x][y] = '❌'
        print(f'you can move to {x},{y}')
        if once == True:
            return
    elif  str(a[x][y].color) != clr: # and a[x][y] != de[x][y]:
      a[x][y].under_attack = True
      print(f'you can move to {x},{y}')
      return
    else:
        return
    return movement(x + xo, xo, y + yo, yo, once,clr)


class Pieces(object):

    def __init__(self, x, y, color, board, emoji, placement, image,under_attack=False):
        self.x, self.y = x, y
        self.color = color
        self.a = board
        a[self.x][self.y] = self
        self.emoji = emoji
        self.placement = placement
        self.image = image
        self.under_attack = under_attack 
        

    def __str__(self):
        return f'{self.emoji}'
    def long_poss_moves(self):  # long moves
        # global x1
        # global y1
        if isinstance(self, Rook) or isinstance(self, Queen):
            #right 0 +1
            movement(self.x + 0, 0, self.y + 1, 1, False, self.color)
            #left 0 -1
            movement(self.x + 0, 0, self.y + -1, -1, False, self.color)
            #up -1 0
            movement(self.x + -1, -1, self.y + 0, 0, False, self.color)
            #down +1 0
            movement(self.x + 1, 1, self.y + 0, 0, False, self.color)
        if isinstance(self, Bishop) or isinstance(self, Queen):
            #upright -1 +1
            movement(self.x + -1, -1, self.y + 1, 1, False, self.color)
            #dwnleft +1 -1
            movement(self.x + 1, 1, self.y + -1, -1, False, self.color)
            #upleft  -1 -1
            movement(self.x + -1, -1, self.y + -1, -1, False, self.color)
            #downright +1 +1
            movement(self.x + +1, +1, self.y + 1, 1, False, self.color)
        board()

    #ALL THE KING NEEDS IS IN HERE
    def short_poss_moves(self):

        movement(self.x + -1, -1, self.y + 0, 0, True, self.color)
        # up -1 0
        #eat only or king:
        movement(self.x + -1, -1, self.y + 1, 1, True, self.color)
        # upright -1 +1
        movement(self.x + -1, -1, self.y + -1, -1, True, self.color)
        # upleft  -1 -1
        if self.moved == False and isinstance(self, Pawn):
            movement(self.x - 2, -2, self.y, 0, True, self.color)
        # double up

        ##### KING:
        if isinstance(self, King):
            movement(self.x + -1, -1, self.y + 1, 1, True, self.color)
            # dwnleft +1 -1
            movement(self.x + +1, -1, self.y + -1, 1, True, self.color)
            # downright -1 +1
            movement(self.x + +1, -1, self.y + 1, 1, True, self.color)
            # right 0 +1
            movement(self.x + 0, 0, self.y + 1, 1, True, self.color)
            # left 0 -1
            movement(self.x + 0, 0, self.y - 1, 1, True, self.color)
            # down +1 0
            movement(self.x + 1, 1, self.y + 0, 0, True, self.color)
        board()

    def poss_moves(self):  # Horse
        # global x1
        # global y1
        #upright -2 1
        movement(self.x + -2, -2, self.y + 1, 1, True, self.color)
        #up left -2 -1
        movement(self.x + -2, -2, self.y + -1, -1, True, self.color)
        #down right 2 1
        movement(self.x + 2, 2, self.y + 1, 1, True, self.color)
        #down left 2 -1
        movement(self.x + 2, 2, self.y + -1, -1, True, self.color)
        #right up -1 2
        movement(self.x + -1, -1, self.y + 2, 2, True, self.color)
        #right down 1 +2
        movement(self.x + 1, 1, self.y + 2, 1, True, self.color)
        #left up -1 -2
        movement(self.x + -1, -1, self.y + -2, -2, True, self.color)
        #left down +1 -2
        movement(self.x + 1, 1, self.y + -2, -2, True, self.color)

        board()

    def move(self, inpx, inpy):
      if self.a[inpx][inpy] != de[inpx][inpy]:
        if self.a[inpx][inpy] == '❌' or a[inpx][inpy].under_attack == True:
            self.moved = True
            self.a[self.x][self.y] = de[self.x][
                self.y]  #previous location becomes empty
            a[self.x][self.y] = de[self.x][
                self.y]  #previous location becomes empty in main board
            self.x, self.y = inpx, inpy  #object's new coords are inputs
            # self.a[inpx][inpy] = self
            a[inpx][inpy] = self
            #images placement
            self.placement[0] += (x1 - x) * width_8
            self.placement[1] += (y1 - y) * height_8
        for i in range(8):
            for j in range(8):
              print(self.a[i][j],de[i][j])
              if a[i][j] == '❌':
                print("1 ",self.a[i][j],de[i][j])
                a[i][j] = de[i][j]
              elif a[i][j] != de[i][j]:
                a[i][j].under_attack = False
    pg.display.update()


def check_piece(x, y):
    if isinstance(a[x][y], Pawn) or isinstance(a[x][y], King):
        a[x][y].short_poss_moves()
    elif isinstance(a[x][y], Rook) or isinstance(
            a[x][y], Bishop) or isinstance(a[x][y], Queen):
        a[x][y].long_poss_moves()
    elif isinstance(a[x][y], Horse):
        a[x][y].poss_moves()


class Pawn(Pieces):

    def __init__(self, x: int, y: int, color: str, board: list, emoji,
                 placement, image, under_attack):
        super().__init__(x, y, color, board, emoji, placement, image, under_attack)
        self.moved = False
        #once moved can only go up in ones


class Rook(Pieces):

    def __init__(self, x: int, y: int, color: str, board: list, emoji,
                 placement, image, under_attack):
        super().__init__(x, y, color, board, emoji, placement, image, under_attack)


class Bishop(Pieces):

    def __init__(self, x: int, y: int, color: str, board: list, emoji,
                 placement, image, under_attack):
        super().__init__(x, y, color, board, emoji, placement, image, under_attack)
        self.image = bishop_white


class Queen(Pieces):

    def __init__(self, x: int, y: int, color: str, board: list, emoji,
                 placement, image, under_attack):
        super().__init__(x, y, color, board, emoji, placement, image, under_attack)


class King(Pieces):

    def __init__(self, x: int, y: int, color: str, board: list, emoji,
                 placement, image, under_attack):
        super().__init__(x, y, color, board, emoji, placement, image, under_attack)
        self.moved = False
        self.image = king_white

        #once moved, cannot castle


class Horse(Pieces):

    def __init__(self, x: int, y: int, color: str, board: list, emoji,
                 placement, image, under_attack):
        super().__init__(x, y, color, board, emoji, placement, image, under_attack)
        self.image = knight_white1


def board():
    x = ''
    for i in range(8):
        x += (str(i) + '\t')
    print('\t' + x)
    z = -1
    for i in a:
        z += 1
        for j in i:
            x += (str(j) + '\t')
        print()
        print(str(z) + '\t' + x)
        x = ''


a = [['⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜'],
     ['⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛'],
     ['⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜'],
     ['⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛'],
     ['⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜'],
     ['⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛'],
     ['⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜'],
     ['⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛']]

# test cases:
# the placement is flexible thanks to math
pawn0 = Pawn(6, 0, 'w', a, "♟", [width_8 / 5, height_8 * 6 + height_8 / 10],
             pawn_white, False)
pawn1 = Pawn(6, 1, 'w', a, "♟",
             [width_8 / 5 + width_8, height_8 * 6 + height_8 / 10], pawn_white, False)
pawn2 = Pawn(6, 2, 'w', a, "♟",
             [width_8 / 5 + width_8 * 2, height_8 * 6 + height_8 / 10],
             pawn_white, False)
pawn3 = Pawn(6, 3, 'w', a, "♟",
             [width_8 / 5 + width_8 * 3, height_8 * 6 + height_8 / 10],
             pawn_white, False)
pawn4 = Pawn(6, 4, 'w', a, "♟",
             [width_8 / 5 + width_8 * 4, height_8 * 6 + height_8 / 10],
             pawn_white, False)
pawn5 = Pawn(6, 5, 'w', a, "♟",
             [width_8 / 5 + width_8 * 5, height_8 * 6 + height_8 / 10],
             pawn_white, False)
pawn6 = Pawn(6, 6, 'w', a, "♟",
             [width_8 / 5 + width_8 * 6, height_8 * 6 + height_8 / 10],
             pawn_white, False)
pawn7 = Pawn(6, 7, 'w', a, "♟",
             [width_8 / 5 + width_8 * 7, height_8 * 6 + height_8 / 10],
             pawn_white, False)

rook0 = Rook(7, 0, 'w', a, "♜", [width_8 / 6.5, height_8 / 10 + height_8 * 7],
             rook_white, False)
rook1 = Rook(7, 7, 'w', a, "♜",
             [width_8 / 6.5 + width_8 * 7, height_8 / 10 + height_8 * 7],
             rook_white, False)

bishop0 = Bishop(7, 1, "w", a, "♗", [width_8, height_8 / 20 + height_8 * 7],
                 bishop_white, False)
bishop1 = Bishop(7, 6, "w", a, "♗",
                 [width_8 * 6, height_8 / 20 + height_8 * 7], bishop_white, False)

queen = Queen(7, 3, "w", a, "♕",
              [width_8 / 50 + width_8 * 3, height_8 / 10 + height_8 * 7],
              queen_white, False)
king = King(7, 4, "w ", a, "♔",
            [width_8 / 12 + width_8 * 4, height_8 / 12 + height_8 * 7],
            queen_white, False)

hrus = Horse(7, 2, 'w', a, "♞", [width_8 * 2, height_8 / 50 + height_8 * 7],
             knight_white1, False)
hrus1 = Horse(7, 5, 'w', a, "♞", [width_8 * 5, height_8 / 50 + height_8 * 7],
              knight_white2, False)

#Segregation
#pawn_black
#knight_black1
#knight_black2
#rook_black
#bishop_black
#queen_black
#king_black
pawn8 = Pawn(0, 0, 'b', a, "♟", [width_8 / 5, height_8 * 6 + height_8 / 10],
             pawn_black, False)
pawn9 = Pawn(0, 1, 'b', a, "♟",
             [width_8 / 5 + width_8, height_8 * 6 + height_8 / 10], pawn_black, False)
pawn10 = Pawn(0, 2, 'b', a, "♟",
             [width_8 / 5 + width_8 * 2, height_8 * 6 + height_8 / 10],
             pawn_black, False)
pawn11 = Pawn(0, 3, 'b', a, "♟",
             [width_8 / 5 + width_8 * 3, height_8 * 6 + height_8 / 10],
             pawn_black, False)
pawn12 = Pawn(0, 4, 'b', a, "♟",
             [width_8 / 5 + width_8 * 4, height_8 * 6 + height_8 / 10],
             pawn_black, False)
pawn13 = Pawn(0, 5, 'b', a, "♟",
             [width_8 / 5 + width_8 * 5, height_8 * 6 + height_8 / 10],
             pawn_black, False)
pawn14 = Pawn(0, 6, 'b', a, "♟",
             [width_8 / 5 + width_8 * 6, height_8 * 6 + height_8 / 10],
             pawn_black, False)
pawn15 = Pawn(0, 7, 'b', a, "♟",
             [width_8 / 5 + width_8 * 7, height_8 * 6 + height_8 / 10],
             pawn_black, False)

rook2 = Rook(1, 0, 'b', a, "♜", [width_8 / 6.5, height_8 / 10 + height_8 * 7],
             rook_black, False)
rook3 = Rook(1, 7, 'b', a, "♜",
             [width_8 / 6.5 + width_8 * 7, height_8 / 10 + height_8 * 7],
             rook_black, False)

bishop2 = Bishop(1, 1, "b", a, "♗", [width_8, height_8 / 20 + height_8 * 7],
                 bishop_black, False)
bishop3 = Bishop(1, 6, "b", a, "♗",
                 [width_8 * 6, height_8 / 20 + height_8 * 7], bishop_black, False)

queen1 = Queen(1, 3, "b", a, "♕",
              [width_8 / 50 + width_8 * 3, height_8 / 10 + height_8 * 7],
              queen_black, False)
king1 = King(1, 4, "b", a, "♔",
            [width_8 / 12 + width_8 * 4, height_8 / 12 + height_8 * 7],
            king_black, False)

hrus2 = Horse(1, 2, 'b', a, "♞", [width_8 * 2, height_8 / 50 + height_8 * 7],
             knight_black1, False)
hrus3 = Horse(1, 5, 'b', a, "♞", [width_8 * 5, height_8 / 50 + height_8 * 7],
              knight_black2, False)

board()
print()

# update_window()
x = None


def main():
    global x
    global y
    global x1
    global y1

    run = True
    #setting the fps to 60 part 1
    clock = pg.time.Clock()
    while run:
        # setting the fps to 60 part 2
        clock.tick(60)
        #quit the game if the game window is closed
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False


#the mouse click code is 1025
#detecting the mouse click and getting the position
            if pg.mouse.get_pressed() == (1, 0, 0) and x == None:
                player = str(pg.mouse.get_pos()).split(", ")
                x, y = int((player[0].split("("))[1]) // width_8, int(
                    (player[1].split(")"))[0]) // height_8
                if a[y][x] in ['⬛', '⬜']:
                    x = None
                else:

                    #drawing a box and getting the peice clicked
                    red_box = pg.Rect((x) * width_8, (y) * height_8, width_8,
                                      height_8)
                    pg.draw.rect(window, (125, 0, 0), red_box)
                    check_piece(y, x)
                    board()

                    update_window()
            #moving the peice
            elif pg.mouse.get_pressed() == (1, 0, 0) and x != None:
                player = str(pg.mouse.get_pos()).split(", ")
                x1, y1 = int((player[0].split("("))[1]) // width_8, int(
                    (player[1].split(")"))[0]) // height_8
                # drawing a box and editing the value in the grid
                green_box = pg.Rect((x1) * width_8, (y1) * height_8, width_8,
                                    height_8)
                pg.draw.rect(window, (0, 125, 0), green_box)

                a[y][x].move(y1, x1)

                x = None
                board()

                pg.display.update()
            else:
                update_window()

    pg.quit()

if __name__ == "__main__":
    main()
