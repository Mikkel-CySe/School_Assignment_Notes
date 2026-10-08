#Fejlslagne
weekdays = ["Mandag", "Tirsdag", "Onsdag", "Torsdag", "Fredag", "Lørdag", "Søndag"]

attempts = []

# Indlæs antal attempts for hver ugedag
for day in weekdays:
    antal = int(input(f"Antal fejl-loginforsøg {day}: "))
    attempts.append(antal)

# Beregninger
total = sum(attempts)
average = total / len(attempts)

least = min(attempts)
most = max(attempts)

day_least = weekdays[attempts.index(least)]
day_most = weekdays[attempts.index(most)]

# Udskriv oversigt
print("\n --- Resultat ---")

for i in range(len(weekdays)):
    print(f"{weekdays[i]}: {attempts[i]} fejl-loginforsøg")

print("\n")
print(f"Samlet antal login-forsøg: {total}")
print(f"Gennemsnit pr. dag: {round(average, 2)}")
print(f"Færrest login-forsøg: {least} ({day_least})")
print(f"Flest login-forsøg: {most} ({day_most})")