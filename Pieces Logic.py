import pygame as pg
import json

# ui
# the properties of the window
pg.init()
main_font = pg.font.SysFont("Arial", 50)
window = pg.display.set_mode((800, 800), pg.RESIZABLE)
pg.display.set_caption("chess")
width, height = 800,800
width_8, height_8 = int(width / 8), int(height / 8)

chess = False
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

    checker_red_base = pg.image.load("chess images/checker red.png")
    checker_black_base = pg.image.load("chess images/checker black.png")

    poss_places_base = pg.image.load("chess images/dot.png")
    button_img_base = pg.image.load("chess images/pngegg.png")
    wallaper_base = pg.image.load("chess images/wallpaper.jpg")
    globals().update(locals())
import_images()
def resize_images():
    knight_white1 = pg.transform.scale(
        knight_white1_base,
        (knight_white1_base.get_width() / 1.6 * width / 800,
         knight_white1_base.get_height() / 1.6 * height / 800))
    knight_white2 = pg.transform.scale(
        knight_white2_base,
        (knight_white2_base.get_width() / 1.6 * width / 800,
         knight_white2_base.get_height() / 1.6 * height / 800))
    pawn_white = pg.transform.scale(
        pawn_white_base, (pawn_white_base.get_width() / 1.7 * width / 800,
                          pawn_white_base.get_height() / 1.7 * height / 800))
    bishop_white = pg.transform.scale(
        bishop_white_base,
        (bishop_white_base.get_width() / 1.7 * width / 800,
         bishop_white_base.get_height() / 1.7 * height / 800))
    queen_white = pg.transform.scale(
        queen_white_base, (queen_white_base.get_width() / 1.7 * width / 800,
                           queen_white_base.get_height() / 1.7 * height / 800))
    king_white = pg.transform.scale(
        king_white_base, (king_white_base.get_width() / 1.7 * width / 800,
                          king_white_base.get_height() / 1.7 * height / 800))
    rook_white = pg.transform.scale(
        rook_white_base, (rook_white_base.get_width() / 1.7 * width / 800,
                          rook_white_base.get_height() / 1.7 * height / 800))

    knight_black1 = pg.transform.scale(
        knight_black1_base,
        (knight_black1_base.get_width() / 1.6 * width / 800,
         knight_black1_base.get_height() / 1.6 * height / 800))
    knight_black2 = pg.transform.scale(
        knight_black2_base,
        (knight_black2_base.get_width() / 1.6 * width / 800,
         knight_black2_base.get_height() / 1.6 * height / 800))
    pawn_black = pg.transform.scale(
        pawn_black_base, (pawn_black_base.get_width() / 1.6 * width / 800,
                          pawn_black_base.get_height() / 1.6 * height / 800))
    bishop_black = pg.transform.scale(
        bishop_black_base,
        (bishop_black_base.get_width() / 1.7 * width / 800,
         bishop_black_base.get_height() / 1.7 * height / 800))
    queen_black = pg.transform.scale(
        queen_black_base, (queen_black_base.get_width() / 1.7 * width / 800,
                           queen_black_base.get_height() / 1.7 * height / 800))
    king_black = pg.transform.scale(
        king_black_base, (king_black_base.get_width() / 1.6 * width / 800,
                          king_black_base.get_height() / 1.6 * height / 800))
    rook_black = pg.transform.scale(
        rook_black_base, (rook_black_base.get_width() / 1.6 * width / 800,
                          rook_black_base.get_height() / 1.6 * height / 800))
    poss_places = pg.transform.scale(poss_places_base, (width_8, height_8))
    button_img = pg.transform.scale(button_img_base, (width / 2, height_8))

    checker_red = pg.transform.scale(
        checker_red_base,
        (checker_red_base.get_width() / 1.7 * width / 800,
         checker_red_base.get_height() / 1.7 * height / 800))
    checker_black = pg.transform.scale(
        checker_black_base,
        (checker_black_base.get_width() / 1.7 * width / 800,
         checker_black_base.get_height() / 1.7 * height / 800))

    wallaper = pg.transform.scale(
        wallaper_base, (wallaper_base.get_width() *1.755,
                          wallaper_base.get_height() *1.755 ))
    globals().update(locals())
