# WEEK ONE - TEUSDAY - ACTIVITY 1
# message = "Welcome to Code Nation"
# messageLength = len(message) %2

# def CheckLength():
#     print(messageLength)
#     if messageLength == 0:
#         print("Message is even")
#     else:
#         print("Message is odd")
# CheckLength()



# test_srting = "welcome to code nation"

# def odd_even_checker(test_string):
#     string_len = len(test_srting)
#     if (string_len%2==0):
#         print(f"the {test_string} is even")
#     else:
#         print(f"the {test_string} is odd")




# ACTIVIY TWO

# alpha = ["a","b","c","d","e","f","g","h","i","j","k","","m","n","o","p","q","r","s","t","u", "v", "w","x","yl","z"]

# for i in alpha:
#     print(i)

# answer=int(input("type a number to see the corresponding letter"))
# answer -=1
# print(alpha[answer])




#  WEEK ONE - WEDNESDAY - ACTIVIY 1

# def is_answer_num():
#     answer = input("please enter a number")

#     try:
#         print(int(answer))
#         print(type(int(answer)))
#     except:
#         print("try again")
#         is_answer_num()

# is_answer_num()



#  ACTIVIY 2

#make dictionary
Countries = {"United Kingdom":"London",
"France":"Paris", "Germany":"Berlin", "Spain":"Madrid", "Italy":"Rome"}

# added 2 countries
Countries.setdefault("Chile","Santiago")
Countries.setdefault("Japan","Tokyo")

#I like using .items as its easier for me to read in the terminal.

print(Countries.items())

#change to language 
Countries["United Kingdom"]="English"
Countries["Spain"]= "Spanish"
Countries["Italy"] ="Spanish"
Countries["Germany"]="German"
Countries["France"]="French"
Countries["Japan"]="Japanese"
Countries["Chile"]="Spanish"

print(Countries.items())


# ACTIVITY 3


#made list items into dictionaties.
fav_songs = [
{"artist":"the protomen", "song_name":"the hounds", "genre":"rock","release_year":"2009"},

{"artist":"yonezu kenshi", "song_name":"unbelievers", "genre":"J-pop","release_year":"2015"},

{"artist":"mamamoo", "song_name":"piano man", "genre":"K-pop","release_year":"2014"}]

print(fav_songs)

# added to list
fav_songs.append({"artist":"meatloaf", "song_name":"bat out of hell", "genre":"hard rock","release_year":"1977"})

print(fav_songs)

# removed from list
fav_songs.remove({"artist":"mamamoo", "song_name":"piano man", "genre":"K-pop","release_year":"2014"})

print(fav_songs)

#changed item in list
fav_songs[0]={"artist":"the protomen", "song_name":"will of one", "genre":"hard rock","release_year":"2005"}

print(fav_songs)