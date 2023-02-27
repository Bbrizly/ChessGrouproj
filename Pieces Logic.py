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

class Pawn:
    def __init__(self,color:str):
        self.color = color
        self.moved = False
        #once moved can only go up in ones
    def movement(self):
        self.moved = True
        # goes through each grid box until occupied or end of board
        # ^ run 3 times (front, diagonally front)
        # run ifs for color of piece that occupies box
        if self.color == "w":
            print("white")
        else:
            print("black")
        print("moves up twice in first move, ")

#queen and king