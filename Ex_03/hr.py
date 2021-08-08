import jobOpportunity
import candidate

class Hr():
    
    def addUnemployed():
        print("\n---- Unemployed Candidate ----")
        name = input("Name: ")
        age = int(input("Age: "))
        time = int(input("Time in Months: "))
            
        candidates.append(candidate.Unemployed(name, age, time)) 
    
    def addEmployee():
        print("\n---- Employee Candidate ----")
        name = input("Name: ")
        age = int(input("Age: "))
        company = input("Company name: ")
            
        candidates.append(candidate.Employee(name, age, company))  
        
    def addInternship():
        print("\n---- Internship ----")
        description = input("Description: ")
        salary = float(input("Salary: "))
        time = int(input("Duration Time in Months: "))
            
        jobOpportunities.append(jobOpportunity.Internship(description, salary, time))
        
    def addContract():
        print("\n---- Contract ----")
        description = input("Description: ")
        salary = float(input("Salary: "))
        temporary = ("y" == input("temporary? (y/n): ").lower())
            
        jobOpportunities.append(jobOpportunity.Contract(description, salary, temporary))
        
    def addCandidateInJob():
        print("\n---- Job Opportunities ----")
        for i in range(len(jobOpportunities)):
            print("\nID: {0}\n{1}".format(i, jobOpportunities[i]) )
                
        jobOption = int(input("Select one to add a candidate : "))
            
        print("\n---- Canditates list ----")
        for i in range(len(candidates)):
            print("\nID: {0}\n{1}".format(i, candidates[i]) )
                
        candidateOption = int(input("Select a candidate : "))
                
        jobOpportunities[jobOption].candidate = (candidates[candidateOption])
        
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
        option = int(input("Select a option: "))

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
            print("\n---- Canditates list ----")
            for i in range(len(candidates)):
                print("\n{0}".format(candidates[i]) )
            
        elif option == 7:
            print("\n---- Job Opportunities ----")
            for i in range(len(jobOpportunities)):
                print("\n{0}".format(jobOpportunities[i]) )

        elif option == 8:
            break;
            
        else:
            print("\nInvalid Option")
           
             
if __name__ == '__main__':
    main()
        
