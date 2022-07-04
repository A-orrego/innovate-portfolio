class Character():
    def __init__(self,real_name, superhero_name):
        self.real_name = real_name
        self.superhero_name = superhero_name


    def set_power(self, super_power):
        self.power = super_power

    def get_power(self):
        print(self.power)