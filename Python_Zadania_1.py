# Zadanie 1
#
# input_scale = input("Podaj skalę (F/C) \n")
# temp = float(input("Podaj tempreraturę. \n"))
# if input_scale == "C":
#     output_scale = "F"
#     new_temp = 32 + (9/5) * temp
# else:
#     output_scale = "C"
#     new_temp = 5/9 * (temp - 32)
# print(f"{temp} {input_scale} to {new_temp} {output_scale}")

# Zadanie 2
#
# haslo = input("Podaj hasło\n")
#
# special_signs = ["@", "$", "#"]
# has_upper = False
# has_digit = False
# has_special_sign = False
#
# for znak in haslo:
#     if znak.isupper():
#         has_upper = True
#     if znak.isdigit():
#         has_digit = True
#     if znak in special_signs:
#         has_special_sign = True
#
# if 5 < len(haslo) < 16 and has_digit and has_upper and has_special_sign:
#     print("Hasło jest poprawne")
# else:
#     print("Hasło jest niepoprawne")

# Zadanie 3
#
# cyfry = {
#     0: "zero",
#     1: "jeden",
#     2: "dwa",
#     3: "trzy",
#     4: "cztery",
#     5: "pięć",
#     6: "sześć",
#     7: "siedem",
#     8: "osiem",
#     9: "dziewięć"
# }
#
# user_input = input("Podaj ciąg cyfr\n")
# output_str = ""
# for znak in user_input:
#     output_str += cyfry[int(znak)] + " "
# print(output_str)

# Zadanie 4
#
# int_list = [343, 53, 43, 2, 566, 90, 64]
# najm = int_list[0]
# najm_ind = 0
# for idx, elem in enumerate(int_list):
#     if elem < najm:
#         najm = elem
#         najm_ind = idx
# print(f"Najmniejszy element to {najm}, występuje na pozycji {najm_ind}")

# Zadanie 5
#
# int_list = [343, 53, 43, 2, 566, 90, 64]
# iloczyn = 1
# for elem in int_list:
#     iloczyn *= elem
# print(iloczyn)

# Zadanie 6
#
# str_list = []
# for i in range(5):
#     str_list.append(input("Podaj słowo\n"))
#
# najdl = str_list[0]
# for napis in str_list:
#     if len(napis) > len(najdl):
#         najdl = napis
# print(najdl)

# Zadanie 7
#
# napis = "The quick Brown Fox"
# upper_chars = 0
# lower_chars = 0
# for znak in napis:
#     if znak.isupper():
#         upper_chars += 1
#     elif znak.islower():
#         lower_chars += 1
#
# print(f"No of upper case characters: {upper_chars}\nNo of lower case characters: {lower_chars}")

# Zadanie 8
#
# n = int(input("Podaj n\n"))
# slownik = {}
# for i in range(1, n):
#     slownik[i] = i * i
# print(slownik)

# Zadanie 9a
#
# pierwsza_lista = [1, 2, 3, 4]
# druga_lista = [0, 3, 4, 5, 1, 2, 9]
#
# czy_zawiera = True
# for elem in pierwsza_lista:
#     if not elem in druga_lista:
#         czy_zawiera = False
#         break
# print(czy_zawiera)

# Zadanie 9b
#
# pierwsza_lista = [1, 2, 3, 4]
# druga_lista = [0, 3, 4, 5, 1, 2, 9]
# print(set(pierwsza_lista).issubset(set(druga_lista)))

# Zadanie 10
#
# slowo = input("Podaj słowo\n").lower()
# if len(slowo) == len(set(slowo)):
#     print("Jest")
# else:
#     print("Nie jest")
