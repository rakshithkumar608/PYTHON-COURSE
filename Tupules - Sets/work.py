#1. Tuple Operations:

# Create a tuple with 5 elements.
# Try to modify one of the elements. What happens?
# Perform slicing on the tuple to extract the second and third elements.
# Concatenate the tuple with another tuple.

my_tupule = ("gun", "bullet", "amg", "smg", "barrel")
print(my_tupule)

# my_tupule = ("gun", "bullet", "amg", "smg", "barrel")
# my_tupule.modify()
# print(my_tupule)

my_tupule = ("gun", "bullet", "amg", "smg", "barrel")
print(my_tupule[3:5])

my_tupule = ("gun", "bullet", "amg", "smg", "barrel")
myy_tupule = ("M4A1", "AK47", "KAR98", "MP40")
combined_tupules = my_tupule + myy_tupule
print(combined_tupules)


#2. Set Operations:

# Create two sets: one with your favorite fruits and another with your friend’s favorite fruits.
# Find the union, intersection, and difference between the two sets.
# Add a new fruit to your set.
# Remove a fruit from your set using both remove() and discard(). What happens when the fruit doesn’t exist?

set1 = {"apple", "graph", "guva"}
set2 = {"banana", "orange", "apple"}
union_set = set1 | set2
print(union_set)

set1 = {"apple", "graph", "guva"}
set2 = {"banana", "orange", "apple"}
interaction_set = set1 & set2
print(interaction_set)

set1 = {"apple", "graph", "guva"}
set2 = {"banana", "orange", "apple"}
sym_set = set1 - set2
print(sym_set)

set1 = {"apple", "graph", "guva"}
set2 = {"banana", "orange", "apple"}
sym_dif_set = set1 ^ set2
print(sym_dif_set)

set1 = {"apple", "graph", "guva"}
set1.add("cheery")
print(set1)

set1 = {"apple", "graph", "guva"}
set1.remove("apple")
print(set1)

set1 = {"apple", "graph", "guva"}
set1.discard("graph")
print(set1)

#3. Tuple and Set Comparison:

# Create a list of elements and convert it into both a tuple and a set.
# Print both the tuple and the set.
# Try to add new elements to the tuple and set. What differences do you observe?


elements = [1, 2, 4, 5, 'apple', 'papaya']

my_tupule = tuple(elements)
my_set = set(elements)

print("Tuple:", my_tupule)
print("Set:", my_set)

# Adding new elements to both

try:
    my_tupule.append(5)  # This will raise an error
except AttributeError:
    print("Cannot add elements to tuple - tuples are immutable")


    #Add elements to set
    my_set.add(45)
    print(my_set)