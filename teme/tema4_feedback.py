# """
# IMPORTANT: denumire variabile
# """
# # pentru indici numerici, folosim nume adecvate (de obicei i, idx, sau index)
# dogs = ['Ares', 'Bobi', 'Pluto', 'Goofy']
# for dog in range(len(dogs)):  # 0, 1, 2, ...
#     print(dog)  # dog va fi 0, 1, 2, 3, deci numele nu prea are sens
#     print(dogs[dog])  # nu are sens sa zicem dogs[dog], dogs[idx] ar avea mai mult sens
#
# # daca avem in schimb iterare direct prin colectie, putem folosi SINGULARUL de la numele colectiei
# for dog in dogs:
#     print(f"{dog} likes to bark!")
#
# # colectiile au nume plurale, elementele lor luate individual au nume singulare
# cars = ["Volvo", "Audi", "BMW"]  # asa DA
# car = ["Volvo", "Audi", "BMW"]  # asa NU, car este o lista, si nu se intelege asta din nume
#
# number = 27  # ok
# numbers = 27  # asa NU, avem un singur numar
#
# car = len(cars)  # NU, lungimea e un numar
# cars_length = len(cars)  # DA, alte nume ok ar fi cars_cnt, cars_len, n
#
# """
# For-else fara break nu isi are rostul
# """
# dogs = ['Ares', 'Bobi', 'Pluto', 'Goofy']
# for dog in dogs:
#     print(dogs)
# else:
#     print("Ce se printeaza aici se va printa si daca nu folosim deloc else, deoarece nu avem niciunde break")
# print("Iar daca folosim else, poate deveni confusing deoarece instructiunea de pe else se va executa intotdeauna")


""""1.
Avand lista
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']

Folositi un for ca sa iterati prin toata lista si sa afisati
‘Masina mea preferata este x’
Faceti acelasi lucru cu un for each
Faceti acelasi lucru cu un while
"""
# for - folosim range
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
for idx in range(len(masini)):
    print(f"{idx}: Masina mea preferata este {masini[idx]}")
# for each - folosim for ... in ...
for masina in masini:
    print(f"Masina mea preferata este {masina}")
# while - avem nevoie de conditie de oprire
cnt = 0
while cnt != len(masini):
    print(f"Masina mea preferata este {masini[cnt]}")
    cnt += 1

print("-"*100)
"""2.
Aceeasi lista
Folositi un for
In for
   Modificati elementele din lista astfel incat sa fie scrie cu majuscule, exceptand primul si ultimul
Printati varianta finala a listei
"""
# # Important: elementele din lista trebuie suprascrise
# for idx in range(1, len(masini) - 1):
#     masini[idx] = masini[idx].upper()
# print(masini)
#
# # Daca folosim for each ca mai jos, NU SE MODIFICA NIMIC DIN LISTA
# # for masina in masini[1:-1]:
# #     masina = masina.upper()
# # print(masini)
#
# # ENUMERATE - functie care ne da la fiecare pas indice + valoare
# for idx, masina in enumerate(masini[1:-1]):
#     print(idx, masina)
#     masini[idx] = masina.upper()
# print(masini)
#
# print("-"*100)
# """3.
# Aceeasi lista,
# Vine un cumparator care doreste sa cumpere un Mercedes
# Iterati prin ea prin for each
# Daca masina e mercedes (if)
#    Printam ‘am gasit masina dorita de dvs’
#    Iesim din ciclu folosind un cuvant cheie care face acest lucru
# Altfel
#    Printam Am gasit masina X. Mai cautam
#
# La final, daca nu exista masina cautata, afisam "Nu am gasit nici un Mercedes"
# """
# masina_dorita = "MERCEDES"
# for masina in masini:
#     if masina == masina_dorita:
#         print("Am gasit ce cautati!")
#         break
#     else:
#         # Daca masina curenta nu este cea dorita
#         print(f"Am gasit {masina}. Mai cautam!")
# else:
#     # Else de la for: aici se va ajunge DOAR DACA nu se ajunge deloc la break, adica daca nu se gaseste masina
#     print(f"Nu am gasit nici o {masina_dorita}")
#
#
# """4.
# Aceasi lista
# Vine un cumparator bogat dar indecis. Ii vom prezenta toate masinile cu exceptia Trabant si Lastun.
# Daca masina e Trabant sau Lastun
#    Folositi un cuvant cheie care sa dea skip la ce urmeaza
# Printati S-ar putea sa va placa masina x
# """
# for masina in masini:
#     if masina == 'Trabant' or masina == 'Lastun':
#         continue
#     print(f"S-ar putea sa va placa {masina}")
#
# """5.
# Modernizati parcul de masini
# Creati o lista goala, masini_vechi
# Iterati prin masini
# Cand gasiti Lastun sau Trabant:
# Salvati aceste masini in masini_vechi
# Suprascrieti-le cu ‘Tesla’ (in lista initiala de masini)
# Printati Modele vechi: x
# Modele noi: x
# """
# # E ok sa avem duplicate, listele ne permit asta, putem adauga Tesla de 2 ori
# masini_vechi = []  # lista goala
# print(masini)
# for idx in range(len(masini)):
#     masina = masini[idx]
#     if masina == 'Trabant' or masina == 'Lastun':
#         masini[idx] = 'Tesla'  # aici nu pot folosi masina = "Tesla", deoarece aici modific lista!!
#         masini_vechi.append(masina)
# print(masini)
# print(masini_vechi)

