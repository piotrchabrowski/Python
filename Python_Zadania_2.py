# Zadanie 1
#
# def is_palindrom(napis):
#     napis = "".join(napis.lower().split())
#     return napis == napis[::-1]
#
# print(is_palindrom("nurses run"))
# print(is_palindrom("kajak"))
# print(is_palindrom("Ala ma kota"))


# Zadanie 2a
#
# import string
#
# def is_pangram1(napis):
#     count_letter = {}
#     napis = "".join(napis.lower().split())
#     for znak in napis:
#         count_letter[znak] = count_letter.get(znak, 0) + 1
#
#     alphabet = set(string.ascii_lowercase)
#     return set(count_letter.keys()) == alphabet

# Zadanie 2b
# from collections import Counter
#
# def is_pangram2(napis):
#     napis = "".join(napis.lower().split())
#     return len(Counter(napis).keys()) == 26

# is_pangram = is_pangram2
# print(is_pangram("The quick brown fox jumps over the lazy dog"))
# print(is_pangram("Ala ma kota"))


# Zadanie 3
#
# roman_numbers = {
#     "I": 1,
#     "V": 5,
#     "X": 10,
#     "L": 50,
#     "C": 100,
#     "D": 500,
#     "M": 1000
# }
#
# def roman_to_int_rec(roman_number):
#     if not roman_number:
#         return 0
#     if len(roman_number) == 1:
#         return roman_numbers[roman_number]
#     first = roman_numbers[roman_number[0]]
#     second = roman_numbers[roman_number[1]]
#     if first < second:
#         return second - first + roman_to_int(roman_number[2:])
#     else:
#         return first + roman_to_int(roman_number[1:])
#
# def roman_to_int_iter1(roman_number):
#     suma = 0
#     idx = 0
#     while idx < len(roman_number):
#         if len(roman_number[idx:]) > 1:
#             first = roman_numbers[roman_number[idx]]
#             second = roman_numbers[roman_number[idx+1]]
#             if first < second:
#                 suma += second - first
#                 idx += 2
#             else:
#                 suma += first
#                 idx += 1
#         else:
#             suma += roman_numbers[roman_number[idx]]
#             idx += 1
#     return suma
#
# def roman_to_int_iter2(roman):
#     suma = 0
#     for i in range(0, len(roman)):
#         if i == len(roman) - 1:
#             suma += roman_numbers.get(roman[i])
#             return suma
#         elif roman_numbers.get(roman[i]) < roman_numbers.get(roman[i+1]):
#             suma -= roman_numbers.get(roman[i])
#         else:
#             suma += roman_numbers.get(roman[i])
#
#
# roman_to_int = roman_to_int_rec
# print(roman_to_int("XL"))  # 40
# print(roman_to_int("LXXX"))  # 80
# print(roman_to_int("MCLXIV"))  # 1164
# print(roman_to_int("MCMXCV"))  # 1995
# print(roman_to_int("MMMDCCLXXXVIII"))  # 3788


# Zadanie 4
#
# def is_perfect(liczba):
#     suma = 0
#     for x in range(1, liczba):
#         if liczba % x == 0:
#             suma += x
#
#     return suma == liczba
#
# print(is_perfect(6))
# print(is_perfect(28))
# print(is_perfect(31))


# Zadanie 5
#
# def fibonacci_recursive(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci_recursive(n-2) + fibonacci_recursive(n-1)
#
#
# def fibonacci_iterative(n):
#     fibonacci = [0, 1]
#     for i in range(2, n+1):
#         fibonacci.append(fibonacci[i-2] + fibonacci[i-1])
#
#     return fibonacci[n]
#
# print(fibonacci_recursive(5))
# print(fibonacci_iterative(5))
# print(fibonacci_recursive(19))
# print(fibonacci_iterative(19))


# Zadanie 6
#
# def is_lap_year(year):
#     if year % 400 == 0:
#         return True
#     elif year % 4 == 0 and year % 100 != 0:
#         return True
#     else:
#         return False
#
# def is_lap_year2(year):
#     return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)
#
#
# print(is_lap_year(2019))
# print(is_lap_year2(2019))
# print(is_lap_year(1996))
# print(is_lap_year2(1996))


# Zadanie 7
#
# sklep = {
#     "bułka": {
#         "cena" : 1.5,
#         "ilosc": 300
#     },
#     "chleb": {
#         "cena": 3,
#         "ilosc": 200
#     },
#     "rogalik": {
#         "cena": 10,
#         "ilosc": 3
#     }
# }
#
# produkt = input("Czego chcesz?\n")
#
# if produkt in sklep:
#     ilosc = int(input("Ile?\n"))
#     na_stanie = sklep[produkt]["ilosc"]
#     if na_stanie >= ilosc:
#         cena = sklep[produkt]["cena"]
#         print(f"Do zapłaty {cena * ilosc}")
#     else:
#         print("Nie mam tyle")
# else:
#     print("Nie ma")


# Zadanie 8
#
# def most_common():
#     words_freq = {}
#     with open("../oda.txt") as file:
#         for line in file:
#             for word in line.lower().split():
#                 words_freq[word] = words_freq.get(word, 0) + 1
#
#     print(sorted(words_freq.items(), key=lambda x: x[1], reverse=True)[:5])
#
# most_common()


# Zadanie 9
#
# import math
#
#
# class Kolo:
#     def __init__(self, promien):
#         self.r = promien
#
#     def obwod(self):
#         return round(2 * math.pi * self.r, 3)
#
#     def pole(self):
#         return round(math.pi * self.r ** 2, 3)
#
#
# a = Kolo(4)
# print(a.obwod(), a.pole())


# Zadanie 10
#
# class Produkt:
#     def __init__(self, nazwa, cena):
#         self.nazwa = nazwa
#         self.cena = cena
#
#     def __str__(self):
#         return f"Produkt {self.nazwa}, o cenie {self.cena}"
#
#     def __repr__(self):
#         return f"Produkt {self.nazwa}, o cenie {self.cena}"
#
# class Koszyk:
#     def __init__(self):
#         self.produkty = {}
#
#     def usun_wszystko(self):
#         self.produkty = {}
#
#     def pokaz(self):
#         # for produkt, ilosc in self.produkty.items():
#         #     print(produkt, ilosc)
#         print(self.produkty)
#
#     def oblicz_wartosc(self):
#         suma = 0
#         for produkt, ilosc in self.produkty.items():
#             suma += produkt.cena * ilosc
#         print(suma)
#
#     def dodaj(self, produkt):
#         if produkt in self.produkty:
#             self.produkty[produkt] += 1
#         else:
#             self.produkty[produkt] = 1
#
#     def usun(self, produkt):
#         if produkt in self.produkty:
#             if self.produkty[produkt] > 0:
#                 self.produkty[produkt] -= 1
#         else:
#             print("Nie ma")
#
#
# produkt1 = Produkt("komputer", 3000)
# produkt2 = Produkt("zegarek", 500)
# ptodukt3 = Produkt("chleb", 3)
#
# koszyk = Koszyk()
# koszyk.dodaj(ptodukt3)
# koszyk.pokaz()
# koszyk.dodaj(produkt2)
# koszyk.oblicz_wartosc()
# koszyk.dodaj(ptodukt3)
# koszyk.pokaz()
# koszyk.usun(ptodukt3)
# koszyk.pokaz()
# koszyk.usun_wszystko()
# koszyk.oblicz_wartosc()

