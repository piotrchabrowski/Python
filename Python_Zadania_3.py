# Zadanie 1

#def swap(a, b):
#	a  = a + b
#	b = a - b
#	a = a - b
#	return a, b
#	
#a = 5
#b = 3
#print(a, b)
#a, b = swap(a, b)
#print(a, b)


# Zadanie 2

#from random import choice

#znaki_wygrywanie = {
#	'k': 'n',  # kamień wygrywa z nożyczkami
#	'p': 'k',  # papier wygrywa z kamieniem
#	'n': 'p'  # nożyczki wygrywają z papierem
#}

#znaki_nazwy = {
#	'k': "kamień",
#	'n': "nożyczki",
#	'p': "papier"
#}

#punkty_user = 0
#punkty_komputer = 0
#while punkty_user < 3 and punkty_komputer < 3:
#	wybor_usera = input("Co wybierasz? Wybierz z opcji: k, n, p \n")
#	wybor_komputera = choice(["k", "n", "p"])
#	if znaki_wygrywanie[wybor_usera] == wybor_komputera:
#		print(f"Wybrałeś {znaki_nazwy[wybor_usera]}, wygrałeś z komputerem, który wybrał {znaki_nazwy[wybor_komputera]}")
#		punkty_user +=1
#	elif znaki_wygrywanie[wybor_komputera] == wybor_usera:
#		print(f"Wybrałeś {znaki_nazwy[wybor_usera]}, przegrałeś z komputerem, który wybrał {znaki_nazwy[wybor_komputera]}")
#		punkty_komputer += 1
#	else:
#		print(f"Oboje wybraliście {znaki_nazwy[wybor_usera]}, jest remis")

#if punkty_user > punkty_komputer:
#	print("WYGRAŁEŚ!")
#else:
#	print("PRZEGRAŁEŚ!")


# Zadanie 3

#def suma_cyfr_iter(liczba):
#	suma = 0
#	while liczba != 0:
#		suma += liczba % 10
#		liczba = liczba // 10
#	return suma

#def suma_cyfr_rek(liczba):
#	if liczba == 0:
#		return 0
#	return liczba % 10 + suma_cyfr_rek(liczba // 10)
#			
#a = 12343
#print(suma_cyfr_iter(a))
#print(suma_cyfr_rek(a))


# Zadanie 4

#def suma_cyfr_potega_iter(liczba, n):
#	suma = 0
#	while liczba != 0:
#		suma += (liczba % 10) ** n
#		liczba = liczba // 10
#	return suma

#def narcystyczna(liczba):
#	n = len(str(liczba))
#	return suma_cyfr_potega_iter(liczba, n) == liczba
#	
#print(narcystyczna(153))
#print(narcystyczna(847))
#print(narcystyczna(9474))


# Zadanie 5

#def pow_iter(a, b):
#	result = 1
#	for i in range(b):
#		result *= a
#	return result
#	
#def pow_rek(a, b):
#	if b == 1:
#		return a
#	return a * pow_rek(a, b-1)
#	
#print(pow_iter(3, 5))
#print(pow_rek(3, 5))


# Zadanie 6

#def ciag_iter(n):
#	ciag = [2]
#	i = 1
#	while i < n:
#		if (i + 1) % 2 == 0:
#			ciag.append(ciag[i-1] + 2)
#		else:
#			ciag.append(ciag[i-1] * 2)
#		i += 1
#	return ciag
#	
#def ciag_rek(n):
#	if n == 1:
#		return 2
#	elif n % 2 == 0:
#		return ciag_rek(n-1) + 2
#	else:
#		return ciag_rek(n-1) * 2
#	
#print(ciag_iter(5))
#print([ciag_rek(x) for x in range(1, 6)])


# Zadanie 7

#def nwd(a, b):
#	x = a % b
#	if x == 0:
#		return b
#	return nwd(b, x)
#	
#print(nwd(282, 78))


# Zadanie 8

#from collections import Counter

#def are_anagrams(napis1, napis2):
#	napis1 = "".join(napis1.lower().split())
#	napis2 = "".join(napis2.lower().split())
#	return Counter(napis1) == Counter(napis2)
#	
#print(are_anagrams("Tom Marvolo Riddle", "I am Lord Voldemort"))
#print(are_anagrams("Ala ma kota", "Kot ma Alę"))


# Zadanie 9

#class Konto:
#	def __init__(self):
#		self.saldo = 0
#		self.is_active = False
#	
#	def otworz_konto(self):
#		self.is_active = True
#	
#	def zamknij_konto(self):
#		self.is_active = False
#	
#	def zwroc_saldo(self):
#		if self.is_active:
#			print(f"Na koncie jest {self.saldo} pieniędzy")
#		else:
#			print("Najpierw musisz otworzyć konto, by poznać saldo")
#	
#	def wplac(self, kwota):
#		if self.is_active:
#			self.saldo += kwota
#			print(f"Wpłacono {kwota} pieniędzy")
#		else:
#			print("By dokonać wpłaty musisz otworzyć konto")
#			
#	def wyplac(self, kwota):
#		if self.is_active:
#			if kwota < self.saldo:
#				self.saldo -= kwota
#				print(f"Wypłacono {kwota} pieniędzy")
#			else:
#				print("Na koncie nie ma wystarczających środków")
#		else:
#			print("By dokonać wypłaty musisz najpierw otworzyć konto")
#			
#rachunek_osobisty = Konto()
#rachunek_osobisty.otworz_konto()
#rachunek_osobisty.zwroc_saldo()
#rachunek_osobisty.wplac(100)
#rachunek_osobisty.zwroc_saldo()
#rachunek_osobisty.wyplac(10)
#rachunek_osobisty.zwroc_saldo()
#rachunek_osobisty.wyplac(100)
#rachunek_osobisty.zamknij_konto()
#rachunek_osobisty.zwroc_saldo()
		

# Zadanie 10

#from math import sqrt

#class Point:
#	def __init__(self, x, y):
#		self.x = x
#		self.y = y
#	
#	def __str__(self):
#		return f"Punkt ({self.x}, {self.y})"

#	def przesun(self, a, b):
#		self.x += a
#		self.y += b
#		
#	def odleglosc(self, other):
#		return sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
#				
#punkt1 = Point(2, 3)
#print(punkt1)
#punkt1.przesun(3, 6)
#print(punkt1)
#punkt2 = Point(2, 5)
#print(punkt2)
#print(punkt1.odleglosc(punkt2))