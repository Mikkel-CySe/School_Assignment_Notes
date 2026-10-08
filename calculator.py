print("Welcome, let's start calculating.")
print("""To start, choose one of the following operations:
Type 1: Addition
Type 2: Subtraction
Type 3: Multiplication
Type 4: Division
Type 5: Type your own calculation""")

# Samler fejlbeskeden ét sted, så vi ikke skal skrive den flere gange.
def error():
    print("Please enter a valid number.")

calculator = []


while True:
    number = input("\nChoose an operation, type q/quit to exit: ")

    if number.isdigit():
        number = int(number)
        #Addition
        if number == 1:
            print("You have chosen 1: Addition")
            while True:
                addition = input("Please enter a number, or type 'result': ")
                if addition.isdigit(): # Tjekker om inputtet er et tal, ellers går den videre til else: statementet.
                    addition = int(addition)
                    calculator.append(addition) # Tallet bliver gemt i listen
                elif addition.lower() == "result": # Sørger for result/RESULT skrives som småt i koden.
                    result_addition = sum(calculator)
                    print(f"The result is {result_addition}")
                    break

                else:
                    error() # Fejlbeskrivese fra linje [11]
            continue # Starter forfra med at spørge efter en operation
        # Substraktion
        elif number == 2:
            print("You have chosen 2: Subtraction")
            while True:
                subtraction = input("Please enter a number, or type 'result': ")
                if subtraction.isdigit(): # Tjekker om inputtet er et tal, ellers går den videre til else: statementet.
                    subtraction = int(subtraction)
                    calculator.append(subtraction) # Tallet bliver gemt i listen
                elif subtraction.lower() == "result":
                    result_subtraction = calculator[0] # Det første tal bruges som startpunkt for udregningen
                    for i in range(1, len(calculator)):
                        result_subtraction -= calculator[i]
                    print(f"The result is {result_subtraction}")
                    break
                else:
                    error()
            continue # Starter forfra med at spørge efter en operation
        # Multiplikation
        elif number == 3:
            print("You have chosen 3: Multiplication")
            while True:
                multiplication = input("Please enter a number, or type 'result': ")
                if multiplication.isdigit(): # Tjekker om inputtet er et tal, ellers går den videre til else: statementet.
                    multiplication = int(multiplication)
                    calculator.append(multiplication) # Tallet bliver gemt i listen
                elif multiplication.lower() == "result":
                    result_multiplication = calculator[0] # Det første tal bruges som startpunkt for udregningen
                    for i in range(1, len(calculator)):
                        result_multiplication *= calculator[i]
                    print(f"The result is {result_multiplication}")
                    break

                else:
                    error()
            continue # Starter forfra med at spørge efter en operation

        # Division
        elif number == 4:
            print("You have chosen 4: Division")
            while True:
                division = input("Please enter a number, or type 'result': ")
                if division.isdigit(): # Tjekker om inputtet er et tal, ellers går den videre til else: statementet.
                    division = int(division)
                    calculator.append(division) # Tallet bliver gemt i listen
                elif division.lower() == "result":
                    result_addition = calculator[0] # Det første tal bruges som startpunkt for udregningen
                    for i in range(1, len(calculator)):
                        result_addition /= calculator[i]
                    print(f"The result is {round(result_addition, 2)}") # Resultatet rundes ned til 2 decimaler
                    break
                else:
                    error()
            continue # Starter forfra med at spørge efter en operation

        elif number == 5:
            print("You have chosen 5: Type your own calculation")
            calculation = input("Please enter your calculation: ")
            result = eval(calculation) # eval gør det muligt at skrive en hel matematisk beregning
            print(f"The result is {round(result,2)}") # Resultatet rundes ned til 2 decimaler

            continue # Starter forfra med at spørge efter en operation

        else:
            print("Invalid input, please enter a valid operation.")

    # Brugeren kan skrive q eller quit for at stoppe programmet
    elif number.lower() == "quit" or number.lower() == "q": # Sørger for at Q/QUIT, skrives med småt
        print("Thank you for your time!")
        break

    # Hvis input ikke er et tal, q eller quit
    else:
        print("Invalid input, please enter a valid operation.")