resize_images()
def update_window():
    global width_8, height_8, width, height
    brown = (100, 65, 30)
    window.fill(brown)

    # check if the window is res
    if width != pg.display.get_surface().get_height():
        width, height = pg.display.get_surface().get_height(), pg.display.get_surface().get_height()
        width_8, height_8 = int(width / 8), int(height / 8)
        resize_images()

    # draw the grid area
    for i in range(len(a)):
        for j in range(len(a[i])):
            if (i % 2 == 0 and j % 2 == 0) or (i % 2 == 1 and j % 2 == 1):
                white_box = pg.Rect(i * width_8, j * height_8, width_8,
                                    height_8)
                pg.draw.rect(window, (255, 255, 255), white_box)
    # Draw the pieces
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j] not in ['⬛', '⬜', "❌", '⚫']:
                if a[i][j].under_attack == True:
                    # window.blit(meme, (j * width_8, i * height_8))
                    red_box = pg.Rect(j * width_8, i * height_8, width_8,
                                      height_8)
                    pg.draw.rect(window, (100, 0, 0), red_box)
                a[i][j].set_placement()
                window.blit(a[i][j].image, tuple(a[i][j].get_placement()))

    # draw the possible moves or the buttons if needed
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j] in ['❌', '⚫']:
                window.blit(poss_places, (int(j * width_8), int(i * height_8)))
        if chess:
            if isinstance(a[7][i], Pawn) or isinstance(a[0][i], Pawn):
                k = 0
                while k < len(btn_lst):
                    btn_lst[k].update()
                    k += 1
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
oldBoard = [['⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜'],
            ['⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛'],
            ['⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜'],
            ['⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛'],
            ['⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜'],
            ['⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛'],
            ['⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜'],
            ['⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛']]
# ♔♕♖♗♘♙♚♛♜♝♞♟
coords = []

def movement(x, xo, y, yo, once, passive, clr, area, pin_counter, possible_pin, extended=0):  # =-=-THE HOLY GRAIL-=-=  (fyi touching this function is treason)
    global possKing, checkmate_check, coords, king_sur, attacker
    path_mark = '❌' if clr == "w" else '⚫'
    opmark = '⚫' if clr == "w" else '❌'
    # if clr == 'w': otherclr = 'b'
    # else: otherclr = 'w'
    if x < 0 or x > 7 or y < 0 or y > 7 :  # checks if out of index
        coords = []
        return

    if area[x][y] == de[x][y] and pin_counter == 0:
        coords.append([x, y])
        if chess:
            if king_sur:
                print(f"=-=-=-=-\n\nking can escape to {pin_area[x][y],x,y}")
                checkmate_check = False
                return
        #if empty square
        if passive == 0: # pawn up
            pass
        elif passive == 1:
            if not possKing or not checkmate_check:
                return
            else:
                pass

        if chess or not extended:
            area[x][y] = path_mark

    if area[x][y] == 'H': #if a free piece can intersect coords not checkmate
        print("\n\n\n\n\n\n\n\n\nintersection at: ", str(area[x][y]),str([x,y]))
        checkmate_check = False
        return
    if area[x][y] == opmark or area[x][y] == path_mark or area[x][y] == 'H':
        pass
    elif area[x][y] != de[x][y] and str(area[x][y].color) != clr:
        #if enemy
        if passive == 0:  #relates to pawn logic [pawn cant eat front]
            return
        if chess:
            if king_sur and [x,y] == attacker:
                checkmate_check = False
                return
            if checkmate_check:
                if x == attacker[0] and y == attacker[1]:
                    print("\n\ncan eat checker\n\n")
                    print(x, y, attacker)
                    print("can eat checker")
                    checkmate_check = False

            if possKing and pin_counter == 0:
                if isinstance(area[x][y], King):
                    print('\n\n\n\n\n', str(coords), "check line of sight\n\n\n\n")
                    possKing = False
                    checkmate(coords)
                    return
            else:
                coords = []
        else:
            if not (x + xo > 7 or x + xo < 0 or y + yo >7 or y + yo < 0):
                if area[x + xo][y + yo] == de[x + xo][y + yo]:
                    area[x + xo][y + yo] = path_mark
                    if not extended:
                        area[x - xo][y - yo].checker_moves(area, turn_color, 2)


        #the first piece is put under attack and raising the pin counter
        if pin_counter == 0 and chess:
            area[x][y].under_attack = True
            pin_counter += 1
            possible_pin = (x, y)

        #if the second piece is the king pin the piece if not return
        elif pin_counter > 0 and isinstance(area[x][y], King):
            a[possible_pin[0]][possible_pin[1]].pinned += 1
            update_window()
            return
        else:
            coords = []
            return

    #if an opposing piece is found, the piece continue checking it's path to check the pin but without leaving a trace
    elif pin_counter > 0 and area[x][y] == de[x][y]:
        return movement(x + xo, xo, y + yo, yo, once, passive, clr, area,
                        pin_counter, possible_pin)
    else:  # str(a[x][y].color) == clr:
        coords = []
        return
    if once == True:
        return
    return movement(x + xo, xo, y + yo, yo, once, passive, clr, area,
                    pin_counter, possible_pin)

