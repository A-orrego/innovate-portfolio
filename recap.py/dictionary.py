# Dictionary data types

#has to be a string or integer
#key and value. can not have the same name key but value can




my_cat = {
    "name":"pepper",
    "colour":"black with white speckles",
    "mood":"grumpy"}

#print(my_cat[2])# index does not exist for dictionary.

#print(my_cat["colour"])

#print(f'my cat {my_cat["name"]} is {my_cat["mood"]} today')  # to use in string use '' marks instead. 




cat_keys=my_cat.keys #watch video later

my_cat["likes"]="cheese" #added to dictionary

print(cat_keys)

#print(my_cat.values())
#print(my_cat.items())#watch video later
#print(my_cat.get("name"))
#print(my_cat.get("legs","this key doesn't exist")#no fatal error and error message.

#print(my_cat.keys())
#print(list(my_cat.keys()))#makes it easier to read by making it more like a list. make it iterable/can move through it un like dictionary. only runs though keys?

#for i in my_cat.keys(): #only runs though keys?
#    print(i)

my_cat.update({"legs":"4"})# adds to diction and changes key values
print(my_cat)

my_cat.pop("legs") #removes key