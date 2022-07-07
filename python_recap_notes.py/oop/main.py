from person import Person

guy = Person("liam", 31, "6.7''")

katy = Person("katy", 30, "5'6''")

katy.set_hair("black")

katy.set_hair("red")


# inheritence:

# Inheritance allows us to define a class that inherits all the methods and properties from another class.
#  Parent class is the class being inherited from, also called base class.
# Child class is the class that inherits from another class, also called derived class


# encapsulation:

# It describes the idea of wrapping data and the methods that work on data within one unit. This puts restrictions on accessing variables and methods directly and can prevent the accidental modification of data.

# polymorphism:

# The literal meaning of polymorphism is the condition of occurrence in different forms.
# It refers to the use of a single type entity (method, operator or object) to represent different types in different scenarios.
#  It means that the same function name can be used for different types.
# # in some situations, the method inherited from the parent class doesn’t quite fit into the child class. In such cases, you will have to re-implement method in the child class.


# abstraction:

# Abstraction in python is defined as a process of handling complexity by hiding unnecessary information from the user
# Abstraction is used to hide internal details and show only functionalities.
# Abstraction provides access to specific part of data.