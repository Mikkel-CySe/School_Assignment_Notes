
#4-13.
#Buffet: A buffet-style restaurant offers only five basic foods.
#Think of five simple foods, and store them in a tuple.
#Use a for loop to print each food the restaurant offers.
#Try to modify one of the items, and make sure that Python rejects the change.
#The restaurant changes its menu, replacing two of the items with different foods.
#Add a line that rewrites the tuple, and then use a for loop to print each
#of the items on the revised menu.
print("--- Opgave 4.13 ---")
print("- Original menu -")
buffet_food = ("Chicken", "Burger", "Pizza", "Kartoffel", "Kødsovs")

for food in buffet_food:
    print(food)

#buffet_food.append("Suppe")
#print(buffet_food)
print("\n- Ny meny -")
buffet_food = ("Fisk", "Burger", "Pizza", "Kartoffel", "Steak")
for food in buffet_food:
    print(food)








#Opgave A
#Lav en liste med mindst 8 forskellige byer.
#Brug slices til at udskrive:
#   De første tre byer
#   De sidste tre byer
#   Tre byer fra midten
#Lav derefter et loop som kun gennemløber de første fire byer.
#Udskriv: I would like to visit Esbjerg
#for hver af de fire byer. (Det med gult skal jo skiftes ud for hver by)
print("\n--- Opgave 1 Byer ---")
cities = ["Esbjerg", "Varde", "Hemmet", "Aarhus", "KBH", "Odense", "Tønder", "Vejers"]

print(f"3 første byer: {cities[:3]}")
print(f"3 sidste byer: {cities[-3:]}")
print(f"3 midter byer: {cities[3:6]}")

print()
for city in cities[:4]:
    print(f"I would like to visit: {city}")










print("\n--- Opgave 2 IP Adresser som tuple---")
#En IPv4-adresse består af fire tal.
#Opret IP-adressen 192.168.1.25 som en tuple:
#ip = (192, 168, 1, 25)
#Udskriv hele tuplen.
#Udskriv kun det første tal.
#Udskriv kun det sidste tal.
#Brug et for-loop til at udskrive alle fire tal.
#Prøv til sidst:
#ip[3] = 30 Hvad sker der? Forklar hvorfor.

ip = (192, 168, 1, 25)
print(f"Her printes hele tuplen: {ip}")
print(f"Det første tal er: {ip[0]}")
print(f"Det sidste tal er: {ip[-1]}")

print("\n- Ip information -")
for adresse in ip:
    print(adresse)

#ip[3] = 30
#Scriptet fejler, da det ikke er muligt at ændre variabler i tuplen, medmindre man overskriver.







print("\n--- Opgave 3 Tilladte porte ---")
#En firewall tillader kun trafik til bestemte porte.
#Gem de tilladte porte i en tuple:
#allowed_ports = (22, 80, 443)
#Lav en variabel: port = 443
#Undersøg med if og in, om port findes i allowed_ports.
#Programmet skal udskrive enten:
#   Port is allowed
#eller:
#   Port is blocked
#Afprøv programmet med:
#   22, 25, 80, 443, 8080
#Ekstra: Lad brugeren indtaste portnummeret med input().

allowed_port = (22, 80, 443)

while True:
    #int input
    port = int(input("Enter your port: "))
    if port in allowed_port:
        print("Port is allowed.")
    elif port not in allowed_port:
        print("Port is blocked.")

    #str input
    quit=input("Do you want to quit? (y/n): ")
    if quit == "y" or quit == "Y":
        print()
    elif quit == "n" or quit == "N":
        print("Thanks for now!")
        break
    else:
        print("Okay, i assume you wanted to continue.")









print("\n--- Opgave 4 - SIKKERHEDSHÆNDELSE ---")
#Vi kan repræsentere en simpel sikkerhedshændelse med en tuple:
#event = ("192.168.1.25", "failed_login", 5)
#Tuplen indeholder:
#   IP-adresse
#   Type af hændelse
#   Antal forsøg
#Udskriv de tre værdier hver for sig.
#Lav derefter en betingelse:
#Hvis event[1] er "failed_login" og event[2] er mindst 3, skal programmet udskrive:
#Warning: Multiple failed login attempts
#Ekstra: Udskriv også den IP-adresse advarslen kommer fra

event = ("192.168.1.25", "failed_login", 5)

# Udskriv de tre værdier
for events in event:
    print(events)
print()

# Tjek om der er flere mislykkede loginforsøg
if event[1] == "failed_login" and event[2] >= 3:
    print("Warning: Multiple failed login attempts")
    print("IP-adresse:", event[0])
