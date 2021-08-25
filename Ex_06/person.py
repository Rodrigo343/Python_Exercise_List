class Person():
    
    def __init__(self, name, age):
         self.name = name
         self.age = age

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
        return "Name:{0}\nAge: {1}".format(self.name, self.age)
    
    
class Student(Person):

    def __init__(self, name, age, course, monthlyPayment):
         super().__init__(name, age)
         self.course = course
         self.monthlyPayment = monthlyPayment

    @property  
    def course(self):
        return self.__course
    
    @course.setter  
    def course(self, course):
        self.__course = course
        
    @property  
    def monthlyPayment(self):
        return self.__monthlyPayment
    
    @monthlyPayment.setter  
    def monthlyPayment(self, monthlyPayment):
        self.__monthlyPayment = monthlyPayment
        
    def __str__(self):
        return super().__str__() + "\nCourse: {0}\nMonthly Payment: {1}".format(self.course, self.monthlyPayment)          


class Professor(Person):

    def __init__(self, name, age, schoolSubject, salary):
         super().__init__(name, age)
         self.schoolSubject = schoolSubject
         self.salary = salary

    @property  
    def schoolSubject(self):       
        
        schoolSubjectList = ""
        
        for i in self.__schoolSubject:
            schoolSubjectList += (str(i) + ", ")
        
        return schoolSubjectList
    
    @schoolSubject.setter  
    def schoolSubject(self, schoolSubject):
        self.__schoolSubject = schoolSubject
        
    @property  
    def salary(self):
        return self.__salary
    
    @salary.setter  
    def salary(self, salary):
        self.__salary = salary
        
    def __str__(self):
        return super().__str__() + "\nSchool Subject: {0}\nSalary: {1}".format(self.schoolSubject, self.salary)  