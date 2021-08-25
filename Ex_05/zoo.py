import animals
import habitats

class Zoo():
        
    """Menu to add an animal and select a habitat"""
    def menu():
        option = 0
        
        while(option != 4):
        
            print("\n----Add Animal----")
            print("1- Aerial")
            print("2- Terrestrial")
            print("3- Aquatic")
            print("4- Back")
            option = int(input("Select a option: "))
    
            if option == 1:                  
                print("\n----Add Aerial ----")
                name = input("Name: ")
                specie = input("Specie: ")
                featherColor = input("Feather Color: ")
                animal = animals.Aerial(name, specie, featherColor)
                Zoo.selectHabitat(animal)
                 
            elif option == 2:
                print("\n----Add Terrestrial ----")
                name = input("Name: ")
                specie = input("Specie: ")
                pawsQuantity = int(input("Paws Quantity: "))
                animal = animals.Terrestrial(name, specie, pawsQuantity)
                Zoo.selectHabitat(animal)
                
            elif option == 3:
                print("\n----Add Aquatic ----")
                name = input("Name: ")
                specie = input("Specie: ")
                amphibian = ("y" == input("Amphibian? (y/n): ").lower())
                animal = animals.Aquatic(name, specie, amphibian)
                Zoo.selectHabitat(animal)

            elif option == 4:
                break
                
            else:
                print("\nInvalid Option")
    
    """Def to list animals by habitat"""                  
    def listAnimalsByHabitat():
        animalsHabitat = ""
        animalsHabitat += ("Vivarium: {0}".format(vivarium.animals))
        animalsHabitat += ("\nLake: {0}".format(lake.animals))
        animalsHabitat += ("\nCoop: {0}".format(coop.animals))
        animalsHabitat += ("\nAquarium: {0}".format(aquarium.animals))
        animalsHabitat += ("\nCage: {0}".format(cage.animals))
        
        return animalsHabitat
        
    """Def to count animals in zoo """                  
    def animalsInZoo():
        animalsQuantity = (vivarium.animalsQuantity() + lake.animalsQuantity() + coop.animalsQuantity() +
                           aquarium.animalsQuantity() + cage.animalsQuantity())
        
        return ("{0} Animals live in zoo".format(animalsQuantity))

    """Def to sum aerial animals"""                  
    def sumAerial():
        aerialTotal = (vivarium.aerialQuantity() + lake.aerialQuantity() + coop.aerialQuantity() +
                       aquarium.aerialQuantity() + cage.aerialQuantity())
        
        return ("{0} Aerials animals live in zoo".format(aerialTotal))
    
    """Def to sum terrestrial animals """                  
    def sumTerrestrial():
        terrestrialTotal = (vivarium.terrestrialQuantity() + lake.terrestrialQuantity() + coop.terrestrialQuantity() + 
                       aquarium.terrestrialQuantity() + cage.terrestrialQuantity())
        
        return ("{0} Terrestrials animals live in zoo".format(terrestrialTotal))
    
    """Def to sum aquatic animals"""                  
    def sumAquatic():
        aquaticTotal = (vivarium.aquaticQuantity() + lake.aquaticQuantity() + coop.aquaticQuantity() +
                       aquarium.aquaticQuantity() + cage.aquaticQuantity())
        
        return ("{0} Aquatic animals live in zoo".format(aquaticTotal))
    
    """Def to count animals in habitat"""                  
    def countAnimalsInHabitat():
        totalAnimalsHabitat = ""
        
        totalAnimalsHabitat += "Vivarium: {0} animals".format(vivarium.animalsQuantity())
        totalAnimalsHabitat += "\nLake: {0} animals".format(lake.animalsQuantity())
        totalAnimalsHabitat += "\nCoop: {0} animals".format(coop.animalsQuantity())
        totalAnimalsHabitat += "\nAquarium: {0} animals".format(aquarium.animalsQuantity())
        totalAnimalsHabitat += "\nCage: {0} animals".format(cage.animalsQuantity())
        
        return totalAnimalsHabitat
    
    """Def to show the total area of habitats """                  
    def totalAreaHabitat():
        totalArea = (vivarium.area + lake.area + coop.area + 
                       aquarium.area + cage.area)
        
        return ("{0} total habitat area".format(totalArea))
    
    """Def to select an habitat"""        
    def selectHabitat(animal):
        option = 0
        
        print("\n---- Habtats ----")
        print("1- Vivarium")
        print("2- Lake")
        print("3- Coop")
        print("4- Aquarium")
        print("5- Cage")
        option = int(input("Select a option: "))
        
        if option == 1:
            vivarium.animals = animal
            
        elif option == 2:
            lake.animals = animal
            
        elif option == 3:
            coop.animals = animal
            
        elif option == 4:
            aquarium.animals = animal
            
        elif option == 5:
            cage.animals = animal
        
        else:
            print("\nInvalid Option")     
        
    """Def to add aerial animal"""                  
    def addAerial():
        with open('aerial.txt', mode = 'r') as aerials:
            file = aerials.read()
            
            file = file.split('\n')
            
            for i in file:
                fileList = i.split(';')
                name = fileList[0]
                specie = fileList[1]
                featherColor = fileList[2]
                
                animal = animals.Aerial(name, specie, featherColor)
                vivarium.animals = animal
                
    """Def to add terrestrial animal"""                  
    def addTerrestrial():
        with open('terrestrial.txt', mode = 'r') as terrestrials:
            file = terrestrials.read()
            
            file = file.split('\n')
            
            for i in file:
                fileList = i.split(';')
                name = fileList[0]
                specie = fileList[1]
                pawsQuantity = int(fileList[2])
                
                animal = animals.Terrestrial(name, specie, pawsQuantity)
                cage.animals = animal
    
    """Def to add aquatic animal"""                  
    def addAquatic():
        with open('aquatic.txt', mode = 'r') as aquatics:
            file = aquatics.read()
            
            file = file.split('\n')
            
            for i in file:
                fileList = i.split(';')
                name = fileList[0]
                specie = fileList[1]
                amphibian = bool(fileList[2])
                
                animal = animals.Aquatic(name, specie, amphibian)
                lake.animals = animal
        
def main():    
             
    global vivarium
    global lake
    global coop
    global aquarium
    global cage
    global option
    
    vivarium = habitats.Vivarium(15)
    lake  = habitats.Lake(200)
    coop  = habitats.Coop(10)
    aquarium  = habitats.Aquarium(50)
    cage  = habitats.Cage(250)
    option = 0

    Zoo.addAerial()
    Zoo.addTerrestrial()
    Zoo.addAquatic()

    while(option != 7):
        
        print("\n----Options----")
        print("1- Add Animal")
        print("2- List Animals")
        print("3- Animals quantity in zoo")
        print("4- Animals quantity in zoo by type")
        print("5- Animals quantity in zoo by habitat")
        print("6- Total Habitat area")
        print("7- Sair")
        option = int(input("Select a option: "))
        
        if option == 1:
            Zoo.menu()
             
        elif option == 2:
            print(Zoo.listAnimalsByHabitat())
            
        elif option == 3:
            print(Zoo.animalsInZoo())
        
        elif option == 4:
            print(Zoo.sumAerial())
            print(Zoo.sumTerrestrial())
            print(Zoo.sumAquatic())
            
        elif option == 5:
            print(Zoo.countAnimalsInHabitat())
            
        elif option == 6:
            print(Zoo.totalAreaHabitat())
            
        elif option == 7:
            break
            
        else:
            print("\nInvalid Option")
        
if __name__ == '__main__':
    main()





   