# pieces classes
class Pieces(object):

    def __init__(self,
                 x,
                 y,
                 color,
                 emoji,
                 area=a,
                 moved=False,
                 under_attack=False,
                 attacking_king=False,
                 pinned=0, checker_king=False):
        self.x, self.y = x, y
        self.color = color
        area[self.x][self.y] = self
        self.emoji = emoji
        self.under_attack = under_attack
        self.pinned = pinned
        self.attacking_king = attacking_king
        self.moved = moved
        self._placement = [0, 0]
        self.checker_king = checker_king

    def __str__(self):
        return f'{self.emoji}'

    def __dict__(self):
        return {
            'x': self.x,
            "y": self.y,
            "emoji": self.emoji,
            "moved": self.moved,
            "color": self.color,
            "kind": "pawn" if isinstance(self, Pawn) else "rook" if isinstance(self, Rook) else "bishop" if isinstance(
                self, Bishop) else "horse" if isinstance(self, Horse) else "queen" if isinstance(self,
                                                                                                 Queen) else "king" if isinstance(
                self, King) else "checker_peice",
            "checker_king" : self.checker_king
        }

    def long_poss_moves(self, area, turn_color):  # long moves

        def longMoves(TF):
            if isinstance(self, Rook) or isinstance(self, Queen) or isinstance(
                    self, King):
                # right 0 +1
                movement(self.x + 0, 0, self.y + 1, 1, TF, None, turn_color,
                         area, 0, None)
                # left 0 -1
                movement(self.x + 0, 0, self.y + -1, -1, TF, None, turn_color,
                         area, 0, None)
                # up -1 0
                movement(self.x + -1, -1, self.y + 0, 0, TF, None, turn_color,
                         area, 0, None)
                # down +1 0
                movement(self.x + 1, 1, self.y + 0, 0, TF, None, turn_color,
                         area, 0, None)
            if isinstance(self, Bishop) or isinstance(
                    self, Queen) or isinstance(self, King):
                # upright -1 +1
                movement(self.x + -1, -1, self.y + 1, 1, TF, None, turn_color,
                         area, 0, None)
                # dwnleft +1 -1
                movement(self.x + 1, 1, self.y + -1, -1, TF, None, turn_color,
                         area, 0, None)
                # upleft  -1 -1
                movement(self.x + -1, -1, self.y + -1, -1, TF, None,
                         turn_color, area, 0, None)
                # downright +1 +1
                movement(self.x + +1, +1, self.y + 1, 1, TF, None, turn_color,
                         area, 0, None)

        if isinstance(self, King):
            longMoves(True)
        else:
            longMoves(False)

    def pawn_moves(self, area, turn_color):

        def moves(m):
            if self.moved == False and area[self.x + (-1 * m)][self.y] == de[
                self.x + (-1 * m)][self.y]:
                # double up
                movement(self.x + (-2 * m), (-2 * m), self.y, 0, True, 0,
                         turn_color, area, 0, None)
            movement(self.x + (-1 * m), (-1 * m), self.y + 0, 0, True, 0,
                     turn_color, area, 0,
                     None)  # up True #up right False #default False
            # up -1 0
            movement(self.x + (-1 * m), (-1 * m), self.y + (1 * m), (1 * m),
                     True, 1, turn_color, area, 0, None)
            # upright -1 +1
            movement(self.x + (-1 * m), (-1 * m), self.y + (-1 * m), (-1 * m),
                     True, 1, turn_color, area, 0, None)
            # upleft  -1 -1

        if turn_color == "w":
            moves(1)
        else:
            moves(-1)

    def horse_moves(self, area, turn_color):  # Horse
        # upright -2 1
        movement(self.x + -2, -2, self.y + 1, 1, True, None, turn_color, area,
                 0, None)
        # up left -2 -1
        movement(self.x + -2, -2, self.y + -1, -1, True, None, turn_color,
                 area, 0, None)
        # down right 2 1
        movement(self.x + 2, 2, self.y + 1, 1, True, None, turn_color, area, 0,
                 None)
        # down left 2 -1
        movement(self.x + 2, 2, self.y + -1, -1, True, None, turn_color, area,
                 0, None)
        # right up -1 2
        movement(self.x + -1, -1, self.y + 2, 2, True, None, turn_color, area,
                 0, None)
        # right down 1 +2
        movement(self.x + 1, 1, self.y + 2, 1, True, None, turn_color, area, 0,
                 None)
        # left up -1 -2
        movement(self.x + -1, -1, self.y + -2, -2, True, None, turn_color,
                 area, 0, None)
        # left down +1 -2
        movement(self.x + 1, 1, self.y + -2, -2, True, None, turn_color, area,
                 0, None)

    def move(self, inpx, inpy):
        global coord, turn_counter, turn_color
        if a[inpx][inpy] != de[inpx][inpy]:
            if a[inpx][inpy] in ['❌', '⚫'
                                 ] or a[inpx][inpy].under_attack == True:
                self.moved = True
                a[self.x][self.y] = de[self.x][
                    self.y]  # previous location becomes empty in main board
                self.x, self.y = inpx, inpy  # object's new coords are inputs
                a[inpx][inpy] = self
                # change the turn
                turn_counter += 1
                turn_color = "w" if turn_counter % 2 else "b"
                if chess:
                    # if a pawn reached the end, promote
                    if isinstance(a[self.x][self.y], Pawn) and (self.x == 0
                                                                or self.x == 7):
                        make_buttons()
                        # takes the coordinates for the pawn to promote
                        coord = [self.x, self.y]
                else: #checkers
                    #removes everything in it's path
                    m = -1 if y > inpx else 1
                    n = -1 if x > inpy else 1
                    for i, j in zip(range(abs(y - inpx)), range(abs(x - inpy))):
                        a[y + m * i][x + n * j] = de[y + m * i][x + n * j]
                    if inpx in [0, 7] and self.moved == True:
                        self.checker_king = True
        for i in range(8):
            for j in range(8):
                if a[i][j] in ['❌', '⚫']:
                    a[i][j] = de[i][j]
                elif a[i][j] != de[i][j]:
                    a[i][j].under_attack = False

    def get_placement(self):
        return self._placement

    pg.display.update()

