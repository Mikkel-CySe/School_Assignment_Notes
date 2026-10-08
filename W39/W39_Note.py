
server1 = {
    "name1": "server01",
    "status1": "online1"
}

#"name" er en key, "status" er en key
#"server01" er den tilhørende value, "online" er den tilhørende value

#Her hentes værdier fra sin dictionary
print("\n--- Afhentning af værdi fra dictionary ---")

server2 = {
    "name2": "server02",
    "ip2": "192.168.1.20",
    "status2": "offline2"
}

print(f"Server name: {server2["name2"]}")
print(f"Server ip: {server2["ip2"]}")

#Der printes:
#server02
#192.168.1.20

#Fælles kodning af eks. til dictionary
print("\n--- Fælles dictionary test ---")
animals = {
    "elephant": "Hannibal",
    "lion": "Leo",
    "zebra": "Mark"
}
print(f"Animal name: {animals["elephant"]}")



#Man kan se på koden at det er en dictionary ved at teksten har xyz["x"].
#Hvor man i en list tilforskel skriver koden som xyz[0].



#Man kan tilføje værdier til en dictionary ved =, eks:
print("--- Tilføj til dictionary ---")
server3 = {
    "name3": "server03",
    "status3": "online3"
}

server3["ip3"] = "192.168.1.30"

print(f"Server3 info: {server3}")



#Erklæring af dictionary server4[]
print("\n--- Erklæring af dictionary ---")
server4 = {}

server4["name"] = "server04"
server4["ip"] = "192.168.1.20"
server4["status"] = "online"
print(server4)



#Fjern fra dictionary
print("\n--- Fjern status fra dictionary ---")
server5 = {
    "name": "server01",
    "ip": "192.168.1.20",
    "status": "online"
}
print(f"Server5 før fjernelse af status {server5}")
del server5["status"]
print(f"Server5 efter fjernelse af status {server5}")


#Vi kan bruge get og set til at hhv. at sætte og få værdier
#Ved .get kan man bruge den til at give en respons til brugeren, hvis deres login ikke kan findes.
#Altså at den er en pre-defineret fejl.
#get kan bruges ved eks:
print("\n--- .get pre-fejl fra dictionary ---")
location = server5.get("location", "Unknown")
print(f"Location: {location}")


#Lad sige at man gennemløbe alle key-value par, det gøres som følgende:
#Siges som: Opslag under key er value (opslag under name er server06) osv.
print("\n--- Gennemløb alle key-value par ---")
animals = {
    "elephant": "Hannibal",
    "lion": "Leo",
    "zebra": "Mark"
}
print("Animal information")
for key, value in animals.items():
    print(f"The {key} is named: {value}")


#En liste af dictionaries
print("\n--- Dictionary i en liste ---")
#Man søger derfor først i listen, og derefter dictionarien.
#hvert element nedenfor beskriver en server.
servers = [
    {"name": "web01", "status": "online"},
    {"name": "db01", "status": "online"},
    {"name": "backup01", "status": "offline"}
]
#Dette kaldes nesting
#Combination af 4 forskellige kodeteknikker
print(" ")
for server in servers:
    if server["status"] == "online":
        print(f"{server["name"]} is online")
    elif server["status"] == "offline":
        print(f"Warning! {server["name"]} is offline")


#En value kan også være en liste.
print("\n--- Value kan være en liste ---")
user = {
    "username": "Anna",
    "roles": ["user", "admin"]
}


for role in user["roles"]:
    print(f"Roles in user: {user["username"]}: {role}")


#Dictionary i en dictionary
print("\n--- Dictionary i en dictionary  ---")
users1 = {
    "Anna": {
        "role": "admin",
        "active": True
    },
    "Peter": {
        "role": "user",
        "active": False
    }
}