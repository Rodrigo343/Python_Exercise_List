class Animal():
    
    def __init__(self, name, specie):
         self.name = name
         self.specie = specie

    @property  
    def name(self):
        return self.__name
    
    @name.setter  
    def name(self, name):
        self.__name = name
        
    @property  
    def specie(self):
        return self.__specie
    
    @specie.setter  
    def specie(self, specie):
        self.__specie = specie

    def __str__(self):        
        return "Name:{0}\nSpecie {1}".format(self.name, self.specie)

class Aerial(Animal):

    def __init__(self, name, specie, featherColor):
         super().__init__(name, specie)
         self.featherColor = featherColor

    @property  
    def featherColor(self):
        return self.__featherColor
    
    @featherColor.setter  
    def featherColor(self, featherColor):
        self.__featherColor = featherColor
        
    def __str__(self):
        return super().__str__() + "\nFeather Color: {0}".format(self.featherColor)          
    
class Terrestrial(Animal):

    def __init__(self, name, specie, pawsQuantity):
         super().__init__(name, specie)
         self.pawsQuantity = pawsQuantity

    @property  
    def pawsQuantity(self):
        return self.__pawsQuantity
    
    @pawsQuantity.setter  
    def pawsQuantity(self, pawsQuantity):
        self.__pawsQuantity = pawsQuantity
        
    def __str__(self):
        return super().__str__() + "\nPaws Quantity: {0}".format(self.pawsQuantity) 
    
class Aquatic(Animal):

    def __init__(self, name, specie, amphibian):
         super().__init__(name, specie)
         self.amphibian = amphibian

    @property  
    def amphibian(self):
        return self.__amphibian
    
    @amphibian.setter  
    def amphibian(self, amphibian):
        self.__amphibian = amphibian
        
    def __str__(self):
        return super().__str__() + "\nAmphibian: {0}amphibian".format(("" if self.amphibian else "isn't ")) 