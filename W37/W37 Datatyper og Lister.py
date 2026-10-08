#int=heltal Eksempel er 5, 10, -3 (Int=Integer)

#float=decimaltal Eksempel 3.5, 0.25 (Bemærk at det er punktum og ikke komma)

#Opløftning i potens a^b, skrives ved a**b, eks. 5 opløftet i 2

angreb=5
print(angreb**2)

#Denne bruges typisk til at beregne hvor mange angreb der er på enheden
#Så eksemplet ovenfor er der et angreb med 5, og den opløftes i to, for at finde

avg=(10+12+8)/3
print(avg)


#Angiv hvor mange decimaler tallet skal være:
#round(guest_amount, 2)


#Lister er det samme som arrays.
#De angives ved [] og adskilles ved, eks:
#Ved navne angives adskillingerne ved "", men ved tal ej.
numbers = [1, 2, 3]
names = ["Bob", "Alice", "David"]
print(names, numbers)
print("Navn 0 er: ", names[0])
print("Navn 1 er: ", names[1])
print("Navn 2 er: ", names[2])

#En liste er mutable, altså den kan forandres.
users=["Admin", "Root", "Bob", "Alice", "David"]
users[1]="Charlie"
print("Den oprindelige users lise er: ", users)
users.append("Anders")
print("Navn tilføjet til:", users)
users.remove("Anders")
print("Navnet er nu fjernet fra:", users)

users.sort()
print("Her er en sorteret liste: ", sorted(users))