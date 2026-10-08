
#Mit første program.

#Den indlæser en værdi, i dette tilfælde skal man indsætte navn og alder
name=input("Indtast dit navn? ")
age=input("Indtast din alder i hele år? ")

#Her vil den konvertere age til tal fremfor tekst, og derfor kan den beregenes senere.
age=int(age)
#Den sørger for at navnet starter med stort bogstav
name=name.capitalize()

#Efter at have indsat navn og alder, da vil den printe "Hej navn" og "Du er x år gammel"
print("Hej",name)
print("Du er", age, "år gammel")

#Beregn år + 1
next_year=age+1
next_five_year=age+5
#Print, næste år vil du være:
print("Næste år vil du være:", next_year, "år gammel")
print("Om 5 år vil du være:", next_five_year, "år gammel")