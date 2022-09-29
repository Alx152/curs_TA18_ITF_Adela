import math
from abc import ABC

"""
Clasele Abstracte trebuie sa mosteneasca o clasa speciala numita ABC
iar metodele lor trebuie sa aiba o singura linie, care ridica o exceptie numita NotImplementedError
"""
class FormaGeometrica(ABC):

    def aria(self):
        raise NotImplementedError

    def perimetru(self):
        raise NotImplementedError


class Cerc(FormaGeometrica):

    def __init__(self, raza):
        self.__raza = raza

    def aria(self):
        return self.__raza ** 2 * 3.14

    def perimetru(self):
        return self.__raza * 3.14

    # Getter
    def get_raza(self):
        return self.__raza

    # Setter
    def set_raza(self, raza_noua):
        if raza_noua > 0:
            self.__raza = raza_noua
            print("Am schimbat raza!")
        else:
            print("Raza nu poate fi negativa!")

    def del_raza(self):
        print("Stergem raza, adica o facem egala cu 0.")
        self.__raza = 0

    radius = property(get_raza, set_raza, del_raza)


class Patrat(FormaGeometrica):

    def __init__(self, latura):
        self.__latura = latura

    def aria(self):
        return self.__latura ** 2

    def perimetru(self):
        return self.__latura * 4

    # Putem folosi orice nume vrem noi pentru atributul public care "inveleste" atributul nostru privat
    # DAR cel mai logic este sa folosim numele atributului privat, fara underscores
    # Getter, numele pe care il folosim la aceasta metoda este chiar atributul public (pe care il expunem)
    @property
    def cartof(self):
        return self.__latura

    # Setter, trebuie ca metoda sa aiba acelasi nume ca si getterul, si trebuie "decorat" cu @nume atribut.setter
    @cartof.setter
    def cartof(self, new_lat):
        self.__latura = new_lat
        # Putem returna ceva aici, dar nu ar trebui sa facem asta, deoarece nu putem prelua return value dintr-o asignare
        return self.__latura

     # Deleter: metoda din nou are acelasi nume, si trebuie "decorat" cu @ nume atribut.deleter
    @cartof.deleter
    def cartof(self):
        self.__latura = 0


class Dreptunghi(FormaGeometrica):

    def __init__(self, lungime, latime):
        self.lungime = lungime
        self.latime = latime

    def aria(self):
        return self.lungime * self.latime

    def perimetru(self):
        return 2 * (self.lungime + self.latime)

    def diagonala(self):
        return math.sqrt(self.lungime**2 + self.latime**2)


class Triunghi(FormaGeometrica):

    def __init__(self, lat1, lat2, lat3):
        self.l1 = lat1
        self.l2 = lat2
        self.l3 = lat3

    def aria(self):
        return self.l1 * self.l2 * self.l3

    def perimetru(self):
        return self.l1 + self.l2 + self.l3

    def inaltimea(self):
        return self.l1 * self.l2 / self.l3


# # Pot crea FormaGeometrica, dar nu are sens (si nu ar trebui sa fac asta oricum)
# forma = FormaGeometrica()
# # print(forma.aria())  # va da eroare
# # print(forma.perimetru())  # va da eroare
#
# lista_forme_geometrice = [
#     Cerc(12),
#     Triunghi(3, 4, 5),
#     Dreptunghi(12, 14),
#     Cerc(7),
#     Dreptunghi(5, 9),
#     Dreptunghi(6, 6)
# ]
#
# for fg in lista_forme_geometrice:
#     print(f"Aria {fg.aria()} si perimetrul {fg.perimetru()}")

"""
Folosim mostenire atunci cand avem atribute si metode comune pe care vrem sa le tinem in clasa parinte.
Folosim abstractizare atunci cand vrem ca mai multe clase copil sa implementeze aceleasi metode,
dar fiecare are o implementare diferita.

La mostenire nu avem nici un fel de "obligatii" fata de clasa parinte.
La abstractizare, suntem obligati sa implementam metodele respective in toate clasele copil.
"""

"""
Zicem ca metodele aria si perimetru sunt POLIMORFICE
Adica ele fac chestii diferite, desi arata la fel (adica se apeleaza cu acelasi nume)
"""

cerc_mic = Cerc(5)
print(cerc_mic.get_raza())
cerc_mic.set_raza(-7)
cerc_mic.set_raza(7)
print(cerc_mic.get_raza())

print(f"Folosind property, putem acum face direct asa: {cerc_mic.radius}")
cerc_mic.radius = 12
print(cerc_mic.radius)
del cerc_mic.radius
print(cerc_mic.radius)


patrat = Patrat(13)
print(patrat.cartof)
patrat.cartof = 5
print(patrat.cartof)
