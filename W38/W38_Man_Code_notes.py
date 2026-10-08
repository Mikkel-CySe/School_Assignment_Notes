print("5>7:", 5>7) #false
print("5<7:", 5<7) #true
print("5>=7:", 5>=7) #false
print("5<=7:", 5<=7) #true

print("\nTjek om værdi 1 er større eller lig med værdi 2")
number1 = int(input("Angiv den første værdi: "))
number2 = int(input("Angiv den anden værdi: "))
print("Vi tester om værdi 1 er større eller lig med værdi 2:", number1>=number2)

#== - Lig med
#!= - Ikke lig med
#> - Større end
#< - Mindre end
#>= - Større eller lig end
#<= - Mindre eller lig med


#if - "Hvis"
#elif - "Eller hvis"
#else - "Ellers så"

print("\nTjek om du er voksen eller barn")
age_1 = int(input("Indtast din alder: "))
if age_1 >= 18:
    print("Adult")
else:
    print("Minor")


print("\nTjek af billet pris ud fra alder.")
age60 = 40
age18 = 80
age12 = 40
age_2 = int(input("Angiv din alder: "))
if age_2 >= 18:
    print(f"Din billet koster {age18}DKK")
elif age_2 < 12:
    print(f"Din billet koster {age12}DKK")

print("\nTjek af score.")
score_1 = int(input("Indtast din score: "))
if score_1 >= 90:
    print("A!")
elif score_1 >= 80:
    print("B!")
else:
    print("Below B :(")

#and - og
#or - eller
#in - inde i

print("\nTjek om brugeren må komme ind i landet med land og alder.")
age_3 = int(input("Angiv din alder: "))
country = input("Indtast end land kode (DK, AU, US): ")

if age_3 >=18 and country == "DK":
    print("Acces allowed in DK")
elif age_3 >= 18 or country == "AU":
    print("Acces allowed in EU")
elif age_3 >= 18 or country == "US":
    print("Acces allowed in US")
else:
    print("Acces not allowed")

print("\nTjek om Bob er i user list")
users1 = ["Bob", "Bo", "Alice"]
user1 = input("Indtast en user: ")
if user1 in users1:
    print(f"{user1} is on the users list")
else:
    print(f"{user1} is not on the users list")

#Test om et tal er mellem 10 og 20
print("\nDer testes som værdien er mellem 10 og 20 (begge inklusive")
number3 = int(input("Angiv din værdi: "))

if number3 >= 10 and number3 <= 20:
    print("In range")
else:
    print("Not in range")

print("\nTjek ip listen")
ips_1 = ["192.168.1.10", "192.168.1.11", "192.168.1.12", "192.168.1.13", "192.168.1.14", "192.168.1.15"]
ip = input("Indtast en ip: ")

if ip in ips_1:
    print("IP validated")
else:
    print("IP invalid")