class Pawn(Pieces):

    def set_placement(self):
        self.image = pawn_white if self.color == "w" else pawn_black
        self._placement = [
            width_8 / 5 + width_8 * self.y, height_8 * self.x + height_8 / 10
        ]
class Rook(Pieces):

    def set_placement(self):
        self.image = rook_white if self.color == "w" else rook_black
        self._placement = [
            width_8 / 6.5 + width_8 * self.y, height_8 * self.x + height_8 / 25
        ]
class Bishop(Pieces):

    def set_placement(self):
        self.image = bishop_white if self.color == "w" else bishop_black
        self._placement = [width_8 * self.y, height_8 * self.x + height_8 / 20]
class Queen(Pieces):

    def set_placement(self):
        self.image = queen_white if self.color == "w" else queen_black
        self._placement = [
            width_8 / 50 + width_8 * self.y, height_8 * self.x + height_8 / 10
        ]
class King(Pieces):
    # once moved, cannot castle
    def set_placement(self):
        self.image = king_white if self.color == "w" else king_black
        self._placement = [
            width_8 / 50 + width_8 * self.y, height_8 * self.x + height_8 / 50
        ]
class Horse(Pieces):

    def set_placement(self):
        if self.color == "w":
            self.image = knight_white1 if self.y == 2 else knight_white2
        else:
            self.image = knight_black1 if self.y == 2 else knight_black2
        self._placement = [
            width_8 / 50 + width_8 * self.y, height_8 * self.x + height_8 / 50
        ]
class checker_peice(Pieces):
    def set_placement(self):
        self.image = checker_black if self.color == "w" else checker_red
        self._placement = [
            width_8 * self.y + width_8 / 20, height_8 * self.x + height_8 / 20
        ]
    def checker_moves(self, area, turn_color, extended = 0):
        if area[self.x][self.y].color == "w" or self.checker_king:
            # upright -1 +1
            movement(self.x + -1 - extended, -1  , self.y + 1 + extended, 1 , True, None, turn_color,
                     area, 0, None, extended)
            # upleft  -1 -1
            movement(self.x + -1 - extended, -1 , self.y + -1 - extended, -1 , True, None,
                     turn_color, area, 0, None, extended)
        if area[self.x][self.y].color == "b" or self.checker_king:
            # dwnleft +1 -1
            movement(self.x + 1 + extended, 1 , self.y + -1 - extended, -1 , True, None, turn_color,
                     area, 0, None, extended)
            # downright +1 +1
            movement(self.x + 1 + extended, +1 , self.y + 1 + extended, 1, True, None, turn_color,
                     area, 0, None, extended)

def check_piece(x, y, area, turn_color):
    global king_sur, checkmate_check
    if isinstance(area[x][y], Pawn):
        area[x][y].pawn_moves(
            area, turn_color) if area[x][y].color == turn_color else False
    elif isinstance(area[x][y], Horse):
        area[x][y].horse_moves(
            area, turn_color) if area[x][y].color == turn_color else False
    elif (isinstance(area[x][y], King) or isinstance(area[x][y], Rook) or isinstance(area[x][y], Bishop) or isinstance(area[x][y], Queen)):
        if checkmate_check and isinstance(area[x][y], King) and str(area[x][y].color) == turn_color:
            king_sur = True
        area[x][y].long_poss_moves(area, turn_color) if area[x][y].color == turn_color else False
        king_sur = False
    elif isinstance(area[x][y], checker_peice):
        area[x][y].checker_moves(area, turn_color) if area[x][y].color == turn_color else False

