#!/usr/bin/env python3

import random

class Kostka:
    def __init__(self, pocetSten=6):
        self.pocetSten = pocetSten

    def hod(self):
        return random.randint(1, self.pocetSten)


if__main__=="__name__"

    k1=Kostka()
    k2=Kostka(12)
    k3=Kostka(18)

    print(k2.hod())
    print(k1.hod())
    print(k3.hod())
