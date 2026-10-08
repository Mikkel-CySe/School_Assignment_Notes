len("hello") #Denne returnerer et tal, altså den tæller antal af bogstaver.



tekst = "Her eR En tEkst!!!"
print(len(tekst.upper()))
print(len(tekst.lower()))



#SLICER SLICER SLICER SLICER SLICER SLICER SLICER SLICER
#Ved slicing finder man variablen fra et interval til et andet
logline = "\nSolen stod lavt over byen, mens de sidste mennesker skyndte sig hjem. På hjørnet stod en gammel cykel lænet op ad en lygtepæl, som om nogen bare havde glemt den. Ingen vidste, hvor længe den havde stået der, men hver morgen var den stadig på samme sted."
print(logline) #Hele logline printes
print("Teksten har",len(logline), "tegn")

#Jeg vil gerne finde "Solen stod lavt over byen"
print(logline[:26]) #noget fra begyndelsen udskrives, altså præfix

#Jeg vil gerne finde "mens de sidste mennesker skyndte sig hjem."
print(logline[28:69]) #noget midt i udskrives

#Jeg vil gerne finde "hver morgen var den stadig på samme sted."
print(logline[-41:]) #noget fra slutningen udskrives, altså suffix


users = ["\nadmin", "alice", "bob", "root", "ip\n"]

for user in users:
    print(user)


ips = ["192.168.1.45", "10.0.0.12", "172.16.0.8"]
for ip in ips:
    print("Checking IP:",ip)



#Her er en liste af kæledyr navne.
pets = ["Muff", "Puff", "Thor", "Quark"]

count = 0

for pet in pets:
    print("Pet name:", pet)
    count = count + 1
    print("This was pet", count, "\n")

print(pets, "\nNumber of pets:",count)
print("We are done!")