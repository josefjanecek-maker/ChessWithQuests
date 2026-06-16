from figurka import Figurka

class Pesak(Figurka):
    def __init__(self, barva):
        if barva == 0:
            vektory = [[-1, 0]]
            vektory_utoku = [[-1, -1], [-1, 1]]
        else:
            vektory = [[1, 0]]
            vektory_utoku = [[1, -1], [1, 1]]
        super().__init__("Pěšák", barva, vektory_utoku, vektory)
        self.skok = False