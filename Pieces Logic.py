import pygame as pg
# ui
# the properties of the window
pg.init()
main_font = pg.font.SysFont("Arial", 50)
window = pg.display.set_mode((800, 800))
pg.display.set_caption("chess")

width, height = pg.display.get_desktop_sizes()[0][1] - 50, pg.display.get_desktop_sizes()[0][1]- 50
width_8, height_8 = int(width / 8), int(height / 8)
window = pg.display.set_mode((width, height), pg.RESIZABLE)
# pg.display.toggle_fullscreen()

# import the assets
def import_images():
    knight_white1_base = pg.image.load("chess images/knight white1.png")
    knight_white2_base = pg.image.load("chess images/knight white2.png")
    pawn_white_base = pg.image.load("chess images/pawn white.png")
    bishop_white_base = pg.image.load("chess images/bishop white.png")
    queen_white_base = pg.image.load("chess images/queen white.png")
    king_white_base = pg.image.load("chess images/king white.png")
    rook_white_base = pg.image.load("chess images/rock white.png")

    knight_black1_base = pg.image.load("chess images/knight black1.png")
    knight_black2_base = pg.image.load("chess images/knight black2.png")
    pawn_black_base = pg.image.load("chess images/pawn black.png")
    bishop_black_base = pg.image.load("chess images/bishop black.png")
    queen_black_base = pg.image.load("chess images/queen black.png")
    king_black_base = pg.image.load("chess images/king black.png")
    rook_black_base = pg.image.load("chess images/rock black.png")

    poss_places_base = pg.image.load("chess images/dot.png")
    button_img_base = pg.image.load("chess images/pngegg.png")
    # meme_base = pg.image.load("chess images/WIN_20221006_20_18_20_Pro.jpg")
    globals().update(locals())
import_images()
def resize_images():
    knight_white1 = pg.transform.scale(knight_white1_base, (knight_white1_base.get_width() / 1.6 * width / 800,knight_white1_base.get_height() / 1.6 * height / 800))
    knight_white2 = pg.transform.scale(knight_white2_base, (knight_white2_base.get_width() / 1.6 * width / 800,knight_white2_base.get_height() / 1.6 * height / 800))
    pawn_white = pg.transform.scale(pawn_white_base,(pawn_white_base.get_width() / 1.7 * width / 800,pawn_white_base.get_height() / 1.7 * height / 800))
    bishop_white = pg.transform.scale(bishop_white_base, (bishop_white_base.get_width() / 1.7 * width / 800,bishop_white_base.get_height() / 1.7 * height / 800))
    queen_white = pg.transform.scale(queen_white_base, (queen_white_base.get_width() / 1.7 * width / 800,queen_white_base.get_height() / 1.7 * height / 800))
    king_white = pg.transform.scale(king_white_base,(king_white_base.get_width() / 1.7 * width / 800,king_white_base.get_height() / 1.7 * height / 800))
    rook_white = pg.transform.scale(rook_white_base,(rook_white_base.get_width() / 1.7 * width / 800,rook_white_base.get_height() / 1.7 * height / 800))

    knight_black1 = pg.transform.scale(knight_black1_base, (knight_black1_base.get_width() / 1.6 * width / 800, knight_black1_base.get_height() / 1.6 * height / 800))
    knight_black2 = pg.transform.scale(knight_black2_base, (knight_black2_base.get_width() / 1.6 * width / 800, knight_black2_base.get_height() / 1.6 * height / 800))
    pawn_black = pg.transform.scale(pawn_black_base, (pawn_black_base.get_width() / 1.6 * width / 800, pawn_black_base.get_height() / 1.6 * height / 800))
    bishop_black = pg.transform.scale(bishop_black_base, (bishop_black_base.get_width() / 1.7 * width / 800, bishop_black_base.get_height() / 1.7 * height / 800))
    queen_black = pg.transform.scale(queen_black_base, (queen_black_base.get_width() / 1.7 * width / 800, queen_black_base.get_height() / 1.7 * height / 800))
    king_black = pg.transform.scale(king_black_base, (king_black_base.get_width() / 1.6 * width / 800, king_black_base.get_height() / 1.6 * height / 800))
    rook_black = pg.transform.scale(rook_black_base, (rook_black_base.get_width() / 1.6 * width / 800, rook_black_base.get_height() / 1.6 * height / 800))
    poss_places = pg.transform.scale(poss_places_base,(width_8, height_8))
    button_img = pg.transform.scale(button_img_base, (width_8, height_8))
    # meme = pg.transform.scale(meme_base, (width_8, height_8))
    globals().update(locals())
