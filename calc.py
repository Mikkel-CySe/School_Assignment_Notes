print("Welcome, let's start calculating.")
print("""To start, choose one of the following:
Type 1: Addition
Type 2: Subtraction
Type 3: Multiplication
Type 4: Division
Type 5: Type your own calculation""")

calculator = []


while True:
    number = input("\nChoose an operation: ")

    if number.isdigit():
        number = int(number)
        if number == 1:
            print("You have chosen 1: Addition")
            while True:
                addition = input("Please enter a number, or type 'result': ")
                if addition.isdigit():
                    addition = int(addition)
                    calculator.append(addition)
                elif addition.lower() == "result":
                    result_addition = sum(calculator)
                    print(f"The result is {result_addition}")
                    break

                else:
                    print("Please enter a valid number or type 'result'.")
            break

        elif number == 2:
            print("You have chosen 2: Subtraction")
            while True:
                subtraction = input("Please enter a number, or type 'result': ")
                if subtraction.isdigit():
                    subtraction = int(subtraction)
                    calculator.append(subtraction)
                elif subtraction.lower() == "result":
                    result_subtraction = calculator[0]
                    for i in range(1, len(calculator)):
                        result_subtraction -= calculator[i]
                    print(f"The result is {result_subtraction}")
                    break
                else:
                    print("Please enter a valid number or type 'result'.")
            break
        elif number == 3:
            print("You have chosen 3: Multiplication")
            while True:
                multiplication = input("Please enter a number, or type 'result': ")
                if multiplication.isdigit():
                    multiplication = int(multiplication)
                    calculator.append(multiplication)
                elif multiplication.lower() == "result":
                    result_multiplication = calculator[0]
                    for i in range(1, len(calculator)):
                        result_multiplication *= calculator[i]
                    print(f"The result is {result_multiplication}")
                    break

                else:
                    print("Please enter a valid number or type 'result'.")
            break

        elif number == 4:
            print("You have chosen 4: Division")
            while True:
                division = input("Please enter a number, or type 'result': ")
                if division.isdigit():
                    division = int(division)
                    calculator.append(division)
                elif division.lower() == "result":
                    result_addition = calculator[0]
                    for i in range(1, len(calculator)):
                        result_addition /= calculator[i]
                    print(f"The result is {result_addition}")
                    break
                else:
                    print("Please enter a valid number or type 'result'.")
            break

        else:
            print("That operation isn't implemented yet.")
    else:
        print("Invalid input, please enter a operation.")