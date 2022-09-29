"""
Mostenire: clasa copil mosteneste atributele si metodele clasei parinte
(pe care le poate suprascrie sau le poate lasa la fel)
"""

class Person:
    def __init__(self, nume, varsta, oras):
        self.nume = nume
        self.varsta = varsta
        self.oras = oras

    def descrie(self):
        print(f"Salut, pe mine ma cheama {self.nume}, am {self.varsta} ani si sunt din {self.oras}")

class Child(Person):
    def __init__(self, nume, varsta, oras, nume_scoala, numar_frati):
        super(Child, self).__init__(nume, varsta, oras)
        self.nume_scoala = nume_scoala
        self.numar_frati = numar_frati

class Adult(Person):
    def __init__(self, nume, varsta, oras, e_angajat, are_copii):
        super(Adult, self).__init__(nume, varsta, oras)
        self.e_angajat = e_angajat
        self.are_copii = are_copii

    def schimba_salariu(self, salariu_nou):
        self.salariu = salariu_nou

ionut = Child("Ionut", 12, "Cluj", "T. Popoviciu", 2)
ionel = Adult("Ionel", 32, "Timisoara", False, True)
maria = Child("Maria", 9, "Alba", "Whatever", 0)

lista_persoane = [ionut, ionel, maria]
for persoana in lista_persoane:
    persoana.descrie()
    # persoana.schimba_salariu(1000)