resize_images()

def update_window():
    global width_8, height_8, width, height
    brown = (100, 65, 30)
    window.fill(brown)

    #check if the window is res
    # if width != pg.display.get_surface().get_height():
    #     width, height = pg.display.get_surface().get_height(), pg.display.get_surface().get_height()
    #     width_8, height_8 = int(width / 8), int(height / 8)
    #     resize_images()

    # draw the grid area
    for i in range(len(a)):
        for j in range(len(a[i])):
            if (i % 2 == 0 and j % 2 == 0) or (i % 2 == 1 and j % 2 == 1):
                white_box = pg.Rect(i * width_8, j * height_8, width_8, height_8)
                pg.draw.rect(window, (255, 255, 255), white_box)
    #dray the peices
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j] not in ['⬛', '⬜', "❌", "O"]:
                if a[i][j].under_attack == True:
                    # window.blit(meme, (j * width_8, i * height_8))
                    red_box = pg.Rect(j * width_8, i * height_8, width_8, height_8)
                    pg.draw.rect(window, (100, 0, 0), red_box)
                a[i][j].set_placement()
                window.blit(a[i][j].image, tuple(a[i][j].get_placement()))
                if a[i][j].pinned > 0:
                    blue_box = pg.Rect(j * width_8, i * height_8, width_8, height_8)
                    pg.draw.rect(window, (0, 0, 125), blue_box)

    #draw the possible moves or the buttons if needed
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j] in ['❌',"O"]:
                window.blit(poss_places, (int(j * width_8), int(i * height_8)))
        if isinstance(a[7][i], Pawn) or isinstance(a[0][i], Pawn):
            k = 0
            while k < len(btn_lst):
                btn_lst[k].update()
                k+=1

    pg.display.update()

a = [['⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜'],
     ['⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛'],
     ['⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜'],
     ['⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛'],
     ['⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜'],
     ['⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛'],
     ['⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜'],
     ['⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛']]
de = [['⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜'],
      ['⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛'],
      ['⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜'],
      ['⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛'],
      ['⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜'],
      ['⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛'],
      ['⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜'],
      ['⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛']]
# ♔♕♖♗♘♙♚♛♜♝♞♟

def movement(x, xo, y, yo, once, passive, clr, area, pin_counter, possible_pin):  # =-=-THE HOLY GRAIL-=-=  (fyi touching this function is treason)
    global possKing
    path_mark = '❌' if clr == "w" else "O"
    if x < 0 or x > 7 or y < 0 or y > 7:  # checks if out of index
        return
    # print(possKing, a[x][y])
    if area[x][y] == de[x][y] and pin_counter == 0 and (area is a):  # add and a[x][y] == enemy ###########
        if passive == 1: #relates to pawn logic
            return
        if possKing == False:
            area[x][y] = path_mark
            print(f'you can move to {x},{y}')
    elif area[x][y] != de[x][y] and str(a[x][y].color) != clr:
        if passive == 0: #relates to pawn logic
            return
        if possKing:
            if isinstance(area[x][y], King):
                print("\n\n\n\nUNDER CHECK\n\n\n\n")
                return
        #the first peice is put under attack and raising the pin counter
        if pin_counter == 0:
            area[x][y].under_attack = True
            pin_counter += 1
            possible_pin = [x,y]
            print(f'you can move to {x},{y}')
        #if the second peice is the king pin the peice if not return
        elif pin_counter > 0 and isinstance(area[x][y], King):
            area[possible_pin[0]][possible_pin[1]].pinned += 1
            print(area[possible_pin[0]][possible_pin[1]].pinned)
            return
        else:
            return
    else:  # str(a[x][y].color) == clr:
        return
    if once == True:
        return
    return movement(x + xo, xo, y + yo, yo, once, passive, clr, area, pin_counter, possible_pin)
