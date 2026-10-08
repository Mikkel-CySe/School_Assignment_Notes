#Brugeren taster et meget stort tal, som gemmes som et heltal.
number = int(input("Indtast et meget stort lige tal :"))

#Modulus bruges til at teste om tallet går i 2, og derved lige el. ulige.
if number % 2 == 0:
    print(f"Tallet {number} er lige")
else:
    print(f"Tallet {number} er ulige")