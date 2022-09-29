my_str = "Acesta este un sir de 12 caractere"
# Accesare prin index, incepem mereu de la 0
print(my_str[0])  # va afisa "A"
print(my_str[5])  # va afisa "a"
print(my_str[6])  # va afisa " "
# Functia len ne da lungimea totala a stringului
my_str_len = len(my_str)
print(f"Lungimea sirului  este {my_str_len}")
print(my_str[my_str_len - 1])  # va afisa "e"
# print(my_str[my_str_len])  # va da eroare

# Exista si optiunea de index negativ, ceea ce inseamna ca se numara de la sfarsit
print(my_str[-1])  # Imi va afisa "e", ultimul caracter
print(my_str[-2])  # va afisa "r"

# Slicing [index inceput : index sfarsit] => ne da substring de la index inceput, pana la index sfarsit, dar fara ultimul caracter
print(my_str[2:5])  # va afisa "est"
print(my_str[0:my_str_len])  # va afisa tot stringul initial

# Putem omite index start/stop, daca vrem sa mergem de la/ pana la capat
print(my_str[:6])  # va afisa "Acesta"
print(my_str[28:])  # va afisa "actere"

# Slicing complet [idx inceput : idx sfarsit : step]. By default, step e 1
print(my_str[:10:2])
# Step (pasul) poate fi si negativ; ATENTIE: idx start aici trebuie sa fie MAI MARE decat index stop
print(my_str[10:2:-1])  # 10, 9, 8, 7, 6, 5, 4, 3 vor fi indicii afisati
print(my_str[::-1])  # Asa inversam un string: "eretcarac 21 ed ris nu etse atsecA"

# Metode: sunt niste functii speciale, care se aplica pe string
# Exemple: upper, lower, count, replace
my_upper_str = my_str.upper()
print(my_upper_str)  # va afisa "ACESTA ESTE UN SIR DE 12 CARACTERE"
print(my_str.isupper())  # va returna False
print(my_upper_str.isupper())  # va returna True

# Count va numara cate substringuri (dat ca parametru) sunt in stringul meu
print(my_str.count("a"))  # va afisa 3
# Ca sa numaram si primul a
# Varianta 1: numaram in propozitia lower
print(my_str.lower().count("a"))
# Varianta 2: numaram si a mic si A mare
print(my_str.count("a") + my_str.count("A"))
print(my_str.replace("a", "x"))  # "Acestx este un sir de 12 cxrxctere"
