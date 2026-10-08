#Opgave A
#Gem følgende loglinje i en variabel og udskriv den:
#2026-01-01 10:15:23 LOGIN_FAILED user=admin ip=192.168.1.45
print("Opgave A")
logline = "2026-01-01 10:15:23 LOGIN_FAILED user=admin ip=192.168.1.45"
print("Loglinjen er som følgende:", logline)

#opgave B
#Udskriv hvor mange tegn loglinjen fra opgave 23 indeholder ved hjælp af len().
print("\nOpgave B")
print("Loglinjen har", len(logline),"tegn")

#Opgave C
#Udskriv loglinjen fra opgave 23 med kun store bogstaver.
print("\nOpgave C")
print("Skrevet med stort:", logline.upper())

#Opgave D
#Udskriv loglinjen fra opgave 23 med kun små bogstaver.
print("\nOpgave D")
print("Skrevet med småt:", logline.lower())

#Opgave E
#Lad brugeren indtaste en loglinje og udskriv både loglinjen og dens længde.
print("\nOpgave E")
log = input("Indskriv en loglinje: ")
print("Loglinjens længde:", len(log))
print("Din indskrevet loglinjen:", log)

#Opgave F
#Lad brugeren indtaste et brugernavn og udskriv brugernavnet to gange lige efter: den ene gang
#kun med store bogstaver, den anden gang kun med små bogstaver.
print("\nOpgave F")
username = input("Intast et brugernavn: ")
print("Brugernavnet skrevet med stort:", username.upper())
print("Brugernavnet skrevet med småt:",username.lower())

#Opgave G
#Lad brugeren indtaste en IP-adresse som tekst og udskriv hvor mange tegn den indeholder.
print("\nOpgave G")
ip =   input("Intast en IP: ")
print("IP'ens længde:", len(ip))
print("Din indskrevet IP:", ip)

#Opgave H
#Lad brugeren indtaste tre loglinjer og gem dem i tre variabler. Udskriv dem alle igen.
print("\nOpgave H")
logline1 = input("Intast den første loglinje: ")
logline2 = input("Indtast den anden loglinje: ")
logline3 = input("Indtast den tredje loglinje: ")
print("\nDe tre loglinjer er:", logline1, logline2, logline3)


#Opgave I
#Udskriv de første 10 tegn af loglinjen fra opgave A (hvilken information giver det os?).
print("\nOpgave I")
print("De 10 første tegn af loglinjen fra opgave A er:\n", logline[:10])


#Opgave J
#Udskriv de sidste 12 tegn af loglinjen fra opgave A (hvilken information giver det os?).
print("\nOpgave J")
print("De 12 sidste tegn af loglinjen fra opgave A er:\n", logline[-12:])

#Opgave K
#Lad brugeren indtaste en loglinje og udskriv de første 5 tegn (antag at disse tegn giver nyttig info).
print("\nOpgave K")
loglinek = input("Intast en loglinje: ")
print("Den 5 første tegn er:", loglinek[:5])

#Opgave L
#Lad brugeren indtaste en loglinje og udskriv både starten (første 8 tegn) og slutningen (sidste 8
#tegn) i samme linje.
print("\nOpgave L")
loglinel = input("Intast en loglinje: ")
print("De 8 første tegn af loglinjen, samt de 8 sidste tegn er:", "\nFørste 8:", loglinel[:8], "Sidste 8:", loglinel[-8:])
