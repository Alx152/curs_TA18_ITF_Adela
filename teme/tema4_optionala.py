"""
11.
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []
Iterati prin lista alte_numere
Populati corect celelalte liste
Afisati cele 4 liste la final
"""

"""
Indicii:
- folosim o structura repetitiva pentru a lua fiecare element din lista (care?)
- pentru fiecare element, trebuie sa facem 2 verificari:
    - DACA este par sau impar
    - DACA este negativ sau pozitiv (putem considera 0 ca fiind pozitiv)
    
Rezultatul final ar trebui sa fie testat de assert-uri

"""
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []

# scrie codul aici

# termina de scris codul aici, acum se fac verificari
assert numere_pare == [2, 12, -6, -4], "Rezultat gresit, nu ai gasit corect toate numerele pare"
assert numere_impare == [-5, 7, 9, 3, 1, 3], "Rezultat gresit, nu ai gasit corect toate numerele impare"
assert numere_pozitive == [7, 2, 9, 12, 3, 1, 3], "Rezultat gresit, nu ai gasit corect toate numerele pozitive"
assert numere_negative == [-5, -6, -4], "Rezultat gresit, nu ai gasit corect toate numerele negative"


print("=" * 120)
"""
12.
Aceeasi lista
Ordonati crescator lista fara sa folositi sort
Va puteti inspira vizual de aici
https://www.youtube.com/watch?v=lyZQPjUT5B4
"""

"""
Indicii: algoritmul de sortare prezentat in video se numeste Bubble Sort: https://en.wikipedia.org/wiki/Bubble_sort
Practic, se itereaza prin lista care trebuie sortata si se compara elementul curent cu urmatorul din lista.
Daca elementul curent e mai mare decat urmatorul, se face swap (cele 2 elemente schimba locul).

Exemplu pasi de rulare pentru lista: [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]

1. elementul curent e -5, care e mai mic decat 7, mergem mai departe
2. elementul curent e 7, care e mai mare decat 2, facem swap
3. lista e acum [-5, 2, 7, 9, 12, 3, 1, -6, -4, 3]
4. elementul curent e 7, care e mai mic decat 9, mergem mai departe
5. elementul curent e 9, care e mai mic decat 12, mergem mai departe
6. elementul curent e 12, care e mai mare decat 3, facem swap
7. lista e acum [-5, 2, 7, 9, 3, 12, 1, -6, -4, 3]
... etc

ATENTIE: nu e suficient sa parcurgem lista o singura data, va trebui sa o parcurgem ori de cate ori este nevoie pana cand
nici un element nu e mai mare decat urmatorul (adica putem zice ca e sortata).

"""
numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_sortate = sorted(numere)
# scrie codul aici, te rog NU FOLOSI si NU MODIFICA in nici un fel lista numere_sortate

# termina de scris codul aici, acum se fac verificari
assert numere == numere_sortate


"""
13.
Ghicitoare de numar
numar_secret = Generati un numar random intre 1 si 30
Numar_ghicit = None
Folosind un while
   User alege un numar
   Programul ii spune:
Nr secret e mai mare
Nr secret e mai mic
Felicitari! Ai ghicit!
"""

"""
Indicii:
 - pentru generarea unui numar aleator ai nevoie de o librarie numita random, 
 si mai exact de functia randint pe care o ofera aceasta librarie: https://www.w3schools.com/python/ref_random_randint.asp
 - rularea se face intr-o bucla while deoarece nu putem stii din cate incercari va ghici userul
 - conditia se opreste atunci cand e ghicit numarul ales de calculator
"""

"""
14. 
Alegeti un numar de la tastatura
Ex:7
Scrieti un program care sa genereze in consola urmatoarea piramida
1
22
333
4444
55555
666666
7777777

Ex:3
1
22
333
"""

"""
Indicii:
 - folosim o structura repetitiva cu numar stiut de pasi (for ... range)
 - functia print are un parametru numit sep (separator) care in mod normal este spatiu " "
 - functia print are un parametru numit end, care in mod normal e newline
 - cand inmultim un string cu un numar x, se afiseaza acel string de x ori 
"""


"""
15.
tastatura_telefon = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
  [0]
]
Iterati prin lista 2d
Printati ‘Cifra curenta este x’
(hint: nested for - adica for in for)
"""

"""
Indicii: 
 - putem face atat cu for each, cat si cu for simplu
 - for each este mai simplu in cazul de fata
 - la primul for, fiecare element va fi o lista
"""