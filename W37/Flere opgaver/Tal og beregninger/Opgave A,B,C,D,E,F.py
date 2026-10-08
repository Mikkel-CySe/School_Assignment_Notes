#Opgave A
#Spørg brugeren om hvor mange login-forsøg der blev registreret i system A og i system B og udskriv til slut det samlede antal forsøg.
print("Opgave A")
login_a=int(input("Angiv hvor mange login-forsøg der er blevet registreret, i system A: "))

login_b=int(input("Angiv hvor mange login-forsøg der er blevet registreret, i system B: "))

print(f"Det samlede antal login-forsøg for hhv. system A og B er: {login_a+login_b}")

#Opgave B
#Spørg brugeren om hvor mange mislykkede login-forsøg der var i går og i dag og
#udskriv forskellen mellem dem (i dag minus i går).
print("\nOpgave B")
log_yesterday = int(input("Angiv hvor mange mislykkede login-forsøg der var i går: "))
log_today = int(input("Angiv hvor mange mislykkede login-forsøg der har været idag: "))

print(f"De mislykkede login-forsøg fra igår og idag har en forskel på: {abs(log_today-log_yesterday)}")

#Opgave C
#Spørg brugeren om hvor mange pakker der blev sendt og hvor mange der blev blokeret af
#firewallen og udskriv produktet af tallene.
print("\nOpgave C")
products_sent = int(input("Angiv hvor mange produkter der er blevet sendt: "))
products_blocked = int(input("Angiv hvor mange produkter der er blevet blokeret: "))

print(f"Produktet af pakkerne som er blevet sendt og blokeret er da: {products_sent * products_blocked}")

#Opgave D
#Spørg brugeren om den samlede datamængde (MB) og tiden (sekunder) og udskriv den
#gennemsnitlige datahastighed (MB pr sekund).
print("\nOpgave D")
mb_second = int(input("Angiv et antal mb: "))
sekunder = int(input("Angiv sekunder: "))

print(f"Den gennemsnitlige datahastig vil da blive: {((mb_second * sekunder)/2)} MB pr sekund.")

#Opgave E
#Spørg brugeren om antallet af angreb fra én IP-adresse og udskriv tallet opløftet i anden potens
#(dvs. vi simulerer belastning).
print("\nOpgave E")
attack = int(input("Angiv hvor mange angreb der kommer fra 192.168.1.10: "))

print(f"Belastningen fra 192.168.1.10 er: {attack**2}")

#Opgave F
#Spørg brugeren om fem målinger af netværkstrafik (i MB) og udskriv gennemsnittet
print("\nOpgave F")
total = 0
for measure in range(5):
    total = int(input(f"Angiv hvad netværkstrafikken er MB for netværkstrafik {measure+1}: ")) + total
print("Den gennemsnitlige MB er da:", (total/5))
