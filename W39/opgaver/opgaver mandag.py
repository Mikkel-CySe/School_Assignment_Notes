#Opgave 6.1 Person
# Use a dictionary to store information about a person you know.
# Store their first name, last name, age, and the city in which they live. You
# should have keys such as first_name, last_name, age, and city. Print each piece
# of information stored in your dictionary.
print("\n--- Opgave 6.1 Person ---")
person = {
    "first_name": "Frederik",
    "last_name": "Larsen",
    "age": 20,
    "City": "Vejen"
}


for key, value in person.items():
    print(f"{key}: {value}")




#Opgave 6.7 People
# Start with the program you wrote for Exercise 6-1 (page 98). Make
# two new dictionaries representing different people, and store all three dictionaries
# in a list called people. Loop through your list of people. As you loop through
# the list, print everything you know about each person.
print("\n--- Opgave 6.7 People ---")
people = [
    {
    "first_name": "Frederik",
    "last_name": "Larsen",
    "age": 20,
    "City": "Vejen"
    },
    {
    "first_name": "Aimal",
    "last_name": "Fazli",
    "age": 18,
    "City": "Esbjerg"
    },
    {
    "first_name": "Mikkel",
    "last_name": "Helligsø",
    "age": 21,
    "City": "Esbjerg"
    }
]

for person in people:
    for key, value in person.items():
        print(f"{key}: {value}")
    print()




#Opgave 6.11 Cities
# Make a dictionary called cities. Use the names of three cities as
# keys in your dictionary. Create a dictionary of information about each city and
# include the country that the city is in, its approximate population, and one fact
# about that city. The keys for each city’s dictionary should be something like
# country, population, and fact. Print the name of each city and all of the information
# you have stored about it.
print("\n--- Opgave 6.11 Cities ---")

cities = {
    "Esbjerg": {
        "country": "Denmark",
        "approx. pop.": 72000,
        "fact": "Esbjerg is known for its large harbour."
    },
    "London": {
        "country": "United Kingdom",
        "approx. pop.": 9000000,
        "fact": "London is the capital of the United Kingdom."
    },
    "New York": {
        "country": "United States",
        "approx. pop.": 8500000,
        "fact": "New York is known as The Big Apple."
    }
}

for city, city_info in cities.items():
    country = city_info["country"].title()
    approx_pop = city_info["approx. pop."]
    fact = city_info["fact"]

    print(f"City: {city}")
    print(f"Country: {country}")
    print(f"Approx. Population: {approx_pop}")
    print(f"Fact: {fact}")
    print()


