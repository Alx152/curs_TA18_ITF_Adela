import math

# Folosim mereu nume de variabile cu underscore pt a separa cuvintele, ca sa fie usor de citit
contactiv = True  # greu de citit, eu initial am citit contact iv
cont_activ = True  # usor de citit si de inteles

# Nu este necesar sa facem type casting la str cu input
cuvant = input("Introdu ceva:\n")
print(type(cuvant))  # va afisa <class 'str'> adica string
str(cuvant)  # Nu va da eroare, dar nu are sens, chiar daca ce am introdus noi este un numar/boolean, etc

# Pentru variabilele care reprezinta o lungime, putem folosi len la final ca sa se inteleaga
nume_prenume = len('Adela') + len('Kacso-Vidrean')  # cand o sa ma uit mai incolo in cod, o sa cred ca in var aceasta am valoarea numelui si a prenumelui
nume_prenume_len = len('Adela') + len('Kacso-Vidrean')  # aici e destul de clar ca am lungimea
# In general, variabilele si comentariile vor fi in engleza, deci va avea mai mult sens cu len

# Pentru situatii in care avem spatii in nume/prenume, putem sa scadem contorul de spatii din lungimea totala, daca ne intereseaza doar caractelere de tip non-spatiu
prenume = 'Elena Adela'
nume = 'Kacso Vidrean'
lungime_nume_prenume = len(nume) + len(prenume) - nume.count(' ') - prenume.count(' ')

# Pentru assert, nu avem nevoie sa facem comparatie cu True
# assert conditie == True
# e echivalent cu
# assert conditie

# Spatiile conteaza atunci cand folosim search/count
sentence = "Coral is either the stupidest animal or the smartest rock"
print(sentence.count('the'))  # o sa afiseze 3, pentru ca avem si eiTHEr
print(sentence.count(' the '))  # o sa afiseze 2, cautem doar cuvintele

# Alta modalitate este sa facem intai split, si apoi count
# In acest caz de fapt noi vom avea o lista de cuvinte, iar matchingul se va face complet cu fiecare element
words = sentence.split()
print(words)  # ['Coral', 'is', 'either', 'the', 'stupidest', 'animal', 'or', 'the', 'smartest', 'rock']
print(type(words))  # va afisa <class 'list'>

# Verificare daca un string contine doar numere
# Aici vom folosi isdigit SAU isnumeric (diferenta e un pic mai complexa, isnumeric suporta si fractii, numere romane, etc)
digits = "12345678904372829"
assert digits.isdigit(), "Acest string NU contine doar numere!"
assert digits.isnumeric(), "Acest string NU contine doar numere!"
assert isinstance(digits, int)  # NU va merge, deoarece type este string

# Exercitii optionale (mai grele)
print('=' * 80)

# Obtinere mijloc string pt lungime impara
# Exemplu string cu lungime 7 (ultimul index va fi 6, deoarece pornim de la 0) => mijlocul este indexul 3
# Putem ori sa scadem 1 din lungime inainte sa impartim la 2, ori sa folosim o metoda de rotunjire
# 0 1 2 3 4 5 6
# c u v i n t e
index_mijloc = (len(sentence) - 1) / 2  # impartire simpla
index_mijloc = len(sentence) // 2  # daca folosim // se va face impartire fara rest, adica 7 / 2 va da 3.5, dar 7 // 2 va da 3
index_mijloc = math.floor(len(sentence) / 2)  # floor ca sa facem rotunjire in jos


# Palidrom: un string care se citeste la fel din ambele capete, ex alabala
palidrom = input("Introduceti un cuvant pt a verifica daca e palindrom")
assert palidrom == palidrom[::-1]

# Compunere operatii de input + split
cuvant1, cuvant2 = input("Introdu 2 cuvinte separate de spatiu (ex. alabala portocala)").split()
print(cuvant1)
print(cuvant2)
# In viata reala, nu ne vom baza niciodata pe faptul ca utilizatorul va scrie fix 2 cuvinte, si vom face MEREU verificari
cuvinte = input("Introdu 2 cuvinte separate de spatiu (ex. alabala portocala)")
assert cuvinte.split() == 2, "Ai introdus un alt numar de cuvinte decat cel cerut!!"

