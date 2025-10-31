#build a Star class that takes a name as an argument and has getter setter and a string representation 
#of the object. Then instantiate an instance of the star


class Star:
    def __init__(self, name):
        self.name = name   

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name  

    def __str__(self):
        return "Star name: " + self.name  


star1 = Star("Sirius")
print(star1.get_name())

star1.set_name("Polaris")
print(star1)

    