def checkmate(coords):
    global checkmate_check, otherclr, a, run
    for i in coords:
        pin_area[i[0]][i[1]] = 'H'  #coords
        board(pin_area)
    print("\n\ndefendboard")

    checkmate_check = True
    check_threat(otherclr) #[defend board] #only pawn zeros (forwards
    print("\n\ndefendboard")

    if not checkmate_check:  #intersection with 'H'
        print("king can escape or piece can intersect")
        return
    else:
        #you win
        checkmate_check = False
        a = [['⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜'],
             ['⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛'],
             ['⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜'],
             ['⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛'],
             ['⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜'],
             ['⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛'],
             ['⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜'],
             ['⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛']]
        win_font = pg.font.SysFont("Arial", 100)
        text_surface = win_font.render(f"player {2 if turn_color == 'b' else 1} wins!", True, (0, 0, 0))
        text_x = width // 2 - text_surface.get_width() // 2
        text_y = height_8 // 2

        update_window()
        run = True
        clock = pg.time.Clock()
        while run:
            clock.tick(5)
            # quit the game if the game window is closed
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    run = False
                else:
                    window.blit(text_surface, (text_x, text_y))
                    pg.display.update()

def wincheck(turnclr, turn_counter):
    global pin_area, possKing, oldBoard, checkmate_check, otherclr, king_surr

    possKing, checkmate_check,king_surr = True, False,False
    pin_area = deep_copy(a)

    if turnclr == 'w': otherclr, othrpath = 'b', '⚫'
    else: otherclr, othrpath = 'w', 'X'


    check_threat(otherclr)  #checking if player is checked [attack board] #pawn diagonal
    print('-=-=', otherclr)
    if not possKing:  #if check: undo
        undo(oldBoard)
        possKing = True
        print("Invalid Move")
        return
    print("IN WINCHECKKKKKKKKKK\n\n\n\n\n")

    pin_area = deep_copy(a)

    check_threat(turnclr)  #attackin board [attack board] #pawn diagonal
    print('-=-=', turnclr)
    if not possKing:  #if check: checkmate #pawn forward
        possKing = True

    oldBoard = deep_copy(a)
    possKing = False
def undo(before):
    global a, turn_counter, turn_color, pin_area
    a = deep_copy(before)
    pin_area = deep_copy(a)

    if turn_color == 'w':
        turn_color = 'b'
    else:
        turn_color = 'w'
    turn_counter -= 1
def check_threat(color):
    global pin_area, possKing, coords, attacker

    #recalculate pinned pieces
    for i in range(8):
        for j in range(8):
            if a[i][j] not in ['⬛', '⬜', "❌", '⚫']:
                a[i][j].pinned = 0

    for i in range(8):
        for j in range(8):
            if possKing:
                attacker = [j,i]
            check_piece(i, j, pin_area, color)
    pg.display.update()

    print(f"\n{color} Moves:\n---------------------\n")
    board(pin_area)
    print("\n---------------------\n")

def board(area):
    x = ''
    for i in range(8):
        x += (str(i) + '\t')
    print('\t' + x)
    z = -1
    x = ''
    for i in area:
        z += 1
        for j in i:
            x += (str(j) + '\t')
        print()
        print(str(z) + '\t' + x)
        x = ''
# copies the board
def deep_copy(copied):
    ret = [['⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜'],
           ['⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛'],
           ['⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜'],
           ['⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛'],
           ['⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜'],
           ['⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛'],
           ['⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜'],
           ['⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛']]
    for i in range(len(copied)):
        for j in range(len(copied[i])):
            if copied[i][j] not in ['⬛', '⬜']:
                peice = copied[i][j]
                if isinstance(peice, Pawn):
                    ret[i][j] = Pawn(peice.x, peice.y, peice.color,
                                     peice.emoji, ret, peice.moved, peice.under_attack,
                                     peice.attacking_king,
                                     peice.pinned)
                elif isinstance(peice, Rook):
                    ret[i][j] = Rook(peice.x, peice.y, peice.color,
                                     peice.emoji, ret, peice.moved, peice.under_attack,
                                     peice.attacking_king,
                                     peice.pinned)
                elif isinstance(peice, Bishop):
                    ret[i][j] = Bishop(peice.x, peice.y, peice.color,
                                       peice.emoji, ret, peice.moved, peice.under_attack,
                                       peice.attacking_king,
                                       peice.pinned)
                elif isinstance(peice, Queen):
                    ret[i][j] = Queen(peice.x, peice.y, peice.color,
                                      peice.emoji, ret, peice.moved, peice.under_attack,
                                      peice.attacking_king,
                                      peice.pinned)
                elif isinstance(peice, King):
                    ret[i][j] = King(peice.x, peice.y, peice.color,
                                     peice.emoji, ret, peice.moved, peice.under_attack,
                                     peice.attacking_king,
                                     peice.pinned)
                elif isinstance(peice, Horse):
                    ret[i][j] = Horse(peice.x, peice.y, peice.color,
                                      peice.emoji, ret, peice.moved, peice.under_attack,
                                      peice.attacking_king,
                                      peice.pinned)
    return ret
