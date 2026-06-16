import time

class GameTimer:
    def __init__(self, cas_hrac):
        self.cas_hrac = cas_hrac

    def nutuj_cas(self):
        if self.cas_hrac > 0:
            self.cas_hrac -= 1

    def pocitej_cas(self, hrac, sekund):
        self.cas_hrac -= sekund
        print(f"Zbývající čas: {self.cas_hrac} s")