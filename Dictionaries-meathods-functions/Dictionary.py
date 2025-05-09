# Dictionary

karnataka_foods = {
  "Bengalru": "Bisi Bele Bath",
  "Mysore": "Mysore Pak",
  "Mangalore": "Mangalorean Fish Curry",
    "Udupi": "Udupi Sambar"
}

print(karnataka_foods)
print(karnataka_foods["Udupi"])
print(karnataka_foods.get("Bengalru"))

# Adding and Updating a new key-value pair

karnataka_foods["shivamogga"] = "Shivamogga Ragi Mudde"
print(karnataka_foods)

# Updating an existing key-value pair
karnataka_foods["Bengalru"] = "idli"
print(karnataka_foods)

#Removing Elements from a Dictionary
 #1.pop()
mysuru_food = karnataka_foods.pop("Mysore")
print(mysuru_food)

#2.del
del karnataka_foods["Mangalore"]
print(karnataka_foods)

#3.clear
# karnataka_foods.clear()
# print(karnataka_foods)

# Dictionary Methods

#1.keys()
print(karnataka_foods.keys())

#2.values()
print(karnataka_foods.values())

#3.items()
print(karnataka_foods.items())

#4.update()
new_foods = {
    "Hassan": "Hassana Kayi"
}
karnataka_foods.update(new_foods)
print(karnataka_foods)