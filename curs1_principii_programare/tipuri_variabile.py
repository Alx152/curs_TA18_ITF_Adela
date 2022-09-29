from math import floor, ceil

# Integer
a = 100
print(type(a))

# Float (nr zecimal)
b = 33.0
c = -10.
d = 11.554059340
print(type(b))

# Boolean
e = True  # 1
f = False  # 0
print(type(e))

# String: orice insiruire de caractere in quotes (simple sau duble)
g = 'a'
h = 'fdsjkfos390238921'
i = "Double quotes here!"
j = "100"
k = "True"
print(type(g))
print(type(i))

print('===================================================================')

# Type casting: convertirea explicita a unei variabile (dintr-un tip in altul)

# Putem converti stringuri in int, float, bool, etc (in functie de ce contine stringul)
print(type(j))
j = int(j)
print(type(j))

print(type(k))
k = bool(k)
print(type(k))

# i = int(i)  # eroare

nr_zecimal = 100.6
nr_intreg = int(nr_zecimal)
print(nr_intreg)  # putem converti float -> int, dar pierdem zecimalele

# Extra stuff
# Daca vrem rotunjire sus (functia ceil), sau jos (functia floor) din libraria math
print(floor(nr_zecimal))
print(ceil(nr_zecimal))

print("===============================================================================")

# Cand facem type casting, TREBUIE sa facem asignare
alfa = "3242"
print(type(alfa))
int(alfa)
print(type(alfa)) # Ramane tot string, pentru ca nu am facut asignare
alfa = int(alfa)  # Aici modificam valoarea
print(type(alfa))
