# Základní třída pro všechny šachové figurky

class Figurka:
    def __init__(self, nazev, barva, vektory_utoku, vektory):
        self.nazev = nazev
        self.vektory_utoku = vektory_utoku
        self.barva = barva
        self.vektory = vektory
        self.pozice = None

    def get_pozice(self, seznam):
        # Vrátí aktuální pozici figurky
        return self.pozice

    def posun_figurky(self, seznam):

        if seznam and len(seznam) == 2:
            if self.pozice is not None:
                novy_radek = self.pozice[0] + seznam[0]
                novy_sloupec = self.pozice[1] + seznam[1]
                self.pozice = [novy_radek, novy_sloupec]
        return self.pozice

    def __str__(self):
        barva_text = "bílá" if self.barva == 0 else "černá"
        return f"{self.nazev} ({barva_text}) na {self.pozice}"