class Pieces(object):
    def __init__(self, x, y, color, emoji):
        self.x, self.y = x, y
        self.color = color
        a[self.x][self.y] = self
        self.emoji = emoji
        self.under_attack = False
        self.pinned = 0
        self.attacking_king = False
        self.moved = False
        self._placement = [0,0]

    def __str__(self):
        return f'{self.emoji}'

    def long_poss_moves(self):  # long moves
        def longMoves(TF):
            if isinstance(self, Rook) or isinstance(self, Queen) or isinstance(self, King):
                # right 0 +1
                movement(self.x + 0, 0, self.y + 1, 1, TF, None, self.color ,a, 0, None)
                # left 0 -1
                movement(self.x + 0, 0, self.y + -1, -1, TF, None, self.color ,a, 0, None)
                # up -1 0
                movement(self.x + -1, -1, self.y + 0, 0, TF, None, self.color ,a, 0, None)
                # down +1 0
                movement(self.x + 1, 1, self.y + 0, 0, TF, None, self.color ,a, 0, None)
            if isinstance(self, Bishop) or isinstance(self, Queen) or isinstance(self, King):
                # upright -1 +1
                movement(self.x + -1, -1, self.y + 1, 1, TF, None, self.color ,a, 0, None)
                # dwnleft +1 -1
                movement(self.x + 1, 1, self.y + -1, -1, TF, None, self.color ,a, 0, None)
                # upleft  -1 -1
                movement(self.x + -1, -1, self.y + -1, -1, TF, None, self.color ,a, 0, None)
                # downright +1 +1
                movement(self.x + +1, +1, self.y + 1, 1, TF, None, self.color ,a, 0, None)
        if isinstance(self, King):
            longMoves(True)
        else:
            longMoves(False)
    def pawn_moves(self):
        def moves(m):
            if self.moved == False and a[self.x + (-1 *m)][self.y] == de[self.x + (-1*m)][self.y]:
                # double up
                movement(self.x + (-2*m), (-2*m), self.y, 0, True, 0, self.color ,a, 0, None)
            movement(self.x + (-1*m), (-1*m), self.y + 0, 0, True, 0, self.color ,a, 0, None)  # up True #up right False #default False
            # up -1 0
            movement(self.x + (-1*m), (-1*m), self.y + (1*m), (1*m), True, 1, self.color ,a, 0, None)
            # upright -1 +1
            movement(self.x + (-1*m), (-1*m), self.y + (-1*m), (-1*m), True, 1, self.color ,a, 0, None)
            # upleft  -1 -1
        if self.color == "w":
            moves(1)
        else:
            moves(-1)
    def horse_moves(self):  # Horse
        # upright -2 1
        movement(self.x + -2, -2, self.y + 1, 1, True, None, self.color ,a, 0, None)
        # up left -2 -1
        movement(self.x + -2, -2, self.y + -1, -1, True, None, self.color ,a, 0, None)
        # down right 2 1
        movement(self.x + 2, 2, self.y + 1, 1, True, None, self.color ,a, 0, None)
        # down left 2 -1
        movement(self.x + 2, 2, self.y + -1, -1, True, None, self.color ,a, 0, None)
        # right up -1 2
        movement(self.x + -1, -1, self.y + 2, 2, True, None, self.color ,a, 0, None)
        # right down 1 +2
        movement(self.x + 1, 1, self.y + 2, 1, True, None, self.color ,a, 0, None)
        # left up -1 -2
        movement(self.x + -1, -1, self.y + -2, -2, True, None, self.color ,a, 0, None)
        # left down +1 -2
        movement(self.x + 1, 1, self.y + -2, -2, True, None, self.color ,a, 0, None)
    def move(self, inpx, inpy):
        global coord , turn_counter, turn_color
        if a[inpx][inpy] != de[inpx][inpy]:
            if a[inpx][inpy] in ['❌', "O"] or a[inpx][inpy].under_attack == True:
                self.moved = True
                a[self.x][self.y] = de[self.x][
                    self.y]  # previous location becomes empty in main board
                self.x, self.y = inpx, inpy  # object's new coords are inputs
                a[inpx][inpy] = self
                # change the turn
                turn_counter += 1
                turn_color = "w" if turn_counter % 2 else "b"
                #if a pawn reached the end, promote
                if isinstance(a[self.x][self.y],Pawn) and (self.x == 0 or self.x == 7):
                    make_buttons()
                    #takes the coordinates for the pawn to promote
                    coord = [self.x,self.y]

        for i in range(8):
            for j in range(8):
                if a[i][j] in ['❌', "O"]:
                    a[i][j] = de[i][j]
                elif a[i][j] != de[i][j]:
                    a[i][j].under_attack = False
    def get_placement(self):
        return self._placement
    pg.display.update()

def check_piece(x, y, clr):
    if isinstance(a[x][y], Pawn):
        a[x][y].pawn_moves() if a[x][y].color == clr else False
    elif isinstance(a[x][y], Horse):
        a[x][y].horse_moves() if a[x][y].color == clr else False
    elif (isinstance(a[x][y],King) or isinstance(a[x][y], Rook) or isinstance(a[x][y], Bishop) or isinstance(a[x][y], Queen)):
        a[x][y].long_poss_moves() if a[x][y].color == clr else False

