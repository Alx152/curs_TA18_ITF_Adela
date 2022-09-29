# Dictionary: structura de date cu cheie: valoare
# Ca si cum am avea un tren in care ne putem referi la vagoane folosind denumiri

tren = {}  # initializat dictionar gol
tren = {
    "vagonul rosu": "malai",
    "vagonul al 3lea": "faina",
    "ultimul vagon": "cereale"
}
print(tren["vagonul al 3lea"])

# Aceste 2 structuri sunt echivalente
dict_as_list = {
    0: "zero",
    1: "unu",
    2: True,
    3: 3.1415
}
lst = ["zero", "unu", True, 3.1415]
print(dict_as_list[0] == lst[0])

text = "A shallow copy constructs a new compound object and then (to the extent possible) inserts references into it to the objects found in the original. A deep copy constructs a new compound object and then, recursively, inserts copies into it of the objects found in the original."
print(text.count("c"))

# Cheile pot fi numere, stringuri, si tuple
cnt_dict = {
    "a": text.count("a"),
    "b": text.count("b"),
    "c": text.count("c")
}
print(cnt_dict)
print(cnt_dict['c'])

# Dictionarele sunt mutabile, adica putem adauga/sterge/modifica
cnt_dict['d'] = 7  # Adaugare in dictionar
print(cnt_dict)
cnt_dict['d'] = 100  # modificare valoare
print(cnt_dict)
del cnt_dict['d']  # Stergere
print(cnt_dict)

# Cheile trebuie sa fie unice, la fel ca si indicii dintr-o lista
d = {
    1: "a",
    1: "b",
    1: "c"
}
print(d[1])  # NU o sa dea eroare, dar ne va da o singura valoare, ceea ce nu vrem

# Un alt exemplu de dictionar
person = {
    "name": "Adela",
    "age": 25,
    "gender": "F",
    "is_married": True
}

print(f"Ma cheama {person['name']} si am {person['age']} ani.")

# Verificare existenta chei, obtinere chei, etc
print(person.keys())  # Imi da lista cu toate cheile existente in dictionar
# print(person['first_name'])  # O sa dea eroare, pentru ca aceasta cheie nu exista
print(person.get("first_name"))  # o sa dea None, DAR nu o sa dea eroare
person["first_name"] = "Ade"
print(person.keys())

# Update value: a mai crescut cu un an persoana
person["age"] += 1
print(person)

# Dictionary membership: putem vedea daca o anumita cheie exista
print("last_name" in person)

# Putem folosi colectiile Python cum dorim noi, de exemplu putem avea o lista de dictionare
lst_persoane = [
    {
        "name": "dan",
        "age": 25
    },
    {
        "name": "lavinia",
        "age": 21
    },
    {
        "first_name": "calin",
        "age": 101
    }
]

print(lst_persoane[0]["name"])
print(lst_persoane[1]["name"])

# Extra
for person in lst_persoane:
    if "name" in person:
        print(person["name"])
