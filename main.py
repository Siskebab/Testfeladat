class Etel:
    def __init__(self,nev,ar):
        self.nev = nev
        self.ar = ar

class Restaurant:
    def __init__(self, menuitems, etteremnev):
        self.menuitems = menuitems
        self.etteremnev = etteremnev
    def __str__(self):
        return f"Az étterem neve {self.etteremnev}"

my_restaurant = Restaurant(menuitems: [], etteremnev: "kisbojtár")
print(my_restaurant)
my_etel = Etel(nev:"leves", ar: 300)
