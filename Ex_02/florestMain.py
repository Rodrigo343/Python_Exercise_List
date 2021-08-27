import plant
from exception import ExceptionTest

class Florest():
    
    """def to verify and validate input """
    def testExceptionInt(message):
        exceptionConfirm = True
                
        while (exceptionConfirm):
            test = input(message)
            
            if(ExceptionTest.exceptionInt(test)): 
                test = int(test)
                exceptionConfirm = False 
                return test  
    
    """Add a Tree"""
    def addTree():
        print("\n---- Tree registration ----")
        name = input("Name: ")
        specie = input("Specie: ")
        characteristicBool = ("y" == input("Fructiferous? (y/n): ").lower())
        
        florest.append(plant.Tree(name, specie, characteristicBool))   
       
    """Add a Flower"""    
    def addFlower():
        print("\n---- Flower registration ----")
        name = input("Name: ")
        specie = input("Specie: ")
        characteristicString = input("Color: ")
        
        florest.append(plant.Flower(name, specie, characteristicString))
     
    """Add a Carnivorous plant"""    
    def addCarnivore():
        print("\n---- Carnivorous Plant registration ----")
        name = input("Name: ")
        specie = input("Specie: ")
        characteristicBool = ("y" == input("Poisonous? (y/n): ").lower())
        
        florest.append(plant.Carnivore(name, specie, characteristicBool))

    """List Plants by type"""
    def plantByType():
        tree = 0
        flower = 0
        carnivore = 0
        
        for i in florest:
            if isinstance(i, plant.Tree):
                tree += 1
        
            elif isinstance(i, plant.Flower):
                flower += 1
                
            else:
                carnivore +=1
                
        print("\nThere are:\n{0} Trees\n{1} Flowers\n{2} Carnivorous plant".format(tree, flower, carnivore))


def main():

    global florest   
    global name
    global specie
    global characteristicBool 
    global characteristicString
    global confirmation
    global option
    
    florest = []
    option = 0
    
    while(option != 7):
        
        print("\n----Options----")
        print("1- Add Tree")
        print("2- Add Flower")
        print("3- Add Carnivorous Plant")
        print("4- List Plants")
        print("5- Number of existing plants")
        print("6- Number of existing plants by type")
        print("7- Exit")
        option = Florest.testExceptionInt("Select a option: ")

        if option == 1:
            Florest.addTree()
             
        elif option == 2:
            Florest.addFlower()
            
        elif option == 3:
            Florest.addCarnivore()
            
        elif option == 4:
            for i in range(len(florest)):
                print("\n{0}".format(florest[i]) )
                
        elif option == 5:
            print("\nThere are {0} plants in the florest".format(len(florest)))
            
        elif option == 6:
            Florest.plantByType()

        elif option == 7:
            break
            
        else:
            print("\nInvalid Option")
            
             
if __name__ == '__main__':
    main()
