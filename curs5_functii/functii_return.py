# # Functiile au posibiliatea de a returna un rezultat folosind cuvantul cheie "return"
#
# # def nume_funct(...):
# #     ...
# #     return ...
# def add_three(a, b, c=10):
#     print(f"Suma este {a+b+c}")
#     return a + b + c
#
# l = [1, 7, -3, 4, 5, 9, 0, 2, -3]
# nr_max = max(l)  # max este o functie care ia un parametru lista si RETURNEAZA cel mai mare element
#
#
# sum_3 = add_three(1, 7, 5)
# print(sum_3)

"""
1. Se citesc doua numere naturale de la tastatura, x si y.
Sa se afiseze toate numerele prime din intervalul [x, y], iar daca nu exista nici un
numar prim in acest interval, sa se afiseze mesajul "Nu exista numere prime in intervalul selectat [x, y]"

Exemplu:
x = 25
y = 50
Se va afisa: 29,  31, 37, 41, 43, 47

x = 25
y = 28
Se va afisa: "Nu exista numere prime in intervalul selectat [25, 28]"
"""

# Functie care verifica daca numarul x (parametru) este prim
# returneaza True - x e prim
# returneaza False - x NU e prim
def is_prime(x):
    for div in range(2, x - 1):
        if x % div == 0:
            # Daca gasim un divizor => x nu e prim => oprim functia, returnam False
            return False
    # Daca am ajuns aici, inseamna ca am terminat bucla for, si NU am gasit nici un divizor
    # Deci, x e prim => returnam True
    return True

# Acest x nu are nici o legatura cu cel din functie
x = int(input("x:\n"))
y = int(input("y:\n"))

for nr in range(x, y):
    if is_prime(nr):
        print(f"Numar prin gasit: {nr}")

