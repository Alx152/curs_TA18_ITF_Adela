# WHILE (cat timp)
# while conditie:
#     fa ceva

# # While este o structura repetitiva prin care se executa o bucata de cod cat timp conditia pusa este adevarata
#
# i = 0
# while i < 7:
#     print(i)
#     i += 1
#
# print("Am terminat!")

# # Use-case real: preluare user input si verificare sa fie corect
# # Vrem sa luam varsta utilizatorului, care trebuie sa fie int, si sa fie intre 1 si 99
# age = 0
# correct_input = False
# while not correct_input:
#     age = input("Introdu varsta\n")
#     if age.isdigit():
#         age = int(age)
#         if 1 < age < 99:
#             print(f"Ai introdus {age}, care este o varsta corecta! Felicitari!")
#             correct_input = True
#         else:
#             print("Nu ati selectat o varsta corecta, nu este in intervalul 1-99!")
#     else:
#         print("Nu ai introdus un numar! Te rog mai incearca!\n")

# Ghicire numar la care s-a gandit calculatorul (intre 1 si 10)
numar_calculator = 7
numar_ghicit = int(input("Ghiceste:\n"))

while numar_ghicit != numar_calculator:
    if numar_calculator < numar_ghicit:
        print("Numarul la care m-am gandit eu este mai mic decat cel ghicit")
    else:
        print("Numarul la care m-am gandit eu este mai mare decat cel ghicit")
    numar_ghicit = int(input("Ghiceste din nou:\n"))

print("Felicitari, ai castigat, acesta era numarul ghicit!")
