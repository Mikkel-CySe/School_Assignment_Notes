#Opgave 7.4 Pizza toppings
#Write a loop that prompts the user to enter a series of
#pizza toppings until they enter a 'quit' value. As they enter each topping, print
#a message saying you’ll add that topping to their pizza.

toppings = []

while True:
    topping = input("\nEnter your topping of choice, type Q/q to stop: ")
    if topping == "q" or topping == "Q":
        break
    print(f"I will add {topping} to your pizza.")
    toppings.append(topping)
print("Thank you for your order.")
print(f"Here is your topping list: {toppings}.")

#Opgave 7.5
#Movie Tickets (Husk også at sørge for at man kan komme ud
#af loopet igen + sørg for at gemme og udskrive en totalpris for
#alle billetter til slut i programmet)

#A movie theater charges different ticket prices depending on
#a person’s age. If a person is under the age of 3, the ticket is free; if they are
#between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is
#$15. Write a loop in which you ask users their age, and then tell them the cost
#of their movie ticket

ages = []
total_price = 0

while True:
    age = input("\nEnter your age, type Q/q to stop: ")

    if age == "q" or age == "Q":
        break

    age = int(age)
    ages.append(age)

    if age < 3:
        print(f"Your age is {age}. Your price is free.")

    elif age >= 3 and age < 12:
        print(f"Your age is {age}. Your price is $10.")
        total_price = total_price + 10

    else:
        print(f"Your age is {age}. Your price is $15.")
        total_price = total_price + 15

print(f"\nThe total price of your tickets is: ${total_price}")
print(f"Ages during the test: {ages}")


#Opgave 7.8 Deli
#Make a list called sandwich_orders and fill it with the names of various
#sandwiches. Then make an empty list called finished_sandwiches. Loop through
#the list of sandwich orders and print a message for each order, such as I made
#your tuna sandwich. As each sandwich is made, move it to the list of finished
#sandwiches. After all the sandwiches have been made, print a message listing
#each sandwich that was made.

sandwich_orders = ["Bacon", "Tuna", "Cheese"]
finished_sandwiches = []

while True:
    print(f"\nPossible sandwich orders: {sandwich_orders}")
    sandwich = input(
        "Which sandwich would you like to order? Type Q/q to stop: ")
    if sandwich == "q" or sandwich == "Q":
        break
    finished_sandwiches.append(sandwich)
    print(f"I made your {sandwich} sandwich.")

print("\nAll sandwiches have been made:")

for sandwich in finished_sandwiches:
    print(sandwich)


# Opgave 7.3 Multiples of Ten
#Ask the user for a number, and then report whether the
#number is a multiple of 10 or not

number = int(input("\nEnter a number: "))

print(f"Debug: {number}: {number % 10}")

if number == 0:
    print(f"You wrote {number}, which is not a multiple of 10!")
elif number % 10 == 0:
    print(f"{number} is a multiple of 10.")
else:
    print(f"{number} is not a multiple of 10.")