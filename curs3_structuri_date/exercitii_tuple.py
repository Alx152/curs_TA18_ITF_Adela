# Tuple - ca o lista, dar IMUTABILA, adica nu putem modifica, adauga, sterge
t = (1, 2, 3, 4, True, "False", 3.14)  # Tuplele folosesc paranteze rotunde

print(type(t))
print(t[0])
print(t[1:5])
print(t[-1])

# t[0] = 7  # Eroare
# t.append(7)  # Eroare
# t.remove(3)  # Eroare
t = (
    {
        "name": "Adela",
        "age": 21
    },
    1234
)

print(t)
t[0]["name"] = "Maria"  # Pot modifica variabilele complexe din interiorul tuplei, daca acestea sunt mutabile
print(t)