pin_area = a

# the placement is flexible thanks to math <3 😘💋
def ClassicOrientation():
    pawn0 = Pawn(6, 0, 'w', "♟")
    pawn1 = Pawn(6, 1, 'w', "♟")
    pawn2 = Pawn(6, 2, 'w', "♟")
    pawn3 = Pawn(6, 3, 'w', "♟")
    pawn4 = Pawn(6, 4, 'w', "♟")
    pawn5 = Pawn(6, 5, 'w', "♟")
    pawn6 = Pawn(6, 6, 'w', "♟")
    pawn7 = Pawn(6, 7, 'w', "♟")
    rook0 = Rook(7, 0, 'w', "♜")
    rook1 = Rook(7, 7, 'w', "♜")

    bishop0 = Bishop(7, 2, "w", "♗")
    bishop1 = Bishop(7, 5, "w", "♗")
    hrus = Horse(7, 1, 'w', "♞")
    hrus1 = Horse(7, 6, 'w', "♞")

    queen = Queen(7, 3, "w", "♕")
    king = King(7, 4, "w", "♔")
    pawn8 = Pawn(1, 0, 'b', "♟")
    pawn9 = Pawn(1, 1, 'b', "♟")
    pawn10 = Pawn(1, 2, 'b', "♟")
    pawn11 = Pawn(1, 3, 'b', "♟")
    pawn12 = Pawn(1, 4, 'b', "♟")
    pawn13 = Pawn(1, 5, 'b', "♟")
    pawn14 = Pawn(1, 6, 'b', "♟")
    pawn15 = Pawn(1, 7, 'b', "♟")
    rook2 = Rook(0, 0, 'b', "♜")
    rook3 = Rook(0, 7, 'b', "♜")

    bishop2 = Bishop(0, 2, "b", "♗")
    bishop3 = Bishop(0, 5, "b", "♗")
    hrus2 = Horse(0, 1, 'b', "♞")
    hrus3 = Horse(0, 6, 'b', "♞")

    queen1 = Queen(0, 3, "b", "♕")
    king1 = King(0, 4, "b", "♔")

def checkers_classicOrientation():
    for i in range(3):
        for j in range(len(a[i])):
            if (i % 2 == 0 and j % 2 == 1) or (i % 2 == 1 and j % 2 == 0):
                a[i][j] = checker_peice(i, j, "b", "k")
            if (i % 2 == 0 and j % 2 == 0) or (i % 2 == 1 and j % 2 == 1):
                a[i + 5][j] = checker_peice(i + 5, j, "w", "n")

def checkers_win_check():
    global a, run
    counter1 = 0
    for i in range(8):
        for j in range(8):
            if isinstance(a[i][j], checker_peice):
                if a[i][j].color == turn_color:
                    a[i][j].checker_moves(a, turn_color)
                    counter1 += 1

    counter2 = 0
    for i in range(8):
        for j in range(8):
            if a[i][j] in ["❌", '⚫']:
                a[i][j] = de[i][j]
                counter2 += 1

    if counter1 == 0 or counter2 == 0:
        # you win
        checkmate_check = False
        print("\n\n\n\n\nCheckmate!!!!!!!!! \n\n\n-=0-=0421-0=4912-4981\n29=0-4812-0498")
        a = [['⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜'],
             ['⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛'],
             ['⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜'],
             ['⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛'],
             ['⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜'],
             ['⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛'],
             ['⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜'],
             ['⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛']]
        win_font = pg.font.SysFont("Arial", 100)
        text_surface = win_font.render(f"player {1 if turn_color == 'b' else 2} wins!", True, (0, 0, 0))
        text_x = width // 2 - text_surface.get_width() // 2
        text_y = height_8 // 2

        update_window()
        run = True
        clock = pg.time.Clock()
        while run:
            clock.tick(5)
            # quit the game if the game window is closed
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    run = False
                else:
                    window.blit(text_surface, (text_x, text_y))
                    pg.display.update()

def save(file):
    with open(file, 'w') as output:
        peices = []
        for i in a:
            for j in i:
                if j not in ['⬛', '⬜', "❌", '⚫']:
                    peices.append(json.dumps(j.__dict__()))
        s = "{\"peices\":[%s]" % ", \n".join(peices) + "}"
        output.write(str(turn_counter) + "\n")
        output.write(s)
