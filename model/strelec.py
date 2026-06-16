from figurka import Figurka

class Strelec(Figurka):
    def __init__(self, barva):
        vektory = [
            [-1, -1], [-1, 1],
            [1, -1],  [1, 1]
        ]
        vektory_utoku = vektory
        super().__init__("Střelec", barva, vektory_utoku, vektory)
        self.skok = False