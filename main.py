class Etel:

    def __init__(self):
        self._nev = ""
        self._ar = 0

    @property
    def ar(self) -> int:
        return self._ar

    @ar.setter
    def ar(self, ar: int):
        if ar < 0 or ar > 100000:
            print("Nem megfelelő ár")
        else:
            self._ar = ar

    @property
    def nev(self) -> str:
        return self._nev

    @nev.setter
    def nev(self, ujnev):
        self._nev = ujnev


class Restaurant:

    def __init__(self, menuitems: [Etel], etteremnev: str):
        self.menuitems = menuitems
        self.etteremnev = etteremnev

    def __str__(self):
        return f"Az étterem neve {self.etteremnev}"

    def __add__(self, other):
        if isinstance(other, Etel):
            self.menuitems.append(other)
        else:
            print("Nem Étel")

    def getmenuitems(self):
        for menuitem in self.menuitems:
            print(f"{menuitem.nev}.................{menuitem.ar} Ft")


my_restaurant = Restaurant([], "Kisbojtár")
my_restaurant.getmenuitems()

for i in range(2):
    etel_neve = input("Add meg az étel nevét: ")
    etel_ara = int(input("Add meg az étel árát: "))
    etel_uj = Etel()
    etel_uj.nev = etel_neve
    etel_uj.ar = etel_ara
    my_restaurant + etel_uj


my_restaurant.getmenuitems()

print(my_restaurant)