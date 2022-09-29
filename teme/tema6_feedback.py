"""
Atribute de clasa vs atribute de instanta.
"""

class Factura:
    # atribut de clasa - poate fi schimbat folosind numele clasei
    # Factura.seria = ceva
    seria = "XYZ"

    def __init__(self, numar_factura):
        # atribut de instanta (obiect)
        # poate fi schimbat per obiect, folosind varibila obiectului
        # obj.numar = 100
        self.numar = numar_factura

    def descrie(self):
        print(f"Factura {self.seria} {self.numar}")


f1 = Factura(100)
f2 = Factura(150)

f1.descrie()
f2.descrie()

Factura.seria = "ABC"

f1.descrie()
f2.descrie()
print("_" * 120)


class FacturaSmart:
    seria = "ABC"
    # tinem acest atribut aici, deoarece vrem sa auto-incrementam numarul facturii, si atunci il tinem per clasa
    numar = 0
    # nu are sens sa tinem total aici, deoarece nu e un atribut care tine de clasa, ci de fiecare factura in sine
    # total = 0

    def __init__(self):
        FacturaSmart.numar += 1
        self.numar = FacturaSmart.numar
        self.total = 0

    def descrie(self):
        print(f"Factura {self.seria} {self.numar}")


fs1 = FacturaSmart()
fs2 = FacturaSmart()
fs3 = FacturaSmart()

fs1.descrie()
fs2.descrie()
fs3.descrie()


"""
Constante vs variabile (pe clasa).
"""
# in Python, variabilele se scriu cu litere mici
# iar constantele se scriu cu litere MARI

class AltaFactura:

    SERIA = "ABC"  # pun litere mari ca sa exprim faptul ca aceasta valoare NU TREBUIE SCHIMBATA
    PI = 3.14
    ZILELE_SAPTAMANII = {"luni", "marti"}
    # SERIA = "XYZ"

"""
Metode care modifica vs metode care nu modifica (cont: debitare / creditare / interogare sold)
"""
print("_" * 120)
class ContIBAN:

    def __init__(self, iban, sold):
        self.iban = iban
        self.sold = sold

    def debitare(self, suma):
        self.sold -= suma
        return self.sold

    def creditare(self, suma):
        pass

    def descrie(self):
        print(f"Aveti in contul {self.iban} suma de {self.sold} RON.")


cont = ContIBAN("dhfiou2309r4u32rn", 120)
cont.descrie()
cont.debitare(30)  # Retrag 30 lei
cont.descrie()


class Angajat:

    def __init__(self, nume, salariu_lunar):
        self.nume = nume
        self.salariu_lunar = salariu_lunar

    def salariu_anual(self):
        return self.salariu_lunar * 12

    def descrie(self):
        print(f"Angajatul {self.nume} are {self.salariu_lunar} salariu lunar,"
              f"respectiv {self.salariu_anual()} salariu anual!")

    def marire(self, procent):
        self.salariu_lunar += self.salariu_lunar*procent/100
        # self.salariu_anual = self.salariu_lunar * 12
        return self.salariu_lunar


ionica = Angajat("Ionica", 1000)
ionica.descrie()
ionica.marire(10)
ionica.descrie()


"""
Clasa TodoList
 
Atribute: todo (dict, cheia e numele taskului, valoarea e descrierea)
La inceput nu avem taskuri, dict e gol si nu avem nevoie de constructor

Metode:
adauga_task(nume, descriere) - se va adauga in dict
finalizeaza_task(nume) - se va sterge din dict
afiseaza_todo_list() - doar cheile
afiseaza_detalii_suplimentare(nume_task) - in f de numele taskului, printam detalii suplimentare
daca taskul nu e in todo list, intrebam utilizatorul daca vrea sa il adauge.
Daca acesta raspunde nu - la revedere
daca raspunde da - il cerem detalii task si salvam nume+detalii in dict
"""

class TodoList:

    def __init__(self):
        self.todo = {}

    def adauga_task(self, nume, descriere):
        if nume not in self.todo:
            self.todo[nume] = descriere
        else:
            print("Aveti deja un task cu acest nume, incercati sa folositi un alt nume, unic")

    def finalizeaza_task(self, nume):
        if nume in self.todo:
            del self.todo[nume]
            print("Felicitari, ai finalizat taskul!")
        else:
            print("Nu am gasit taskul cautat!")

    def afiseaza_todo_list(self):
        print(self.todo.keys())

    def afiseaza_detalii_suplimentare(self, nume_task):
        if nume_task in self.todo:
            print(self.todo[nume_task])
        else:
            # nu exista, oferim posibilitatea sa il adaugam
            adauga = input("Taskul nu exista, vrei sa il adaugi? da/nu")
            if adauga == "da":
                detalii_task = input("Introdu detalii task:")
                self.adauga_task(nume_task, detalii_task)
            elif adauga == "nu":
                print("La revedere!")
            else:
                print("Raspuns invalid. Incearca din nou.")


print()
print("_" * 120)
tl = TodoList()
tl.afiseaza_todo_list()
tl.adauga_task("tema", "Fa tema pentru cursul 6")
tl.adauga_task("video", "Urmareste video despre Github")
tl.afiseaza_detalii_suplimentare("curatenie")
tl.afiseaza_todo_list()