def load(file):
    global turn_counter
    with open(file) as save_state:
        turn_counter = int(save_state.readline().strip("\n"))
        peices = save_state.read()
        peices_dict = json.loads(peices)
        for peice in peices_dict["peices"]:
            if peice["kind"] == "pawn":
                a[peice["x"]][peice["y"]] = Pawn(peice["x"], peice["y"], peice["color"], peice["emoji"], a,
                                                 peice["moved"])
                oldBoard[peice["x"]][peice["y"]] = Pawn(peice["x"], peice["y"], peice["color"], peice["emoji"],
                                                        oldBoard, peice["moved"])
            elif peice["kind"] == "rook":
                a[peice["x"]][peice["y"]] = Rook(peice["x"], peice["y"], peice["color"], peice["emoji"], a,
                                                 peice["moved"])
                oldBoard[peice["x"]][peice["y"]] = Rook(peice["x"], peice["y"], peice["color"], peice["emoji"],
                                                        oldBoard, peice["moved"])
            elif peice["kind"] == "bishop":
                a[peice["x"]][peice["y"]] = Bishop(peice["x"], peice["y"], peice["color"], peice["emoji"], a,
                                                   peice["moved"])
                oldBoard[peice["x"]][peice["y"]] = Bishop(peice["x"], peice["y"], peice["color"], peice["emoji"],
                                                          oldBoard, peice["moved"])
            elif peice["kind"] == "queen":
                a[peice["x"]][peice["y"]] = Queen(peice["x"], peice["y"], peice["color"], peice["emoji"], a,
                                                  peice["moved"])
                oldBoard[peice["x"]][peice["y"]] = Queen(peice["x"], peice["y"], peice["color"], peice["emoji"],
                                                         oldBoard, peice["moved"])
            elif peice["kind"] == "king":
                a[peice["x"]][peice["y"]] = King(peice["x"], peice["y"], peice["color"], peice["emoji"], a,
                                                 peice["moved"])
                oldBoard[peice["x"]][peice["y"]] = King(peice["x"], peice["y"], peice["color"], peice["emoji"],
                                                        oldBoard, peice["moved"])
            elif peice["kind"] == "horse":
                a[peice["x"]][peice["y"]] = Horse(peice["x"], peice["y"], peice["color"], peice["emoji"], a,
                                                  peice["moved"])
                oldBoard[peice["x"]][peice["y"]] = Horse(peice["x"], peice["y"], peice["color"], peice["emoji"],
                                                         oldBoard, peice["moved"])
            elif peice["kind"] == "checker_peice":
                a[peice["x"]][peice["y"]] = checker_peice(peice["x"], peice["y"], peice["color"], peice["emoji"], a,
                                                          peice["moved"],False,False,0,peice["checker_king"])
class Button(object):

    def __init__(self, x, y, image, text):
        # the image of the button, the coordinates of it, the text shown on the button
        self.x, self.y = x, y
        self.image = image
        self.text = text
        self.rect = self.image.get_rect(center=(self.x, self.y))

    def update(self):
        main_font = pg.font.SysFont("Arial", int(50 * height / 1000))
        self.button_text = main_font.render(self.text, True, "white")
        self.text_rect = self.button_text.get_rect(center=(self.x, self.y))
        window.blit(self.image, self.rect)
        window.blit(self.button_text, self.text_rect)

    def check_for_input(self, x, y):
        global btn_lst
        # if the click is on the button, detect which button then promote
        if x in range(self.rect.left, self.rect.right) and y in range(
                self.rect.top, self.rect.bottom):
            if self.text == "queen":
                a[coord[0]][coord[1]] = Queen(coord[0], coord[1], a[coord[0]][coord[1]].color, "♕")
            elif self.text == "bishop":
                a[coord[0]][coord[1]] = Bishop(coord[0], coord[1],a[coord[0]][coord[1]].color,"♗")
            elif self.text == "horse":
                a[coord[0]][coord[1]] = Horse(coord[0], coord[1],
                                              a[coord[0]][coord[1]].color, "♞")
            elif self.text == "rook":
                a[coord[0]][coord[1]] = Rook(coord[0], coord[1],
                                             a[coord[0]][coord[1]].color, "♜")
            btn_lst = []

    def main_menu_check(self, x, y):
        global turn_counter, window, btn_lst, chess
        if x in range(self.rect.left, self.rect.right) and y in range(
                self.rect.top, self.rect.bottom):
            turn_counter = 1
            btn_lst = []
            if self.text == "start":
                chess = True
                ClassicOrientation()
                main()
            elif self.text == "continue chess":
                chess = True
                load("chessSaveState.json")
                main()

            elif self.text == "checkers":
                checkers_classicOrientation()
                main()
            elif self.text == "continue checkers":
                load("checkersSaveState.json")
                main()

def make_buttons():
    global btn_lst
    # makes the buttons and saves them in a list
    button0 = Button(int(width / 2), height_8, button_img, "queen")
    button1 = Button(int(width / 2), height_8 * 3, button_img, "bishop")
    button2 = Button(int(width / 2), height_8 * 5, button_img, "horse")
    button3 = Button(int(width / 2), height_8 * 7, button_img, "rook")
    btn_lst = [button0, button1, button2, button3]

