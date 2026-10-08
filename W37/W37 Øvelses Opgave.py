from http.cookiejar import uppercase_escaped_char

print("Indtast det antal elefanter du har set igennem hele dit liv.")
elephants=input()
elephants=int(elephants)
print("Det betyder at du har set", elephants, " elefanter")

print("Det betyder at du har set", elephants+elephants, " elefanter gennem dit liv")





#Program eksempel med kommatal
print("Indtast et kommatal vi kalder for x")
x=input()
print("Indtast et kommatal vi kalder for y")
y=input()

#Konverteres til kommatal
x=float(x)
y=float(y)

#x divideret med y
resultat=x/y
print("x-værdien divideret med y-værdien givet:", resultat)

#2 måder at lave print på
name="Mikkel"
age=21
print("Navn:", name)
print("Age:", age)

#Den formaterede print, ender i sidste ende ligesom den normale, dog er den hurtigere at skrive.
print(f"Navn: {name}")
print(f"Age: {age}")
