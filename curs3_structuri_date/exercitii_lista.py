# Lista = o structura de date complexa, in care putem pastra alte tipuri de date
# O putem asemnana cu un tren, fiecare vagon reprezinta un element din lista


# Initializare lista
lst = []  # Python creeaza o lista goala
lst_str = ['C', 'o', 'r', 'a', 'l']
str = "Coral"  # echivalent cu lista de mai sus

# Indexare
lst_diff = [12, True, "str", 3.1415, "final string"]
print(lst_diff[0])  # printeaza 12
print(lst_diff[-1])  # printeaza "final string"

# List slicing - functioneaza exact la fel ca si la stringuri
print(lst_diff[2:4])  # printeaza al doilea si al treilea element din lista

lst_nr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(lst_nr[::2])  # printeaza nr pare
print(lst_nr[1::2])  # printeaza nr impare

print(lst_nr.index(7))

# Functii specifice pentru liste de numere: max, min, sum
print(f"Maximul este: {max(lst_nr)}")
print(f"Minimul este: {min(lst_nr)}")
print(f"Suma nr este: {sum(lst_nr)}")

# Operatii pe lista : add, delete, change
print(lst_nr)
lst_nr.append(10)  # Adaugarea unui element LA FINAL se face cu append
print(lst_nr)
lst_nr[0] = -1  # Schimbarea unui element se face folosind indexul acestuia => listele sunt MUTABILE
print(lst_nr)
lst_nr.remove(5)  # Sterge valoarea data ca parametru
print(lst_nr)
# lst_nr.remove(5)  # O sa dea eroare, deoarece nu mai exista 5 in lista

# Listele pot contine valori duplicate
lst_nr.append(10)
print(lst_nr)

# List membership: se face folosind in
print(f"Este 10 in lista?")
print(10 in lst_nr)
print(f"Este 5 in lista?")
print(5 in lst_nr)

# !! ATENTIE !!
l1 = [1, "2", True, "alfa"]
l2 = l1  # L1 este acum la aceeasi locatie din memorie ca si L2, deci daca modificam una din ele, se modifica si cealalta!!
l2.append(3)
print(l2)
print(l1)
l1.remove("2")
print(l1)
print(l2)

# Daca vrem sa copiem o lista intr-una noua, si sa nu mai fie dependente una de cealalta, putem folosi copy
l2 = l1[:]  # cu list slicing de la 0 la len, il fortam pe Python sa faca o copie noua a listei, la o noua locatie in memorie
l2.append(100)
print(l1)
print(l2)

lst_complexa = [1, 2, ["a", "b", "c"], True, False]
print(len(lst_complexa))  # va da 5, deoarece lista din interior este un singur element

# Inserare inainte de indexul 5: insert(index, value)
lst_nr.insert(5, "cinci")
print(lst_nr)
