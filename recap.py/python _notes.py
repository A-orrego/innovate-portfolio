# # this is how to show info you  dont want to show in the terminal.



# print("Recap of python learnt in LVL 2 course")

# greeting = "hello everyone"

# print(greeting)

# # basic data types
# print("this is a string displaying characters") #this is a string
# print(1234+1)#this is an interger/whole number
# print(12.34) #this is a floating number
# print(True) #one of the boolean data type
# print(False) #one of the booleans
# print(None) #none - black/null data

# #methods change or gives propoties in a string dot notation
# print(len(greeting))#len gives the lenth 
# print(greeting[1]) #index find the position of the specified letter. use -1 to get the last letter
# print(greeting.upper())#brings to uppercase. needs brackets at the end.
# print("HELLO".lower) #brings to lowercase 
# print("hello".capitalize)
# print("food mood".count("o"))#
# print("that".find("t"))#gives the lowest index position
# print("the frog is fat".replace("fat","fast"))
# print("the frog is fast     ".strip())#removes spaces from beginning and end of a sentence. giving an argument also to strip words from beginning to end specified point

# #libraries is a library in python. imports every method in library it avoid the use - from random import random uniform randint
# from ast import Assign, operator
# from doctest import FAIL_FAST
# from inspect import Parameter

import random

# print(random.random())
# print(random.uniform(1,10))
# print(random.randint(1,10))



# #snake_case is a naming convention. rule- all lowercase with an underscore to connect words

# #veriables are like boxes for info
# my_name="tilly"
# my_age=26
# money=False

# print(my_name,my_age,money)

# #concatination can only work on string data types 
# print("my name is",my_name)
# print ("i am" + my_name)
# print ("i am", my_name)


# print("hello my name is{} and i am {} years old".format(my_name, my_name))# old method of formatinguese {} as placeholders for the veriables, used to be best practice. data is filled in based on order of 

# #new method is an f-string.
# print(f"hello my name is{my_name} and i am {my_age} years old")

# #operators
# # = Assignment operator




#arithmice operator
# print(1+2)#addition
# print(3-2)#subtraction
# print(3*3)#muitiplication
# print(3**3)#squered
# print(6/2)#division
# print(15%3)#gives reminder

# # comparison operator
# #==


# balance=100
# amount=20

# balance=amount+balance
# print(balance)

# balance +=amount # more efficiant way. must be += way around 


# #replaces string with user input. \n breaks the line p
# answer=input("what is your name \n")

# #then prints veriables with users name
# print(answer)

# # if else 

# music = "Classical"

# if music.lower == "lassical":
#     print("oh no, its classical")
# elif music == ("no music"):
#     print("ahh, peace and quite")
# else:
#     print("turn it up")


# # comparison operator
# # == equal to
# # != not equal to
# # >  >=
# # <  <=
# print(10%2==0)#checks if the equation is equal to 0 and well return a boolean of true or false

# num = 10
# num2 = 20 

# if num > num2:
#     print(f"{num} is bigger")
# elif num2 > num:
#     print(f"{num2} is bigger")
# else:
#     print(f"both are equal")

# #logical operators
# place = "MCR"
# weather = "Rainy"

# if place == "MCR" and weather == "sunny":
#     print("hghg")
# elif place == "MCR" and weather == "cloudy":
#     print("vndj")
# else:
#     print("obvs")

# day = "sunday" 
# bank_hol = false

# if day == "sunday" or "saturday":
#     print("thank god! im so tired")
# else:
#     print("off to work ig")

#----------------------------------------------------------

# # Functions  

# # defining a function 
# #def names the function

# def light_switch():
#     print("its getting dark")
#     print("time to turn on the lights")

# light_switch() 
# light_switch() 
# light_switch()#calls the function. can call the function as many times as you want.

# #giving paramiters (dif from arguments)
# #  argument that fill in the Parameter

# def cash_withdraw(amount, accom):
#     print(f"you have withdrawn {amount} from {accom}")# give para data when you call the function

# cash_withdraw(300,12345678) # must be written in the order you have specified

#----------------------------------------------------------

# #list

# fav_songs = [
#     "The protomen - the hounds"
#     "Yonezu kenshi - unbelievers"
#     "piano man - mamamoo"
# ]
# print(fav_songs)


# fav_songs[0] ="Yonezu kenshi - unbelievers"# index position changes the posision in the list 

# fav_songs = [
#     "The protomen - the hounds"
#     "Yonezu kenshi - unbelievers"
#     "piano man - mamamoo"]

# fav_songs.append(" piano man")#add to the end of the list

# fav_songs.pop()# removes item from end of list. can also support index position to remoove items
#----------------------------------------------------------


#for loops for as many thing as it can sequence through

# fav_songs = [
# "The protomen - the hounds\n"
# "Yonezu kenshi - unbelievers\n"
# "piano man - mamamoo\n"]

#for i in fav_songs: # cycles through the list
#    print(i)

#for i in range(10):#0 is the beginnig value, ten is the stop value
#    print(i)

# for i in range(2,10,2):# 2- start, 10 -stop, 2step
#     print(i)

#for i in range(10,-1,-1):
#    print(i)


#while loops
#ctrl+c to stop a while loop

# num = 0
# while num < 10:
#     num +=1    # adds 1 to num if not add num will always be less than 10 and will run forever
#     print(num)

# my_num = 13
# comp_num = random.randint(1,50)

# while my_num != comp_num:
#     print(f"the nums {my_num} and {comp_num} match")
#     comp_num = random.randint(1,50) #this step changes the number
# print(f"the numbers match")

