import random

# # converting data types

# int()#create an integer data type
# print (int(5.4)) #floating point
# print(type(int("54"))) #string. type tells you what data tpye it is


# # casting
# balance = 100

# deposit =int(input("how much do you want to deposit"))

# balance +=deposit
# print(f"you have{balance}")

#Truthy and Falsy
#falsy values are:
# empty strings ""
# integer value 0
# floating point value 0.0
#eveything is Truthy



# print ("what is your name")
# name = input()

# if name:
#     print(f"welcome{name}")
# else:
#     print("you did submit a name")


# day = "sunday" 
# bank_hol = false

# if day == "sunday" or "saturday":
#     print("thank god! im so tired")
# else:
#     print("off to work ig")

# not operator flips the value of in

# allowed_sweets = ["m","k","e"]
# name = input("what is your name")
# while name not in allowed_sweets:
#     print("no sweets for you")
#     print("try again")
#     name = input("what is your name")

# print("you can have one")

# try/except
#similer to if/else but here to help catch any errors without breaking(fatal error) your program

# def add_up():
#     num1 = input("what is the 1st number you want to add up?\n")
#     num2 = input("what is the 2nd number you want to add up?\n")

#     try:
#         print(int(num1) + int(num2)) #if doesnt run it will run except
#     except:
#         print("please use numbers only")
#         print("try again")
#         add_up()
# add_up()

#----------------------------------

# scope

# light = False #global variable, not written in the function. if written in veriable it would be a local variable

# def light_switch():
#     global light # needed to allow change the veriable
#     if light:
#         print("whoa! its bright in here")
#         light = False
#     else:
#         print("who out the light")
#         light = True #changes the veriable to True

# light_switch()#will provent change in the veriable if  global not used
# light_switch() 



#Tuples vs list
#data in tuples can't be changed - immutable. data in list can be changed mutable

# even_nums = [2,4,6,8,10] #square brackets are lists

# even_nums.append(12)
# even_nums.insert(0,0)
# print(even_nums)

# odd_nums = (1,3,5,7,9) #tuples have normal brackets. can't be change with methods
# odd_nums.append(11)#tuples has no .append. This will not work 
# print(odd_nums)

#-------------------------------------------------------------------------------

#slice notation
#starts at specified point and slice throught the list.

# fav_songs = [
#      "The protomen - the hounds"
#      "Yonezu kenshi - unbelievers"
#      "piano man - mamamoo"]

# print(fav_songs[1:2:1]) #using silce to show the index posistion of specified item in list. show 1 and stop at 2 then step by 1 (start - stop - step) would use when you want to see more of the list.

#print(fav_songs[1]) is the same but the rest is also runnig in the background. 

#test[::-1]



# test = "TooT"

# if test == test[::-1]:
#     print(f"yes {test} it a palindrome")
# else:
#     print("its not a palindrome ")

#-----------------------------------------------------------------------------------------------------------------------

#while True

# while True: #no condition to compare to.
#     print("don't run this. it will run forever")

loop=True
while loop == True:
    print("don't run this. it will run forever")
    loop=False


#compares a variable and runs under a condition
num=random.randint(1,50)

while num%2 == 0:
    print("even")
    num=random.randint(1,50)

print("oh no odd")


################################

while True:
    num