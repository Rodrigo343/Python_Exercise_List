class Costumer():
    
    def __init__(self, code, name, age):
         self.code = code
         self.name = name
         self.age = age
        
    @property
    def code(self):
        return self.__code

    @code.setter  
    def code(self, code):
        self.__code = code
        
    @property
    def name(self):
        return self.__name   
        
    @name.setter  
    def name(self, name):
        self.__name = name
        
    @property
    def age(self):
        return self.__age
    
    @age.setter  
    def age(self, age):
        self.__age = age

    def __str__(self):        
        return "Code: {0}\nName: {1}\nAge: {2}".format(self.code, self.name, self.age)
