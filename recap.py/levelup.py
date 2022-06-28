# print("tghj")

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

def add_up():
    num1 = input("what is the 1st number you want to add up?\n")
    num2 = input("what is the s2nd number you want to add up?\n")

    try:
        print(int(num1) + int(num2))
    except:
        print("please use numbers only")
        print("try again")
        add_up()
add_up()
