class JobOpportunity():
    
    def __init__(self, description, salary):
         self.description = description
         self.salary = salary
         self.__candidate = []
         
    @property  
    def description(self):
        return self.__description
    
    @description.setter  
    def description(self, description):
        self.__description = description
        
    @property  
    def salary(self):
        return self.__salary
    
    @salary.setter  
    def salary(self, salary):
        self.__salary = salary
        
    @property  
    def candidate(self):
        candidates = ""
        
        for i in range(len(self.__candidate)):
            candidates += str(self.__candidate[i].name) + ", "
            
        return candidates
    
    @candidate.setter  
    def candidate(self, candidate):
        self.__candidate.append(candidate)

    def __str__(self):        
        return "Description:{0}\nSalary: {1}\nCandidates: {2}".format(self.description, self.salary, self.candidate)

class Internship(JobOpportunity):
    
    def __init__(self, description, salary, time):
         super().__init__(description, salary)
         self.time = time

    @property  
    def time(self):
        return self.__time
    
    @time.setter  
    def time(self, time):
        self.__time = time
        
    def __str__(self):
        return super().__str__() + "\nTime: {0} Month".format(self.time)          

class Contract(JobOpportunity):
    
    def __init__(self, description, salary, temporary):
         super().__init__(description, salary)
         self.temporary = temporary

    @property  
    def temporary(self):
        return self.__temporary
    
    @temporary.setter  
    def temporary(self, temporary):
        self.__temporary= temporary
        
    def __str__(self):
        return super().__str__() + "\nTemporary: {0}temporary".format(("" if self.temporary else "isn't "))             