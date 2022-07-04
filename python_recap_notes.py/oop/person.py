#capitals for classes
class Person():
    def __init__(self, person_name,person_age, person_height): #constucter sets attributes
        self.name = person_name  #not really done. just put name instead of person_name.
        self.age = person_age 
        self.height = person_height

    def set_hair(self,person_hair): # setter - set info inside the class
        self.hair = person_hair

    def get_hair(self):
        print(self.hair) # getter - not used that much
        

