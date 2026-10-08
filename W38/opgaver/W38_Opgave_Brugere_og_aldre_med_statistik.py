#Opgave Brugere og aldre med statistik
#I denne opgave skal løse disse underopgaver:
#Først laves en liste med 8 fornavne på personer (gemt som strings)
#Nu skal I lave en ny tom liste (der senere skal indeholde tal).
#I denne liste skal brugernes alder, (indtastes fra tastaturet) placeres (Husk at konvertere tekst til int).
#Programmet skal nu udregne gennemsnittet af brugernes alder.
#Til slut skal udskrives en oversigt over brugere og aldre (brug print-f) samt gennemsnittet.

names = ["Mikkel", "Frederik", "Jakob", "Rasmus", "Milan", "Aimal", "Dennis", "Bob"]
ages = []

for name in names:
    age = int(input(f"What is {name}'s age: "))
    ages.append(age)

average = sum(ages) / len(ages)

print("\n --- Resultat ---")
for index in range(len(ages)):
    print(f"{names[index]} is {ages[index]} years old")

print(f"Average age: {round(average, 2)} years old")