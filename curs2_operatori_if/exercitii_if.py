# Indentare: vom avea mereu 4 spatii / 1 tab ca sa indentam codul din Python

# nota_trecere = 5
# nota_mea = int(input("Scrie nota ta:\n"))
#
# print("Inainte de IF")
# if nota_mea >= nota_trecere:
#     print("Aici sunt in interiorul blocului IF, "
#           "voi ajunge aici doar daca nota mea e mai mare decat nota de trecere")
#     print("Oricate lucruri fac, daca am indentare, sunt tot in blocul IF")
#     nota_trecere = 9
#
# print(nota_trecere)
# print("Dupa IF")


# # If-else
# varsta = int(input("Introdu varsta ta:\n"))
# if varsta >= 18:
#     print("Esti major")
# else:  # Altfel, daca varsta este mai mica decat 18
#     print("Esti minor")
# print("Gata!")

# # If-elif-else
# a, b = input("Introdu 2 numere intregi separate de spatiu\n").split()
# a, b = int(a), int(b)
# operator = input("Alege un operator (+ - * /)\n")
# if operator == "+":
#     # Facem adunare
#     print(a + b)
# elif operator == "-":
#     print(a - b)
# elif operator == "*":
#     print(a * b)
# else:
#     # Ultimul bloc va fi else simplu, pentru ca nu mai avem conditii
#     print(a / b)

# # If-urile pot fi imbricate
# varsta = int(input("Varsta\n"))
# if varsta > 18:
#     print("Esti adult")
# else:
#     if varsta < 1:
#         print("Esti bebelus")
#     else:
#         print("Esti copil")

note_sesiune = input("Introdu cele 3 note")
nota1, nota2, nota3 = note_sesiune.split() # impartim stringul de intrare in substringuri
print(nota1, nota2, nota3, type(nota1), type(nota2), type(nota3))
# Facem type casting, pentru ca altfel nu putem compara cu integer
nota1 = int(nota1)
nota2, nota3 = int(nota2), int(nota3)
if nota1 > 5:
    print("Ai trecut")

