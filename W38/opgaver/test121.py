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