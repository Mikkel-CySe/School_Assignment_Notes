#Dyr egenskaber:
#pattedyr True/False
#art
#alder
#fødested
#vaccineret True/False

# Dyrepark case fra undervisningen.

animals_in_park = [
    {
        "pattedyr": True,
        "art": "Elefant",
        "alder": 54,
        "fødested": "Danmark",
        "vaccineret": False
    },
    {
        "pattedyr": False,
        "art": "Alligator",
        "alder": 9,
        "fødested": "Amerika, Florida",
        "vaccineret": True
    }
]


new_animal = {
        "pattedyr": True,
        "art": "Giraf",
        "alder": 21,
        "fødested": "Madagascar",
        "vaccineret": True
}

animals_in_park.append(new_animal)

print(f"Dyr i parken: \n{animals_in_park}")
