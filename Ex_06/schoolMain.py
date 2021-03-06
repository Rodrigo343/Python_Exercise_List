import person
import classroom
from exception import ExceptionTest

class School():

    """def to verify and validate int input """
    def testExceptionInt(message):
        exceptionConfirm = True
                
        while (exceptionConfirm):
            test = input(message)
            
            if(ExceptionTest.exceptionInt(test)): 
                test = int(test)
                exceptionConfirm = False 
                return test  
            
    """def to verify and validate float input """
    def testExceptionFloat(message):
        exceptionConfirm = True
                
        while (exceptionConfirm):
            test = input(message)
            
            if(ExceptionTest.exceptionFloat(test)): 
                test = float(test)
                exceptionConfirm = False 
                return test  
            
    """def to add a student""" 
    def addStudent():    
        print("\n----Add Student ----")
        name = input("Name: ")
        age = School.testExceptionInt("Age: ")
        course = input("Course: ")
        monthlyPayment = School.testExceptionFloat("Monthly Payment Value: ")
        student =  person.Student(name, age, course, monthlyPayment)
        students.append(student)

    """def  to add a professor""" 
    def addProfessor():
        schoolSubjectList = []
        
        print("\n----Add Professor ----")
        name = input("Name: ")
        age = School.testExceptionInt("Age: ")
        
        quantity = School.testExceptionInt("Quantity of School Subject: ")
        
        for i in range(quantity):
            schoolSubject = input("School Subject Name: ")
            if (schoolSubject and len(schoolSubject) > 3): 
                schoolSubjectList.append(schoolSubject)
            else:
                print("This School Subject won't added")
        
        salary = School.testExceptionFloat("Monthly Payment Value: ")
        professor =  person.Professor(name, age, schoolSubjectList, salary)
        professors.append(professor)

    """def  to add a classroom""" 
    def addClassroom():
        peopleList = []
        
        print("\n----Add Classrooms ----")
        name = input("Name: ")
        
        School.listProfessors()
        professor = School.testExceptionInt("Select a Professor: ")
        professor -= 1
        if(professor > len(professors) or professor == -1):
            return print("\nInvalid option, the classroom won't be added")
        else:  
            peopleList.append( professors[professor] )
        
        quantity = School.testExceptionInt("Quantity of Students in classroom: ")
        
        School.listStudents()
        for i in range(quantity):
            student = School.testExceptionInt("Select a Student: ")
            professor -= 1
            if(student > len(students) or student == -1):
                return print("\nInvalid option, the classroom won't be added")
            else:  
                peopleList.append( professors[professor] )
        
        classroomAdd = classroom.Classroom(name, peopleList)
        classrooms.append(classroomAdd)
        return print("\nClassRoom Added")
            
    """def  to list students""" 
    def listStudents():    
        j = 1
        
        print("\n---- Students ----")
        for i in students:
            print("\nId:{0}\n{1} ".format(j, i))  
            j += 1
            
    """def to list professors""" 
    def listProfessors():    
        j = 1
        
        print("\n---- Professors ----")
        for i in professors:
            print("\nId:{0}\n{1} ".format(j, i))  
            j += 1
            
    """def to list classrooms""" 
    def listClassrooms():    
        j = 1
        
        print("\n---- Classrooms ----")
        for i in classrooms:
            print("\nId:{0}\n{1} ".format(j, i))  
            j += 1
            
    """def to calculate the school profit and the classrooms profits""" 
    def calculateProfit():   
        studentsClassroom = []
        profit = 0
        totalProfit = 0
        
        for i in classrooms:
            print("\n---- {0} ----".format(i.name))
            studentsClassroom = i.listStudentsInClassroom()
            
            for j in studentsClassroom:
                profit += j.monthlyPayment
                
            print("Classroom profit = {0}".format(profit))
            totalProfit += profit
            profit = 0
            
        print("\nSchool profit = {0}".format(totalProfit))
        
    """Def to insert values in the students list"""                  
    def addStudents():
        with open('students.txt', mode = 'r') as studentsFile:
            file = studentsFile.read()
            
            file = file.split('\n')
            
            for i in file:
                fileList = i.split(';')
                name = fileList[0]
                age = int(fileList[1])
                course = fileList[2]
                monthlyPayment = float(fileList[3])
                
                students.append(person.Student(name, age, course, monthlyPayment))
                
    """Def to insert values in the professors list"""                  
    def addProfessors():
        with open('professors.txt', mode = 'r') as professorsFile:
            file = professorsFile.read()
            
            file = file.split('\n')
            
            for i in file:
                fileList = i.split(';')
                name = fileList[0]
                age = int(fileList[1])
                schoolSubject1 = fileList[2]
                schoolSubject2 = fileList[3]
                monthlyPayment = float(fileList[4])
                
                professors.append(person.Professor(name, age, [schoolSubject1, schoolSubject2], monthlyPayment))
                
    """Def to insert values in the classrooms list"""                  
    def addClassrooms():
        with open('classrooms.txt', mode = 'r') as classroomsFile:
            file = classroomsFile.read()
            
            file = file.split('\n')
            
            for i in file:
                fileList = i.split(';')
                name = fileList[0]
                person1 = professors[ int(fileList[1]) - 1]
                person2 = students[ int(fileList[2]) - 1]
                person3 = students[ int(fileList[3]) - 1]

                classrooms.append(classroom.Classroom(name, [person1, person2, person3] ))
        
def main():

    global students
    global professors
    global classrooms
    global option
    
    option = 0
    students = []
    professors = []
    classrooms = []
    option = 0

    School.addStudents()
    School.addProfessors()
    School.addClassrooms()

    while(option != 8):
        
        print("\n----Options----")
        print("1- Add Student")
        print("2- Add Professor")
        print("3- Add Classroom")
        print("4- List Students")
        print("5- List Professors")
        print("6- List Classrooms")
        print("7- List School Profit")
        print("8- Exit")
        option = School.testExceptionInt("Select a option: ")

        if option == 1:
            School.addStudent()
             
        elif option == 2:
            School.addProfessor()
            
        elif option == 3:
            School.addClassroom()
                    
        elif option == 4:
              School.listStudents()
              
        elif option == 5:
              School.listProfessors()
              
        elif option == 6:
              School.listClassrooms()
              
        elif option == 7:
              School.calculateProfit()
            
        elif option == 8:
            break
            
        else:
            print("\nInvalid Option")
        
if __name__ == '__main__':
    main()