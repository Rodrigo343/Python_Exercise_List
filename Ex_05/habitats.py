import animals

class Habitat():
    
    def __init__(self, area):
         self.area = area
         self.__animals = []

    @property  
    def area(self):
        return self.__area
    
    @area.setter  
    def area(self, area):
        self.__area = area
        
    @property  
    def animals(self):
        animals = ""
        
        for i in range(len(self.__animals)):
            animals += str(self.__animals[i].name) + ", "
        
        if animals == "":
            return "There aren't animals in the habitat"
        else:
            return animals
    
    @animals.setter  
    def animals(self, animal):
        self.__animals.append(animal)
        
    """Def to return total animals quantity in habitat"""
    def animalsQuantity(self):
        return len(self.__animals)
    
    """Def to return total aeria animals quantity in habitat"""
    def aerialQuantity(self):
        i = 0
        for animal in self.__animals:
            if( isinstance(animal, animals.Aerial) ):
                i += 1     
        return i
    
    """Def to return total terrestrial animals quantity in habitat"""
    def terrestrialQuantity(self):
        i = 0
        for animal in self.__animals:
            if( isinstance(animal, animals.Terrestrial) ):
                i += 1     
        return i
    
    """Def to return total aquatic animals quantity in habitat"""
    def aquaticQuantity(self):
        i = 0
        for animal in self.__animals:
            if( isinstance(animal, animals.Aquatic) ):
                i += 1      
        return i

    def __str__(self):        
        return "Area:{0}\nAnimals: {1}".format(self.area, self.animals)
    
class Vivarium(Habitat):
    def __init__(self, area):
        super().__init__(area)
        
class Lake(Habitat):
    def __init__(self, area):
        super().__init__(area)
    
class Cage(Habitat):
    def __init__(self, area):
        super().__init__(area)
    
class Coop(Habitat):
    def __init__(self, area):
        super().__init__(area)
        
class Aquarium(Habitat):
    def __init__(self, area):
        super().__init__(area)




