from abc import ABC, abstractmethod

class Bicikli(ABC):
    def __init__(self, tipus, ar, allapot):
        self.tipus = tipus
        self.ar = ar
        self.allapot = allapot

    @abstractmethod
    def display_info(self):
        pass


class OrszagutiBicikli(Bicikli):
    def __init__(self, tipus, ar, allapot):
        super().__init__(tipus, ar, allapot)


    def display_info(self):
        print(f"Országúti bicikli - Tipus: {self.tipus}, Ár: {self.ar}, Állapot: {self.allapot}")


class HegyiBicikli(Bicikli):
    def __init__(self, tipus, ar, allapot):
        super().__init__(tipus, ar, allapot)


    def display_info(self):
        print(f"Hegyi bicikli - Tipus: {self.tipus}, Ár: {self.ar}, Állapot: {self.allapot}")


class Kolcsonzo:
    def __init__(self, nev):
        self.nev = nev
        self.biciklik = []

    def add_bicikli(self, bicikli):
        self.biciklik.append(bicikli)

    def display_info(self):
        print(f"Kölcsönző neve: {self.nev}")
        print("Biciklik:")
        for bicikli in self.biciklik:
            bicikli.display_info()
            print("---------")


orszaguti_bicikli = OrszagutiBicikli(tipus="Országúti", ar=800, allapot="Új")
hegyi_bicikli = HegyiBicikli(tipus="Hegyi", ar=1000, allapot="Használt")

kolcsonzo = Kolcsonzo(nev="Kerékpárkölcsönző kft.")
kolcsonzo.add_bicikli(orszaguti_bicikli)
kolcsonzo.add_bicikli(hegyi_bicikli)

kolcsonzo.display_info()