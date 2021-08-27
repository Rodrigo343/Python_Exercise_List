class Candidate():
    
    def __init__(self, name, age):
         self.name = name
         self.age = age

    @property  
    def name(self):
        return self.__name
    
    @name.setter  
    def name(self, name):
        if(len(name) > 3):
            self.__name = name
        else:
            self.__name = "Generic"
        
    @property  
    def age(self):
        return self.__age
    
    @age.setter  
    def age(self, age):
        if age >= 18:
            self.__age = age
        else:
            self.__age = 18

    def __str__(self):        
        return "Name:{0}\nAge: {1}".format(self.name, self.age)

class Employee(Candidate):
    
    def __init__(self, name, age, company):
         super().__init__(name, age)
         self.company = company

    @property  
    def company(self):
        return self.__company
    
    @company.setter  
    def company(self, company):
        if(len(company) > 3):
            self.__company = company
        else:
            self.__company = "Generic"
        
    def __str__(self):
        return super().__str__() + "\nCompany: {0}".format(self.company)          

class Unemployed(Candidate):

    def __init__(self, name, age, time):
         super().__init__(name, age)
         self.time = time

    @property  
    def time(self):
        return self.__time
    
    @time.setter  
    def time(self, time):
        self.__time = time
        
    def __str__(self):
        return super().__str__() + "\nTime: {0} months".format(self.time)          