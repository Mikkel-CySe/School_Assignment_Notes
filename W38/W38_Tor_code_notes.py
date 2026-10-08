print("\n--- For-loop ---")
print("range (1,6)")
for i in range (1,6):
    print(i)
#Der printes 1, 2, 3, 4, 5

print("\n")
print("range (0,11,2)")
for i in range (0,11,2):
    print(i)
#range(start, stop, step)
#Der printes 0, 2, 4, 6, 8, 10

print("\n--- For-loop og lister ---")
names = ["Anna", "Sofie", "Peter"]
for name in names:
    print(name)
#Der printes alle navnene i names.
#Anna, Sofie, Peter


print("\n--- While-loop ---")
x = 1
while x <= 5:
    print(x)
    x = x + 1
#Et while-loop kører så længe en betingelse er sand/opfyldt.
#Der printes 1, 2, 3, 4, 5
#Eksemplet kører også et bestemt antal gange, men kun fordi vi ændrer størrelsen af variablen x.

print("\n--- While demo ---")
x = 3
while x <= 5:
    print(x)
    x = x + 1
#Denne printer 3 uendeligt
#fixes med x = x + 1
#med fix, tæller den fra x til 5.


print("\n--- While loop, stop loop med break ---")
while True:
    name = input("Enter your name, type Q/q to stop: ")
    if name == "Q" or name == "q": #Her er et if-statement inde i loopet.
        break


#Denne printer Hej uendeligt
#while True:
#   print("Hej")
#Programmet spørger forsat efter navn, indtil brugere taster Q el. q, hvortil den stopper (break)
#Denne type er især godt, når man endnu ikke kender antallet af personer / navne.

print("\nCyber-eks med break")
ips = []

while True:
    ip = input("Enter your IP address, type Q/q to stop: ")
    if ip == "Q" or ip == "q":
        break
    #ips.append(ip) for at tilføje ip'en til en liste.
    ips.append(ip)

print("\nChecking ips")
for ip in ips:
    print("Checking IP:", ip)
#while True: kan også bruges til at indsætte den kommende liste i en liste.
#dernæst kan listen printes, enten ved siden af hinanden som liste, eller under hinanden.
#print("Checking IP:", ip) (ip for under hinanden) (ips for liste ved siden af hinanden)


print("\n--- Modulus %---")
#Modulus betyder hvad er rest af division i heltal.
#eks 1:
#10 % 3 = 1, da 10/3=3 , med 1 i rest.

#eks 2:
#8 % 2 = 0, 8/2=4(8), (0 i rest)
#9 % 2 = 1, 9/2=4(8), (1 i rest)
#17 % 5 = 2, 17/5=3(15), (2 i rest)
#20 % 5 = 0, 20/5=4(20), (0 i rest)
#Hvis divisionen går i 0, går divisionen op uden rest.

#Eks:
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")


print("\n--- Modulus % sammen med et for-loop")
#Vi kan gennemløbe tallene fra 1 til 10:
print("\nAlle tal printes")
for i in range (1, 11):
    print(i)
#Der printes: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

#modulus kan da bruges til kun at udskrive de lige tal:
print("\nAlle lige tal printes")
for i in range (1, 11):
    if i % 2 == 0:
        print(i)
#Der printes: 2, 4, 5, 6, 8, 10