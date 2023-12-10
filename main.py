from abc import ABC, abstractmethod

class Bicikli(ABC):
    def __init__(self, tipus, ar, allapot):
        self.tipus = tipus
        self.ar = ar
        self.allapot = allapot

    @abstractmethod
    def bicikli_informacio(self):
        pass

class OrszagutiBicikli(Bicikli):
    def __init__(self, tipus, ar, allapot, sebesseg):
        super().__init__(tipus, ar, allapot)
        self.sebesseg = sebesseg

    def bicikli_informacio(self):
        return f"Országúti bicikli - Sebesség: {self.sebesseg} km/h"

class HegyiBicikli(Bicikli):
    def __init__(self, tipus, ar, allapot, fokozatok):
        super().__init__(tipus, ar, allapot)
        self.fokozatok = fokozatok

    def bicikli_informacio(self):
        return f"Hegyi bicikli - Fokozatok: {self.fokozatok}"

class Kolcsonzo:
    def __init__(self, nev):
        self.nev = nev
        self.biciklik = []

    def bicikli_hozzaadasa(self, bicikli):
        self.biciklik.append(bicikli)

    def bicikli_torlese(self, bicikli):
        self.biciklik.remove(bicikli)

    def biciklik_listazasa(self):
        for bicikli in self.biciklik:
            print(bicikli.bicikli_informacio())
from datetime import datetime

class Kolcsonzes:
    def __init__(self, bicikli, datum):
        self.bicikli = bicikli
        self.datum = datum

    def kolcsonzes_lemondasa(self):
        if self.datum >= datetime.now().date():
            print("A kölcsönzés lemondása sikeres.")
        else:
            print("A kölcsönzés már nem mondható le.")

    def kolcsonzes_informacio(self):
        print(f"Bicikli: {self.bicikli.bicikli_informacio()}")
        print(f"Dátum: {self.datum}")

def main():
    kolcsonzo = Kolcsonzo("Kis Pista")

    orszaguti_bicikli = OrszagutiBicikli("Országúti", 1000, "Új", 30)
    hegyi_bicikli = HegyiBicikli("Hegyi", 800, "Használt", 21)

    kolcsonzo.bicikli_hozzaadasa(orszaguti_bicikli)
    kolcsonzo.bicikli_hozzaadasa(hegyi_bicikli)

    print("Válasszon műveletet:")
    print("1. Biciklik listázása")
    print("2. Bicikli kölcsönzése")
    print("3. Kölcsönzés lemondása")

    muvelet = input("Művelet kiválasztása: ")

    if muvelet == "1":
        kolcsonzo.biciklik_listazasa()
    elif muvelet == "2":
        bicikli_index = int(input("Válasszon biciklit (1. Országúti vagy 2. Hegyi ): "))
        datum = input("Adja meg a kölcsönzés dátumát (YYYY-MM-DD): ")
        bicikli = kolcsonzo.biciklik[bicikli_index - 1]
        kolcsonzes = Kolcsonzes(bicikli, datetime.strptime(datum, "%Y-%m-%d").date())
        kolcsonzes.kolcsonzes_informacio()
    elif muvelet == "3":
        datum = input("Adja meg a kölcsönzés dátumát (YYYY-MM-DD): ")
        kolcsonzes = Kolcsonzes(None, datetime.strptime(datum, "%Y-%m-%d").date())
        kolcsonzes.kolcsonzes_lemondasa()
    else:
        print("Érvénytelen művelet.")

if __name__ == "__main__":
    main()