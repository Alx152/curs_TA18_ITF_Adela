# OOP - object-oriented programming
# clasa - modeleaza lumea reala prin obiecte

class Patrat:
    # aici suntem in clasa Patrat

    # atribute (fields)
    # un atribut este doar o variabila care apartine clasei
    latura = 0

    # metode
    # metodele sunt functii care apartin clasei
    def aria(self):
        return self.latura * self.latura


# obiect = o instanta a unei clase;
# daca privim clasa ca pe un matrita, atunci patrat_mic este un obiect facut din aceasta matrita
patrat_mic = Patrat()


class Om():

    nume = ""
    prenume = ""
    inaltime = 0.0
    varsta = 0

    # Constructor: o metoda SPECIALA prin care putem da valori initiale obiectelor noastre
    def __init__(self, name, firstname, height, age):
        self.nume = name
        self.prenume = firstname
        self.inaltime = height
        self.varsta = age

    def say_hello(self):
        print(f"Hello, my name is {self.nume}, {self.prenume} and I'm {self.varsta} years old!")

    def say_hello_to(self, alt_om):
        print(f"Hello, {alt_om.nume} {alt_om.prenume}! Eu sunt {self.nume} {self.prenume}!")


adela = Om("Neacsu", "Adela", 1.80, 31)
alexandra = Om("Dancovici", "Alexandra", 1.70, 30)

# say_hello(adela, ...)
adela.say_hello()

# say_hello(alexandra, ...)
# La momentul rularii, self <- alexandra
alexandra.say_hello()

# Metoda say_hello_to se va apela cu valorile (adela, alexandra)
# Deci self va fi adela, iar alt_om va fi alexandra
adela.say_hello_to(alexandra)

lavinia = Om("Manolea", "Lavinia", 1.70, 30)
lavinia.say_hello()
lavinia.say_hello_to(adela)
lavinia.say_hello_to(alexandra)

# lst este de fapt un obiect, iar `list` este o clasa
lst = list()
# append este o metoda a clasei list
lst.append(12)
print(lst)

# Constructorul clasei list va fi apelat acum cu un parametru optional,
# prin care noi punem niste valori initiale in lista
lst2 = list([1, 4, 7])
lst2.append(12)
print(lst2)
