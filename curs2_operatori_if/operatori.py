# a += 5  # nu va merge, pt ca se evalueaza la a = a + 5, dar nu avem valoare initala pt a

# Operatori de atribuire (assign)
i = 10
s = "Salut, lume"
f = 1.2223343

i += 2  # echivalent cu i = i + 2 => 12
i -= 2  # i => 10
i /= 2  # i => 5
i *= 2  # i => 10
i //= 3  # i => 3 (floor division / integer division) impartire fara rest
print(i)

# Cel mai des folosim pt incrementare/decrementare
idx = 0
print(s[idx])
idx += 1
print(s[idx])
idx += 1
print(s[idx])

# Adunarea o putem face si pe str (are rol de concatenare)
a = "alabala "
a += "portocala"
# print(a.__add__(" alta portocala"))  # Exista si metoda de add, DAR nu e recomandat sa o folosim; folosim mereu + pentru concatenare
print(a)

# Scadere NU putem face
# a -= "portocala"  # o sa dea eroare

# Putem inmulti un string cu un int, rezultatul va fi stringul initial repetat de x ori
x = "adela "
x *= 5
print(x)  # adela adela adela adela adela
print("=" * 20)

# Operatori aritmetici (toti cei de la matematica)
op1, op2 = 5, 7
suma = op1 + op2
dif = op1 - op2
prod = op1 * op2  # produs
imp = op1 / op2
rest = op2 % op1  # operatorul modulo, 2
put = op2 ** op1  # ridicarea la putere

# Operatori de comparare: rezultatul va fi bool (True/False)
print(op1 == op2)  # False
print(op1 != op2)  # numerele sunt diferite? True
print(op1 > op2)  # False
print(op1 < op2)  # True
print(op2 >= op1)  # True
print(op2 <= op1)  # False

# Putem combina operatorii mereu
assert (3 + 4) == (2 + 5)

# Operatori logici: actioneaza pe var de tip bool, si returneaza tot bool

# AND (si) : returneaza True daca ambele conditii sunt True
nota = int(input("Scrie o nota: "))
assert 1 < nota and nota <= 10, "Nota nu este valida"
assert 1 < nota <= 10, "Nota nu este valida"  # In python putem inlantui comparatii

# OR (sau) : returneaza True daca cel putin o conditie este True
nota1, nota2 = input("Introdu cele 2 note").split()
nota1 = int(nota1)
nota2 = int(nota2)
# Daca nota1 sau nota2 e mai mica decat 5, ai picat
assert nota1 < 5 or nota2 < 5, "Ai picat!"

# NOT (operatorul de negare): True devine False, si viceversa
age = int(input("Varsta:"))
este_major = age > 18
assert not este_major, "Daca nu este major, da eroare"
