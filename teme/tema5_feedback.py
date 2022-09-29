import math

"""
IMPORTANT!!
"""
# ATENTIE: in general nu folosim parametrii in functii direct din restul programului,
# ci ii pasam ca si argumente pentru functia noastra, deoarece functiile trebuie sa fie REUTILIZABILE
# si de asemenea sa nu depinda (in limita posibilitatilor) de ceea ce se intampla in jurul lor (adica sa fie atomice)

print("Exemplu de functie fara parametri, care se bazeaza pe nume de variabile externe")
def min_max():
    if a > b:
        return a
    else:
        return b

a = 7
b = 12
print(f"Daca vreau sa aflu maximul dintre a si b, e simplu: {min_max()}")
x = 22
y = 100
print("Dar cum fac acum sa aflu maximul dintre x si y???")


"""
IMPORTANTA: numele functiilor
Folosim mereu VERBE, deoarece functia = actiune.
In general: 
    is_ceva pentru cele care returneaza True/False (verifica o conditie)
    get_ceva pentru cele care returneaza valori numerice/string
    compute_ceva pentru cele care doar calculeaza o valoare dar nu o returneaza
Putem folosi si nume mai scurte, dar trebuie sa fie bine gandite incat sa stim ce face functia din nume.
Gen functiile din Python: min, max, len, sum, print, etc.
Ex:
is_odd -> (traducere este par) -> returneaza True daca nr e par, False altfel
get_char_count -> returneaza un numar de caractere
"""

"""
If-elif nu are nevoie neaparat de else.
Atunci cand ajungem la return, codul se va opri, deci putem folosi asta in avantajul nostru.
Urmatoarele functii sunt identice dpdv al executiei.
"""
def max_v1(a, b):
    if a > b:
        return a
    elif b > a:
        return b
    else:
        return 0  # sunt egale

def max_v2(a, b):
    if a > b:
        return a
    elif b > a:
        return b
    return 0  # sunt egale

def max_v3(a, b):
    if a > b:
        return a
    if b > a:
        return b
    return 0  # sunt egale

"""
Return value: daca nu returnam nimic dintr-o functie, se va "returna" automat valoarea None (null, inexistent, nimic)
"""
def f1():
    print("functie care nu returneaza nimic")

print(f1())  # va afisa None

# echivalent cu
x = f1()
print(x)  # va afisa None, deoarece x e None, pentru ca functia f1 nu a returnat nimic

# Rezolvari TEMA
"""
1.Funcție care să calculeze și să returneze suma a două numere
"""
# ATENTIE: aici suprascriem functia originala sum din Python
# def sum(a, b):
#     return a + b

def sum_of(a, b):
    # ATENTIE: aici suprascriem prin variabila sum, functia sum din Python
    # sum = a + b
    # return sum
    return a + b


"""
2. Funcție care sa returneze TRUE dacă un număr este par, FALSE pt impar
"""
# Varianta 1
def is_odd_v1(nr):
    if nr % 2 == 0:
        return True
    else:
        return False

# varianta 2
def id_odd_v2(nr):
    return nr % 2 == 0

"""
In general, daca avem:
def functie():
    if cond:
        return True
    else:
    return False
    
Putem inlocui cu
def functie():
    return conditie
"""


"""
3. Funcție care returnează numărul total de caractere din numele tău complet.
(nume, prenume, nume_mijlociu)
"""
# Solutie care gestioneaza si persoanele fara nume mijlociu
def get_name_chars_cnt(first_name, last_name, middle_name=""):
    return len(first_name) + len(last_name) + len(middle_name)


"""
4. Funcție care returnează aria dreptunghiului
"""
def get_rectangle_area(length, width):
    return length * width


"""
5. Funcție care returnează aria cercului
"""
def get_circle_area(radius):
    return math.pi * radius**2


"""
6. Funcție care returnează True dacă un caracter x se găsește într-un string dat
și False dacă nu se găsește.
"""
# Fara sa folosim find / index / in
def is_char_in_str(chr, str):
    for c in str:
        if c == chr:
            return True
    return False


"""
7. Funcție fără return, primește un string și printează pe ecran:
● Nr de caractere lower case este x
● Nr de caractere upper case exte y
"""
def print_case_counters(str):
    upper_cnt = 0
    lower_cnt = 0

    for c in str:
        if c.isupper():
            upper_cnt += 1
        elif c.islower():
            lower_cnt += 1

    print(f"Nr de caractere lower case este {lower_cnt}")
    print(f"Nr de caractere upper case este {upper_cnt}")


"""
8. Funcție care primește o LISTA de numere și returnează o LISTA doar cu
numerele pozitive
"""
# [-3, 4, 6, 2, -9, 12, -7, 0]
# return [4, 6, 2, 12]
def get_positive_numbers(numbers):
    positive_nrs = []
    for nr in numbers:
        if nr > 0:
            positive_nrs.append(nr)

    return positive_nrs


"""
9. Funcție care nu returneaza nimic. Primește două numere și PRINTEAZA
● Primul număr x este mai mare decat al doilea nr y
● Al doilea nr y este mai mare decat primul nr x
● Numerele sunt egale.
"""


def print_highest_number(a, b):
    if a > b:
        print(f'Primul număr {a} este mai mare decat al doilea nr {b}')
    elif a < b:
        print(f'Al doilea nr {b} este mai mare decat primul nr {a}')
    else:
        print('Numerele sunt egale.')

print_highest_number(12, 5)
print_highest_number(5, 12)
print_highest_number(12, 12)

"""
10. Funcție care primește un număr și un set de numere.
● Printeaza ‘am adaugat numărul nou în set’ + returnează True
● Printeaza ‘nu am adaugat numărul în set. Acesta există deja’ +
returnează False
"""


def add_to_set(number, s):
    if number in s:
        print('Nu am adaugat numărul în set. Acesta există deja')
        return False
    else:
        s.add(number)
        print(f'Am adaugat numărul nou în set {number}')
        return True


"""
Mereu RULATI si TESTATI codul cu mai multe valori!
"""
test_set = {1, 2, 3}
# print ( functie() ) => va printa valoarea returnata de functie
print(add_to_set(3, test_set))
print(add_to_set(7, test_set))
print(add_to_set(7, test_set))