class Pawn(Pieces):
    def set_placement(self):
        self.image = pawn_white if self.color == "w" else pawn_black
        self._placement = [width_8 / 5 + width_8 *self.y, height_8 * self.x + height_8 / 10]
class Rook(Pieces):
    def set_placement(self):
        self.image = rook_white if self.color == "w" else rook_black
        self._placement = [width_8 / 6.5 + width_8 *self.y, height_8 * self.x + height_8 / 25]
class Bishop(Pieces):
    def set_placement(self):
        self.image = bishop_white if self.color == "w" else bishop_black
        self._placement = [width_8 *self.y, height_8 * self.x + height_8 / 20]
class Queen(Pieces):
    def set_placement(self):
        self.image = queen_white if self.color == "w" else queen_black
        self._placement = [width_8 / 50 + width_8 *self.y, height_8 * self.x + height_8 / 10]
class King(Pieces):
        # once moved, cannot castle
    def set_placement(self):
        self.image = king_white if self.color == "w" else king_black
        self._placement = [width_8 / 50 + width_8 * self.y, height_8 * self.x + height_8 / 50]
class Horse(Pieces):
    def set_placement(self):
        if self.color == "w":
            self.image = knight_white1 if self.y == 2 else knight_white2
        else: self.image = knight_black1 if self.y == 2 else knight_black2
        self._placement = [width_8 / 50 + width_8 *self.y, height_8 * self.x + height_8 / 50]

def board():
    x = ''
    for i in range(8):
        x += (str(i) + '\t')
    print('\t' + x)
    z = -1
    x=''
    for i in a:
        z += 1
        for j in i:
            x += (str(j) + '\t')
        print()
        print(str(z) + '\t' + x)
        x = ''
board()

def check_threat():
    turn_color = "w" if turn_counter % 2 else "b"
    for i in range(2):
        for i in range(8):
            for j in range(8):
                check_piece(i, j, turn_color)
        turn_color = "b" if turn_counter % 2 else "w"

    if possKing == False: # if found king
        return True
    return False


