"""
Clasa Masina
Atribute: marca, culoare, viteza
Metode: start, stop, accelereaza, franeaza
"""

class Masina:

    def __init__(self, marca, culoare):
        self.marca = marca
        self.culoare = culoare
        self.viteza = 0
        self.motor_pornit = False

    def start(self):
        print(f"Masina {self.marca} {self.culoare} a pornit motorul!")
        self.motor_pornit = True

    def stop(self):
        print(f"Masina {self.marca} {self.culoare} a oprit motorul!")
        self.motor_pornit = False

    def accelereaza(self, accelereaza_cu):
        if self.motor_pornit:
            self.viteza += accelereaza_cu
            print(f"Am accelerat la {self.viteza} km/h")
        else:
            print("Nu se poate accelera, nu este pornit motorul!")

    def decelereaza(self, decelereaza_cu):
        if self.motor_pornit:
            self.viteza -= decelereaza_cu
            print(f"Am decelerat la {self.viteza} km/h")
        else:
            print("Nu se poate decelera, nu este pornit motorul!")

jeep = Masina("Jeep", "negru")
jeep.accelereaza(10)  # incerc sa accelerez cu 10km/h
jeep.start()
jeep.accelereaza(10)
jeep.accelereaza(12)
jeep.decelereaza(5)
jeep.accelereaza(40)
jeep.stop()
jeep.accelereaza(12)

marca_masina = input("Ce marca de masina vrei?\n")
culoare_masina = input("Culoare masina:\n")
masina_custom = Masina(marca_masina, culoare_masina)

masina_custom.start()
x = int(input("La cat vrei sa accelerezi?\n"))
masina_custom.accelereaza(x)

honda = Masina("Honda", "verde")
circuit_curse = [jeep, honda]

circuit_dict = {
    "jeep": jeep,
    "honda": honda
}

