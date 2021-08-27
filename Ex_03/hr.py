import jobOpportunity
import candidate
from exception import ExceptionTest

class Hr():
    
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
            
    """def to add an unemployed person"""
    def addUnemployed():
        print("\n---- Unemployed Candidate ----")
        name = input("Name: ")
        age = Hr.testExceptionInt("Age: ")
        time = Hr.testExceptionInt("Time in Months: ")

            
        candidates.append(candidate.Unemployed(name, age, time)) 
        
    """def to add an employed person"""
    def addEmployee():
        print("\n---- Employee Candidate ----")
        name = input("Name: ")
        age = Hr.testExceptionInt("Age: ")
        company = input("Company name: ")
            
        candidates.append(candidate.Employee(name, age, company))  
       
    """def to add an Internship position"""    
    def addInternship():
        print("\n---- Internship ----")
        description = input("Description: ")
        salary = Hr.testExceptionFloat("Salary: ")
        time = Hr.testExceptionInt("Duration Time in Months: ")
            
        jobOpportunities.append(jobOpportunity.Internship(description, salary, time))
        
    """def to add a Contract position"""       
    def addContract():
        print("\n---- Contract ----")
        description = input("Description: ")
        salary = Hr.testExceptionFloat("Salary: ")
        temporary = ("y" == input("temporary? (y/n): ").lower())
            
        jobOpportunities.append(jobOpportunity.Contract(description, salary, temporary))
        
    """def to add a candidate in a job opportunity"""        
    def addCandidateInJob():
        
        if(jobOpportunities or candidates):
            validation = True
            while validation:
                print("\n---- Job Opportunities List ----")
                for i in range(len(jobOpportunities)):
                    print("\nID: {0}\n{1}".format(i, jobOpportunities[i]) )
                        
                jobOption = Hr.testExceptionInt("Select one to add a candidate: ")
                    
                print("\n---- Candidates  list ----")
                for i in range(len(candidates)):
                    print("\nID: {0}\n{1}".format(i, candidates[i]) )
                        
                candidateOption = Hr.testExceptionInt("Select a candidate : ")
                      
                if(jobOption <= len(jobOpportunities) and  jobOption <= len(candidates)):
                    jobOpportunities[jobOption].candidate = (candidates[candidateOption])
                    validation = False
                else:
                    print("\nInvalid option in Candidates list or Job Opportunities List")
                
        else:
            print("\nJob Opportunities List or Candidates  list is empty")
            
    """def to print the candidate list"""        
    def printCandidateList():
        
        if candidates:
            print("\n---- Candidates list ----")
            for i in range(len(candidates)):
                print("\n{0}".format(candidates[i]) )
        else:
            print("\nCandidates list is empty")
            
    """def to print the Job Opportunities list"""        
    def printJobOpportunitiesList():
        
        if jobOpportunities:
            print("\n---- Job Opportunities ----")
            for i in range(len(jobOpportunities)):
                print("\n{0}".format(jobOpportunities[i]) )
        else:
            print("\nJob Opportunities list is empty")
        
def main():

    global candidates  
    global jobOpportunities

    candidates = []
    jobOpportunities = []
    option = 0

    while(option != 8):
        
        print("\n----Options----")
        print("1- Add Unemployed Candidate")
        print("2- Add Employee Candidate")
        print("3- Add Internship")
        print("4- Add Contract")
        print("5- Add a Candidate in a Job Opportunity")
        print("6- Candidates List")
        print("7- Job Opportunities List");
        print("8- Exit")
        option = Hr.testExceptionInt("Select a option: ")

        if option == 1:
            Hr.addUnemployed()             
        
        elif option == 2:
            Hr.addEmployee()
            
        elif option == 3:
            Hr.addInternship()
        
        elif option == 4:
            Hr.addContract()
            
        elif option == 5:
            Hr.addCandidateInJob()
            
        elif option == 6:
            Hr.printCandidateList()
            
        elif option == 7:
            Hr.printJobOpportunitiesList()


        elif option == 8:
            break;
            
        else:
            print("\nInvalid Option")
           
             
if __name__ == '__main__':
    main()
        