# test cases:
# the placement is flexible thanks to math <3 😘💋
def ClassicOrientation():
    pawn0 = Pawn(6, 0, 'w', a, "♟", [width_8 / 5, height_8 * 6 + height_8 / 10],
                 pawn_white, False, False)
    pawn1 = Pawn(6, 1, 'w', a, "♟",
                 [width_8 / 5 + width_8, height_8 * 6 + height_8 / 10], pawn_white, False, False)
    pawn2 = Pawn(6, 2, 'w', a, "♟",
                 [width_8 / 5 + width_8 * 2, height_8 * 6 + height_8 / 10],
                 pawn_white, False, False)
    pawn3 = Pawn(6, 3, 'w', a, "♟",
                 [width_8 / 5 + width_8 * 3, height_8 * 6 + height_8 / 10],
                 pawn_white, False, False)
    pawn4 = Pawn(6, 4, 'w', a, "♟",
                 [width_8 / 5 + width_8 * 4, height_8 * 6 + height_8 / 10],
                 pawn_white, False, False)
    pawn5 = Pawn(6, 5, 'w', a, "♟",
                 [width_8 / 5 + width_8 * 5, height_8 * 6 + height_8 / 10],
                 pawn_white, False, False)
    pawn6 = Pawn(6, 6, 'w', a, "♟",
                 [width_8 / 5 + width_8 * 6, height_8 * 6 + height_8 / 10],
                 pawn_white, False, False)
    pawn7 = Pawn(6, 7, 'w', a, "♟",
                 [width_8 / 5 + width_8 * 7, height_8 * 6 + height_8 / 10],
                 pawn_white, False, False)

    rook0 = Rook(7, 0, 'w', a, "♜", [width_8 / 6.5, height_8 / 10 + height_8 * 7],
                 rook_white, False, False)
    rook1 = Rook(7, 7, 'w', a, "♜",
                 [width_8 / 6.5 + width_8 * 7, height_8 / 10 + height_8 * 7],
                 rook_white, False, False)

    bishop0 = Bishop(7, 2, "w", a, "♗", [width_8 * 2, height_8 / 20 + height_8 * 7],bishop_white, False, False)
    bishop1 = Bishop(7, 5, "w", a, "♗",[width_8 * 5, height_8 / 20 + height_8 * 7], bishop_white, False, False)

    queen = Queen(7, 3, "w", a, "♕",[width_8 / 50 + width_8 * 3, height_8 / 10 + height_8 * 7],queen_white, False, False)
    king = King(7, 4, "w", a, "♔",[width_8 / 12 + width_8 * 4, height_8 / 12 + height_8 * 7],king_white, False)

    hrus = Horse(7, 1, 'w', a, "♞", [width_8, height_8 / 50 + height_8 * 7],knight_white1, False, False)
    hrus1 = Horse(7, 6, 'w', a, "♞", [width_8 * 6, height_8 / 50 + height_8 * 7],knight_white2, False, False)

    pawn8 = Pawn(1, 0, 'b', a, "♟", [width_8 / 5, height_8 + height_8 / 10],
                 pawn_black, False, False)
    pawn9 = Pawn(1, 1, 'b', a, "♟",
                 [width_8 / 5 + width_8, height_8 + height_8 / 10], pawn_black, False, False)
    pawn10 = Pawn(1, 2, 'b', a, "♟",
                  [width_8 / 5 + width_8 * 2, height_8 + height_8 / 10],
                  pawn_black, False, False)
    pawn11 = Pawn(1, 3, 'b', a, "♟",
                  [width_8 / 5 + width_8 * 3, height_8 + height_8 / 10],
                  pawn_black, False, False)
    pawn12 = Pawn(1, 4, 'b', a, "♟",
                  [width_8 / 5 + width_8 * 4, height_8 + height_8 / 10],
                  pawn_black, False, False)
    pawn13 = Pawn(1, 5, 'b', a, "♟",
                  [width_8 / 5 + width_8 * 5, height_8 + height_8 / 10],
                  pawn_black, False, False)
    pawn14 = Pawn(1, 6, 'b', a, "♟",
                  [width_8 / 5 + width_8 * 6, height_8 + height_8 / 10],
                  pawn_black, False, False)
    pawn15 = Pawn(1, 7, 'b', a, "♟",
                  [width_8 / 5 + width_8 * 7, height_8 + height_8 / 10],
                  pawn_black, False, False)

    rook2 = Rook(0, 0, 'b', a, "♜", [width_8 / 10, height_8 / 15],
                 rook_black, False, False)
    rook3 = Rook(0, 7, 'b', a, "♜",
                 [width_8 / 6 + width_8 * 7, height_8 / 15],
                 rook_black, False, False)

    bishop2 = Bishop(0, 2, "b", a, "♗", [width_8 * 2, height_8 / 20],bishop_black, False, False)
    bishop3 = Bishop(0, 5, "b", a, "♗",[width_8 * 5 + width_8 / 30, height_8 / 20], bishop_black, False, False)

    queen1 = Queen(0, 3, "b", a, "♕",[width_8 * 3 + width_8 / 20, height_8 / 10],
                   queen_black, False, False)
    king1 = King(0, 4, "b", a, "♔",
                 [width_8 / 20 + width_8 * 4, height_8 / 20],
                 king_black, False)

    hrus2 = Horse(0, 1, 'b', a, "♞", [width_8, height_8 / 20],knight_black1, False, False)
    hrus3 = Horse(0, 6, 'b', a, "♞", [width_8 * 6, height_8 / 50],knight_black2, False, False)
ClassicOrientation()

board()
print()

# update_window()
x = None

def main():
    global x, y, x1, y1, possKing

    run = True
    # setting the fps to 60 part 1
    clock = pg.time.Clock()
    while run:
        # setting the fps to 60 part 2
        clock.tick(60)
        # quit the game if the game window is closed
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            # detecting the mouse click and getting the position
            if event.type == pg.MOUSEBUTTONDOWN and x == None:
                player = str(pg.mouse.get_pos()).split(", ")
                x, y = int((player[0].split("("))[1]) // width_8, int(
                    (player[1].split(")"))[0]) // height_8
                if a[y][x] in ['⬛', '⬜']:
                    x = None
                else:

                    # drawing a box and getting the piece clicked
                    red_box = pg.Rect((x) * width_8, (y) * height_8, width_8,
                                      height_8)
                    pg.draw.rect(window, (125, 0, 0), red_box)
                    check_piece(y, x)
                    board()
                    update_window()
            # moving the piece

            elif event.type == pg.MOUSEBUTTONDOWN and x != None:
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
                possKing = True
                check_threat()
                possKing = False
            else:
                update_window()
    pg.quit()
if __name__ == "__main__":
    main()