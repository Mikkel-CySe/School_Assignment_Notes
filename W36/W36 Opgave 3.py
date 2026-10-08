# Beder om to variable, som brugeren angiver
tal1=input("Angiv dit første tal: ")
tal2=input("Angiv dit andet tal: ")

# Konvertere tal1 og tal2 værdierne til tal, fremfor tekst (string til integer)
tal1=int(tal1)
tal2=int(tal2)

# Beregner følgende:
summen=tal1+tal2
forskellen=tal1-tal2
produkt=tal1*tal2

# Sørger for at forskellen er givet i positive tal
if forskellen<0:
    forskellen=-forskellen

# Printer værdiernes resultater.
print("\nSummen af dine to tal vil da være:", summen)
print("Forskellen mellem dine to tal vil da være:", forskellen)
print("Produktet af dine to tal vil da være:", produkt)