def get_coordinates():
    player = str(pg.mouse.get_pos()).split(", ")
    return int((player[0].split("("))[1]) // width_8, int((player[1].split(")"))[0]) // height_8

def main():
    global x, y, x1, y1, possKing, turn_counter, turn_color, checkmate_check, king_sur, run, chess
    y1, x1 = 0, 0
    x = None
    possKing = False
    checkmate_check = False
    king_sur = False
    window = pg.display.set_mode((width, height), pg.RESIZABLE)
    board(a)

    turn_color = "w" if turn_counter % 2 else "b"

    run = True
    # setting the fps to 60 part 1
    clock = pg.time.Clock()
    while run:
        # setting the fps to 60 part 2
        clock.tick(60)
        # quit the game if the game window is closed
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if chess:
                    save("chessSaveState.json")
                else: save("checkersSaveState.json")
                run = False
            # detecting the mouse click and getting the position
            if event.type == pg.MOUSEBUTTONDOWN:
                if len(btn_lst) > 0:
                    player = str(pg.mouse.get_pos()).split(", ")
                    x2, y2 = int((player[0].split("("))[1]), int(
                        (player[1].split(")"))[0])
                    # checks if the coordinates are within any button
                    i = 0
                    while i < len(btn_lst):
                        btn_lst[i].check_for_input(x2, y2)
                        i += 1
                    turn_color = "b" if turn_counter % 2 else "w"
                    wincheck(turn_color, turn_counter)
                    turn_color = "w" if turn_counter % 2 else "b"
                    update_window()
                elif x == None:

                    x, y = get_coordinates()

                    # no clicks outside the grid
                    try:
                        if x > 7 or y > 7 or a[y][x] in ['⬛', '⬜']:
                            raise Exception
                    except:
                        x = None
                    else:
                        # drawing a box and getting the piece clicked
                        red_box = pg.Rect((x) * width_8, (y) * height_8,
                                          width_8, height_8)
                        pg.draw.rect(window, (125, 0, 0), red_box)
                        check_piece(y, x, a, turn_color)
                        board(a)
                        pg.display.update()
                # moving the piece
                elif x != None:
                    x1, y1 = get_coordinates()

                    # no clicks outside the grid
                    try:
                        if x1 > 7 or y1 > 7:
                            raise ValueError
                    except:
                        # remove all Xs, Os and under_attacks
                        x = None
                        for i in range(len(a)):
                            for j in range(len(a[i])):
                                # remove all Xs, Os and under_attacks
                                if a[i][j] in ['❌', '⚫']:
                                    a[i][j] = de[i][j]
                                elif a[i][j] != de[i][j]:
                                    a[i][j].under_attack = False
                        update_window()
                    else:
                        # player moved
                        if a[y1][x1] in ["❌", '⚫']:
                            # drawing a box and editing the value in the grid
                            green_box = pg.Rect((x1) * width_8,
                                                (y1) * height_8, width_8,
                                                height_8)
                            pg.draw.rect(window, (0, 125, 0), green_box)
                        a[y][x].move(y1, x1)

                        if chess:
                            turn_color = "b" if turn_counter % 2 else "w"
                            wincheck(turn_color, turn_counter)
                            turn_color = "w" if turn_counter % 2 else "b"
                        else:
                            checkers_win_check()
                        x = None
                        board(a)
                        pg.display.update()
            else:
                update_window()
    pg.quit()

def main_menu():
    global width, height, width_8, height_8, run
    run = True
    # setting the fps to 60 part 1
    clock = pg.time.Clock()

    window = pg.display.set_mode((width, height))
    window.blit(wallaper, ((window.get_width() - wallaper.get_width()) // 2 , (window.get_height() - wallaper.get_height()) // 2))

    start_button = Button(int(width / 2), height_8 * 2, button_img, "start")
    continue_button = Button(int(width / 2), height_8 * 3.5, button_img, "continue chess")
    checkers_button = Button(int(width / 2), height_8 * 5, button_img, "checkers")
    checkers_continue_button = Button(int(width / 2), height_8 * 6.5, button_img, "continue checkers")
    btn_lst = [start_button, continue_button, checkers_button, checkers_continue_button]

    k = 0
    while k < len(btn_lst):
        btn_lst[k].update()
        k += 1
    pg.display.update()

    while run:
        # setting the fps to 60 part 2
        clock.tick(60)
        # quit the game if the game window is closed
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            if event.type == pg.MOUSEBUTTONDOWN:
                player = str(pg.mouse.get_pos()).split(", ")
                x, y = int((player[0].split("("))[1]), int((player[1].split(")"))[0])

                i = 0
                while i < len(btn_lst):
                    btn_lst[i].main_menu_check(x, y)
                    i += 1

if __name__ == "__main__":
    main_menu()