#Dette er et program der kan fordele en regning ved et restaurant, hvori regning + drikkepenge indgår.
#Split en restaurant regning V.2

#Antal gæster
guest_amount = int(input("Angiv hvor mange gæster i er: "))

#Gæsternes navne indtastes og gemmes
guests_names = []

for x in range(1,guest_amount + 1):
    name = input("Angiv navnet på gæst " + str(x) + ": ")
    name = name.capitalize()
    guests_names.append(name)

print("Gæsternes navne er:", guests_names)

#Regningens størrelse, samt float da regningen kan være kommatal
bill = float(input("\nAngiv prisen på regningen i DKK: "))

#Drikkepenge i procent.
tip = int(input("\nAngiv hvor mange procent drikkepenge i giver: "))

#Udregningen kommer her
tip_amount = bill * (tip/100)
total_amount = bill + tip_amount
guests_bill = total_amount/guest_amount

print("\nRegningens størrelse:", bill,"DKK")
print("Drikkepenge:", tip,"%")
print("\nFordelingen af regningen:")
for name in guests_names:
    print(name, "skal betale", round(guests_bill, 2), "DKK")

print(f"Total regning med tip: {guests_bill * guest_amount}DKK")
