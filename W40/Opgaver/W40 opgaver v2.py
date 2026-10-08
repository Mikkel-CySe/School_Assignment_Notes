#OPGAVE 1 – KONTROL AF LOGIN-FORSØG
#Du skal lave et lille program, der spørger brugeren om antallet af mislykkede login-forsøg.
#Programmet skal blive ved med at spørge, indtil brugeren skriver:
#quit
#Eksempel:
#Enter number of failed logins or quit: 2
#2 failed login attempts
#Enter number of failed logins or quit: 7
#Warning: Many failed login attempts
#Enter number of failed logins or quit: quit
#Program stopped
#Programmet skal kontrollere brugerens input.
#Kun heltal mellem 0 og 20 er gyldige.
#Hvis brugeren skriver tekst i stedet for et tal, skal programmet skrive:
#Invalid input
#Hvis brugeren skriver et tal mindre end 0 eller større end 20, skal programmet skrive:
#Number must be between 0 and 20
#Hvis tallet er 5 eller højere, skal programmet skrive en advarsel:
#Warning: Many failed login attempts
#Ellers udskrives antallet af login-forsøg.
#Du får brug for:
#   while
#   input()
#   isdigit()
#   int()
#   if / else
#   break

print("\n--- OPGAVE 1 – KONTROL AF LOGIN-FORSØG ---")

while True:
    loginattempts = input("\nEnter number of failed logins, type Q/q to quit: ")
    if loginattempts == "q" or loginattempts == "Q":
        print("Program stopped")
        break
    if loginattempts.isdigit(): #Tjek datatype
        loginattempts = int(loginattempts) #Konvertering
        if loginattempts >= 1 and loginattempts < 5: #Mellem 1 og 5
            print(f"{loginattempts} failed login attempts")
        elif loginattempts >=5 and loginattempts <=20: #Mellem 5 og 20
            print(f"WARNING: {loginattempts} failed login attempts")
        else:
            print("Numbers must be between 1 and 20, try again!")
    else:
        print("Invalid input, must be a numeric number between 1 and 20, try again!") #Hvis input er en string










#OPGAVE 2 – KONTROL AF PORTNUMRE
#Et portnummer i TCP/IP kan være mellem 1 og 65535.
#Lav et program, som gentagne gange spørger brugeren:
#Enter port number or quit:
#Programmet skal stoppe, når brugeren skriver:
#quit
#Kontrollér først, om input er et tal.
#Hvis det ikke er et tal, udskrives:
#Invalid input
#Hvis det er et tal, skal det konverteres til int.
#Kontrollér derefter, om tallet ligger mellem 1 og 65535.
#Hvis det ikke gør, udskrives:
#Invalid port number
#Opret denne tuple:
#common_ports = (22, 80, 443)
#Hvis det indtastede portnummer findes i common_ports, skal programmet skrive:
#Common port
#Ellers skal programmet skrive:
#Other valid port
#Eksempel:
#Enter port number or quit: 443
#Common port
#Enter port number or quit: 8080
#Other valid port
#Enter port number or quit: hello
#Invalid input
#Enter port number or quit: 70000
#Invalid port number
#Enter port number or quit: quit
#Program stopped
#Du får brug for:
#   while
#   input()
#   isdigit()
#   int()
#   if / elif / else
#   in
#   tuple
#   break
print("\n--- OPGAVE 2 – KONTROL AF PORTNUMRE ---")

common_ports = (22, 80, 443) #Tuple

while True:
    port = input("\nEnter your port, type q/Q to quit: ")
    if port == "q" or port == "quit":
        print("Program stopped")
        break
    if port.isdigit(): #Tjek datatype
        port = int(port) #Konvertering
        if port in common_ports: #Tjek om porten er i tuple
            print("Common valid port")
        elif port >=1 and port <= 65535: #Mellem 1 og 65535
            print("Other valid port")
        else:
            print("Invalid port") #Hvis value er over 65535 el. = 0
    else:
        print("Invalid input, must be a positive numeric port between 1 and 65535, try again!") #Hvis input er en string.

