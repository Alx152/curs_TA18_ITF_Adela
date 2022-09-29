"""
Clasa Locuinta:
Atribute: tip (apartament, casa), numar camere, suprafata, pret, numar locatari
Metode: schimba_pret, schimba_nr_locatari
"""

class Locuinta:

    TIPURI_LOCUINTE = ["apartament", "casa"]

    def __init__(self, tip, nr_camere, suprafata, pret):
        if tip in self.TIPURI_LOCUINTE:
            self.tip = tip
        else:
            print(f"Nu ati ales un tip de locuinta corect! Locuinta creata acum va fi automat apartament")
            self.tip = "apartament"
        self.nr_camere = nr_camere
        self.suprafata = suprafata
        self.pret = pret
        self.nr_locatari = 0

    def schimba_pret(self, noul_pret):
        print(f"Locuinta era {self.pret}, acum este {noul_pret}")
        self.pret = noul_pret

    def schimba_nr_locatari(self, nr_locatari):
        print(f"Locuiau {self.nr_locatari} aici, acum locuiesc {nr_locatari}")
        self.nr_locatari = nr_locatari


apartament = Locuinta("apartament", 4, 65.5, 120000)
print(f"Apartamentul cu {apartament.nr_camere} camere "
      f"are o suprafata de {apartament.suprafata} mp "
      f"si se vinde cu {apartament.pret} euro!")