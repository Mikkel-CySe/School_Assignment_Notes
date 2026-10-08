#5.3 Alien Colors, 5.4
alien_color = input("Enter the color of the alien (green, yellow, red): ")
if alien_color == "green":
    print("You earned 5 points")
else:
    print("You have earned 10 points")



#5.5 Alien Colors
alien_color2 = input("\nEnter the color of the alien (green, yellow, red): ")
if alien_color2 == "green":
    print("You earned 5 points")
elif alien_color2 == "yellow":
    print("You earned 10 points")
elif alien_color2 == "red":
    print("You earned 15 points")
else:
    print("No points")



#5.6 Stages of life
age = int(input("\nEnter the age of a fictional person: "))
if age <2:
    print("The person is a baby")
elif age <4:
    print("The person is a toddler")
elif age <13:
    print("The person is a kid")
elif age <20:
    print("The person is a teenager")
elif age <65:
    print("The person is an adult")
else:
    print("The person is an elder")


#5.10 Checking usernames
print("\nChecking usernames")
current_users = ["mandag", "tirsdag", "onsdag", "torsdag", "fredag"]
new_users = ["montag", "tirsdag", "onsdag", "donnerstag", "freitag"]

index = 0

for user in new_users:
    if user in current_users and new_users:
        print(f"Username: {user} already exists")

print("\n")
for index in range(len(current_users)):
    for user in new_users:
        if user == current_users[index]:
            print(f"Username: {user} already in use")