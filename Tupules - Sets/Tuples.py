 # Tuples

genders = ("male", "female", (1, 2, 3), "others")
print(genders)
 
 #  tuples operations

tuple1 = (1,2, 3 , 4)
tuple2 = (5, 7,6)
combined_tuple = tuple1 + tuple2
print(combined_tuple)

# tupules Repetation

repeated_tupule = (5, 6) *4
print(repeated_tupule)

# Checking Membership


# Tuples Meathods

#1.count

my_fruits = ("orange", "apple", "graphs", "guva", "orange", "pineapple", "orange")
print(my_fruits.count("orange"))

#2.index
my_fruits = ("orange", "apple", "graphs", "guva", "orange", "pineapple", "orange")
print(my_fruits.index("guva"))


#SETS

s = {19, 208, 3, 6, 3, 3} # set is unorderd
print(type(s))

# Set Opetrations

#1.Union
set1 = {2,4,5}
set2 = {1,7,5}
union_set = set1 | set2
print(union_set)

#2.Intersection
set1 = {2,4,5}
set2 = {1,7,5}
intresection_set = set1 & set2
print(intresection_set)

#3.Difference
set1 = {2,4,5}
set2 = {1,7,5}
difference_set = set1 - set2
print(difference_set)

#4.symmetric Difference 
set1 = {2,4,5}
set2 = {1,7,5}
sym_diff_set = set1 ^ set2
print(sym_diff_set)

# Set Meathod

#1.add()

fruit_set = {"orange", "apple", "banana"}
print(fruit_set)

fruit_set = {"orange", "apple", "banana"}
fruit_set.add("cheery")
print(fruit_set)

# 2.Remove()
fruit_set = {"orange", "apple", "banana"}
fruit_set.remove("apple")
print(fruit_set)

#3.discard()
fruit_set = {"orange", "apple", "banana"}
fruit_set.discard("cheery")
print(fruit_set)

#4.pop
fruit_set = {"orange", "apple", "banana"}
fruit_set.pop()
print(fruit_set)

#5.remove
fruit_set = {"orange", "apple", "banana"}
fruit_set.remove("apple")
print(fruit_set)