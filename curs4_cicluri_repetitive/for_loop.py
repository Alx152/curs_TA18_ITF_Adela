# # FOR: ciclu repetitiv in care stim cati pasi vom efectua
# # for index in range(n):
# #    fa ceva cu index
#
# # range = functie care ne da un numar de pasi: 0, 1, 2, 3, .... n
# # range(n) - n va fi parametrul de stop
# # range(start, stop) - start, start+1, start+2, .... stop
# # range(start, stop, pas) - start, start+pas, start+2*pas, ... stop
# for idx in range(10):
#     print(idx)
#
# print("*" * 80)
# # Exemplu: afisare elemente lista unul cate unul
# # Putem folosi numerele oferite de functia range ca si indici pentru a accesa elementele din lista noastra
# lst = ['luni', 'marti', 'miercuri', 'joi', 'vineri']
# for idx in range(len(lst)):
#     print(lst[idx])
#
# print("*" * 80)
# for idx in range(1, 10, 2):
#     print(idx)
#
# print("*" * 80)
# # Iterare peste colectii Python
# # for element in collection:
# #    fa ceva cu element
# for zi in lst:
#     print(zi)

# Exemplu: gasirea unui numar intr-o lista data
my_list = [34, 12, 7, 5, 99, 100]
number_to_find = 77
number_found = False

for number in my_list:
    print(f"Testam valoarea {number}")
    if number == number_to_find:
        print("Am gasit numarul cautat in lista!")
        number_found = True
        break

if not number_found:
    print(f"{number_to_find} nu se gaseste in lista!")

print("Am terminat for-ul!")

# Ce am scris mai sus se poate scrie asa
for number in my_list:
    if number == number_to_find:
        print("Am gasit!")
        break
else:
    # Ramura else de la for se va executa daca in timpul for-ului nu am ajuns deloc la o instructiune BREAK
    print("Nu am gasit numarul cautat!")


print("="*80)
# Continue - sari peste codul ce urmeaza la iteratia urmatoare
# Exemplu: afisare numere impare prin "sarirea" peste cele pare
for i in range(10):
    print(f"Verificam {i}")
    if i % 2 == 0:
        # Daca am un numar par, vreau sa sar la urmatorul numar
        print(f"{i} este par, SARIM peste el")
        continue
    print(f"{i} este numar impar")

# Unirea a 2 liste, iterand peste una dintre ele si folosind append
l1 = [4, 3, 54, 6, 12, 0]
l2 = [43, 5, 9, 99, 100, 2, 3]
# l1.extend(l2)
for element in l2:
    l1.append(element)
