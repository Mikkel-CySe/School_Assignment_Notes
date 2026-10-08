#Dette er et program der kan fordele en regning ved et restaurant, hvori regning + drikkepenge indgår.
#Split en restaurant regning V.1

#Indput af antal gæster
guests = int(input("Angiv hvor mange gæster i er: "))

#Regningens størrelse, samt float da regningen kan være kommatal
bill = float(input("\nAngiv prisen på regningen i DKK: "))
print("Den totale regningen u. drikkepenge er da: ", bill)

#Drikkepenge i procent.
tip = int(input("\nAngiv hvor mange procent drikkepenge i giver: "))
print("I vil gerne give", tip,"% i drikkepenge.")

#Udregningen kommer her
tip_amount = bill * (tip/100)
total_amount = bill + tip_amount
guest_amount = total_amount/guests
print("\nDvs. at hele regningen inkl. procent, ligger på: ", total_amount, "DKK")
print("Hver gæst skal da betale: ", round(guest_amount, 2), "DKK")

