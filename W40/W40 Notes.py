#Eksempel på kopiering.
cities = ["Esbjerg", "Odense", "Aarhus"]

# Vi laver en kopi af den oprindelige cities liste. (Og der gemmes kopien i en ny variable)
my_cities = cities[:]

# Vi laver her en variable, som har samme værdier for det samme data.
#my_cities = cities  #Pas på, da dette ikke er en kopi


cities.append("Varde")
print(f"Oprindelig listte: {cities}")
print(f"Ny variable liste: {my_cities}")





#Lister []
#Dictionaries {}
#Tupler ()


#Tupler kan ikke ændres, og denne vil derfor give fejl.
location = (55.4765, 8.4594)
print(f"Oprindelige: {location}")

#location kan ikke ændres, ved den måde.
#location[0] = 56.0

#location kan ændres ved at override den oprindelige variable.
location = (65.4765, 8.4594)
print(f"Ny: {location}")

location2 = (55.4765, 8.4594)

for coordinates in location2:
    print(f"Ny: {coordinates}")




#Hvis vi skal have brugeren til at indtaste en numerisk værdi, og vil sørge for at de ikke skriver
#et bogstav, kan man bruge .ifdigit(), som vil konvertere stringen til en integer
#eks.

#INPUT VALIDERING
#Step 1: Tjek datatypen med .isdigit()

number2 = input("\nEnter a number: ")
if number2.isdigit():
    print("This can be converted to an integer")
else:
    print("Oops, that should have been a number!")

#Step 2: Kontrolléring og Step 3: Konvertéring
age = input("\nEnter your age: ")
if age.isdigit():
    age = int(age)
    if age >=0 and age <= 120:
        print(f"Your age is {age} and inside the allowed range")
    else:
        print(f"Your age is {age} and outside the allowed range")


#Så altså rækkefølgen er derved:
#1: Input()
#2: Kontrollér
#3: Konvertér
#4:Brug værdien


while True:
    number = input(f"\nEnter a number, press q/Q to quit: ")
    if number.isdigit():
        number = int(number)
        print(f"You entered {number}")
    elif number == "q" or number == "Q":
        break
    else:
        print("Invalid input")



#.pop
