# Dictionary data types

#has to be a string or integer
#key and value. can not have the same name key but value can

#keys are always the 1st and values are always the 2nd


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
#print(my_cat.get("legs","this key doesn't exist")) #no fatal error and error message.

#print(my_cat.keys())
#print(list(my_cat.keys()))#makes it easier to read by making it more like a list. make it iterable/can move through it un like dictionary. only runs though keys?

#for i in my_cat.keys(): #only runs though keys?
#    print(i)

my_cat.update({"legs":"4"})# adds to diction and changes key values
print(my_cat)

my_cat.pop("legs") #removes key
#---------------------------------------------------------------------------------------------------------------------------------

Countries = {"United Kingdom":"London",
"France":"Paris", "Germany":"Berlin", "Spain":"Madrid", "Italy":"Rome"}


Countries.setdefault("Chile","Santiago")
Countries.setdefault("Japan","Tokyo")

# print(Countries.items()) # prints the whole list

for i in Countries.items():
    print(i)


# #print(list(Countries))

# #for k, v in Countries.items():
#     print(k ":" +v)

Countries.update({"United Kingdom":"English"})

print(Countries.items())





######################################

fav_songs = [
{"artist":"the protomen", "song_name":"the hounds", "genre":"rock","release_year":"2009"},

{"artist":"yonezu kenshi", "song_name":"unbelievers", "genre":"J-pop","release_year":"2015"},

{"artist":"mamamoo", "song_name":"piano man", "genre":"K-pop","release_year":"2014"}]

print(fav_songs[1]) # targets the 2nd dictionary in list - idex position 1.

fav_songs.append({"artist":"meatloaf", "song_name":"bat out of hell", "genre":"hard rock","release_year":"1977"}) #.append to update list.

del (fav_songs[1] )# removes the 2nd dictionary in list - idex position 1.
fav_songs.pop(0)#if left empty will remove item from end of the list.

fav_songs[2].update({"song_name":"piano man"}) #updates key of list item specifed.