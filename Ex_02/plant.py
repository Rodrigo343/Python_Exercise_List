class Plant():
    
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
    
    
class Tree(Plant):

    def __init__(self, name, specie, fructiferous):
         super().__init__(name, specie)
         self.fructiferous = fructiferous

    @property  
    def fructiferous(self):
        return self.__fructiferous
    
    @fructiferous.setter  
    def fructiferous(self, fructiferous):
        self.__fructiferous = fructiferous
        
    def __str__(self):
        return super().__str__() + "\nFructiferous: {0}fructiferous".format(("" if self.fructiferous else "isn't "))          


class Carnivore(Plant):

    def __init__(self, name, specie, poisonous):
         super().__init__(name, specie)
         self.poisonous = poisonous

    @property  
    def poisonous(self):
        return self.__poisonous
    
    @poisonous.setter  
    def poisonous(self, poisonous):
        self.__poisonous = poisonous
        
    def __str__(self):
        return super().__str__() + "\nPoisonous: {0}poisonous".format(("" if self.poisonous else "isn't "))  


class Flower(Plant):

    def __init__(self, name, specie, color):
         super().__init__(name, specie)
         self.color = color

    @property  
    def color(self):
        return self.__color
    
    @color.setter  
    def color(self, color):
        self.__color = color
        
    def __str__(self):
        return super().__str__() + "\nColor: {0}".format(self.color)     