"""6. 
Avand dict
pret_masini = {
    'Dacia': 6800,
    'Lastun': 500,
    'Opel': 1100,
    'Audi': 19000,
    'BMW': 23000
}
Vine un client cu un buget de 15000 euro
Prezentati doar masinile care se incadreaza in acest buget
Iterati prin dict.items() si accesati masina si pretul
Printati Pentru un buget de sub 15000 euro puteti alege masina x
Iterati prin lista
"""
# for ... in ...  functioneaza si pe dictionare (functioneaza pe toate colectiile python)
# for element in collection (list, dictionar, tupla, set)
pret_masini = {
    'Dacia': 6800,
    'Lastun': 500,
    'Opel': 1100,
    'Audi': 19000,
    'BMW': 23000
}
# Varianta 1: iterare prin dictionar simpla, iar apoi preluam valoarea cu dictionar[key]
for key in pret_masini:
    print(key, pret_masini[key])

# Varianta 2: iteram direct prin items() cu cheie si valoare
for key, value in pret_masini.items():
    print(key, value)

buget = 15000
for masina in pret_masini:
    if pret_masini[masina] < buget:
        print(f"Pentru un buget de sub {buget} euro puteti alege masina {masina}")

print("-"*100)
"""7.
Avand lista
numere = numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
Iterati prin ea
Afisati de cate ori apare 3
(nu aveti voie sa folositi count)
"""
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
contor_3 = 0
for numar in numere:
    if numar == 3:
        contor_3 += 1  # Incrementam contorul cand am gasit numarul cautat
print(contor_3, numere.count(3))

"""8. 
Aceeasi lista
Iterati prin ea
Calculati si afisati suma numerelor
(nu aveti voie sa folositi sum)
"""
suma = 0
for numar in numere:
    suma += numar
print(suma, sum(numere))

"""9. 
Aceeasi lista
Iterati prin ea
Afisati cel mai mare numar
(nu aveti voie sa folositi max)
"""
# Fara sa folosim sort (nu are sens)
# ATENTIE: nu initializam maximul cu 0, este posibil sa avem doar numere negative in lista
nr_max = numere[0]
for numar_curent in numere:
    if numar_curent > nr_max:
        nr_max = numar_curent

print(nr_max, max(numere))

"""10.
Aceeasi lista
Iterati prin ea
Daca numarul e pozitiv, inlocuiti-l cu valoarea lui negativa
Ex: daca e 3, sa devina -3
Afisati noua lista
"""
# Modificarile se fac in lista originala
print(numere)
for i in range(len(numere)):
    if numere[i] > 0:
        numere[i] = -numere[i]
print(numere)

"""
Extra: SORT
Functia de sortare actioneaza pe o lista si o sorteaza in-place (adica modifica lista)
"""
lista_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
lista_numere.sort()
print(lista_numere)

# NU este necesar sa sortam o lista pentru fiecare numar in parte
for i in lista_numere:
    lista_numere.sort()
# Deja TOATA lista va fi sortata dupa prima iteratie, si nu are nici un sens sa continuam
