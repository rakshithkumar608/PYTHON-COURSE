#1. Basic Dictionary Operations:

# Create a dictionary to store information about 5 cities in Karnataka and their famous dishes.
# Add a new city and its dish to the dictionary.
# Update the dish for Bengaluru.
# Remove one city from the dictionary.
# Use the keys() method to print all city names in the dictionary.
# Use the values() method to print all dishes in the dictionary.


# Create a dictionary to store information about 5 cities in Karnataka and their famous dishes.

cars_details = {
    "Maruthi Suzuki": "india",
    "BMW": "Germany",
    "toyato": "Japan",
    "Renault": "France",
    "Ford": "USA"
}

print(cars_details)

# Add a new city and its dish to the dictionary
cars_details["Lamborgini"]= "Italy"
print(cars_details)

# Update the dish for Bengaluru.
cars_details["Maruthi Suzuki"] = "france"
print(cars_details)

# Remove one city from the dictionary.
del cars_details["BMW"]
print(cars_details)


# Use the keys() method to print all city names in the dictionary.
print(cars_details.keys())

# Use the values() method to print all dishes in the dictionary.
print(cars_details.values())


# Nested Dictionary Practice (Simple for now):

# Create a dictionary to store details of two of your friends, including their names, favorite subject, and favorite food.
# Access and print the favorite food of one friend.

friends_details = {
    "friend1": {
        "name": "John",
        "favorite_subject": "Math",
        "favorite_food": "Pizza"
    },
    "friend2": {
        "name": "Jane",
        "favorite_subject": "Science",
        "favorite_food": "Pasta"
    }
}

print(friends_details)

# Access and print the favorite food of one friend.

print(friends_details["friend1"]["favorite_food"])
# Output: Pizza