"""
Encapsulation (Incapsulare) - mentinerea atributelor si a metodelor intr-o clasa pe nivele de vizibilitate

Privat - incep cu dublu underscore => nu se pot accesa din afara clasei in care au fost definite
Protected - incep cu un singur underscore => se pot accesa doar din clasele copil
Public - toate celelalte => se pot accesa de oriunde
"""

class FacturaSmart:
    __seria = "ABC"  # privat
    _numar = 0  # protected

    def __init__(self):
        FacturaSmart._numar += 1
        self.numar = FacturaSmart._numar
        self.total = 0

    def descrie(self):
        print(f"Factura {self.__seria} {self.numar}")

class FacturaSmartChild(FacturaSmart):
    def __init__(self):
        super(FacturaSmartChild, self).__init__()
        print(f"Din clasa copil putem accesa atributele de tip protected {self._numar}")
        # print(f"Dar nu si pe cele de tip privat {self.__seria}")  # va da eroare


fs = FacturaSmart()
# print(fs.__seria)  # eroare
print(fs.numar)  # atributul numar este public
# print(FacturaSmart.__seria)  # eroare

fsc = FacturaSmartChild()
# print(fsc.__seria)  # eroare
print(fsc._numar)  # protected, dar eu il accesez din clasa copil
