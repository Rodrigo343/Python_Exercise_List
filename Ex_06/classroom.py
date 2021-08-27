import person

class Classroom():
    
    def __init__(self, name, people):
         self.name = name
         self.people = people
         
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
    def people(self):         
        people = ""
        
        for i in range(len(self.__people)):
            if isinstance(self.__people[i], person.Professor):
                people += ("Professor:\n" + str(self.__people[i].name) + "\nStudents:\n")
                break
            
        for i in range(len(self.__people)):
            if isinstance(self.__people[i], person.Student):
                people += (str(self.__people[i].name) + ", ")
            
        return people
    
    @people.setter  
    def people(self, people):
        self.__people = people
        
    """Def to list students in the classroom"""
    def listStudentsInClassroom(self):
        students = []
        
        for i in range(len(self.__people)):
            if isinstance(self.__people[i], person.Student):
                students.append(self.__people[i])
                
        return students
    
    def __str__(self):        
        return "Name:{0}\n{1}".format(self.name, self.people)