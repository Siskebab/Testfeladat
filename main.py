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

orszaguti_bicikli = OrszagutiBicikli(tipus="Országúti", ar=800, allapot="Új")
hegyi_bicikli = HegyiBicikli(tipus="Hegyi", ar=1000, allapot="Használt")


orszaguti_bicikli.display_info()
print("---------")
hegyi_bicikli.display_info()