import animals
import habitats

class Zoo():
        
    """Menu to select a Media to rent"""
    def menu():
        option = 0
        
        while(option != 4):
        
            print("\n----Qual animal deseja adicionar----")
            print("1- Voador")
            print("2- Terrestre")
            print("3- Aquatico")
            print("4- Voltar")
            option = int(input("Select a option: "))
    
            if option == 1:                  
                print("\n----Cadastro Voador ----")
                name = input("Name: ")
                specie = input("Specie: ")
                featherColor = input("Feather Color: ")
                animal = animals.Aerial(name, specie, featherColor)
                Zoo.selectHabitat(animal)
                 
            elif option == 2:
                print("\n----Cadastro Terrestre ----")
                name = input("Name: ")
                specie = input("Specie: ")
                pawsQuantity = int(input("Paws Quantity: "))
                animal = animals.Terrestrial(name, specie, pawsQuantity)
                Zoo.selectHabitat(animal)
                
            elif option == 3:
                print("\n----Cadastro Aquatico ----")
                name = input("Name: ")
                specie = input("Specie: ")
                amphibian = ("y" == input("Amphibian? (y/n): ").lower())
                animal = animals.Aquatic(name, specie, amphibian)
                Zoo.selectHabitat(animal)

            elif option == 4:
                break
                
            else:
                print("\nInvalid Option")
    
    """Def  """                  
    def listAnimalsByHabitat():
        animalsHabitat = ""
        animalsHabitat += ("Vivarium: {0}".format(vivarium.animals))
        animalsHabitat += ("\nLake: {0}".format(lake.animals))
        animalsHabitat += ("\nCoop: {0}".format(coop.animals))
        animalsHabitat += ("\nAquarium: {0}".format(aquarium.animals))
        animalsHabitat += ("\nCage: {0}".format(cage.animals))
        
        return animalsHabitat
        
    """Def  """                  
    def animalsInZoo():
        animalsQuantity = (vivarium.animalsQuantity() + lake.animalsQuantity() + coop.animalsQuantity() +
                           aquarium.animalsQuantity() + cage.animalsQuantity())
        
        return ("{0} Animals live in zoo".format(animalsQuantity))

    """Def """                  
    def sumAerial():
        aerialTotal = (vivarium.aerialQuantity() + lake.aerialQuantity() + coop.aerialQuantity() +
                       aquarium.aerialQuantity() + cage.aerialQuantity())
        
        return ("{0} Aerials animals live in zoo".format(aerialTotal))
    
    """Def """                  
    def sumTerrestrial():
        terrestrialTotal = (vivarium.terrestrialQuantity() + lake.terrestrialQuantity() + coop.terrestrialQuantity() + 
                       aquarium.terrestrialQuantity() + cage.terrestrialQuantity())
        
        return ("{0} Terrestrials animals live in zoo".format(terrestrialTotal))
    
    """Def """                  
    def sumAquatic():
        aquaticTotal = (vivarium.aquaticQuantity() + lake.aquaticQuantity() + coop.aquaticQuantity() +
                       aquarium.aquaticQuantity() + cage.aquaticQuantity())
        
        return ("{0} Aquatic animals live in zoo".format(aquaticTotal))
    
    """Def """                  
    def countAnimalsInHabitat():
        totalAnimalsHabitat = ""
        
        totalAnimalsHabitat += "Vivarium: {0} animals".format(vivarium.animalsQuantity())
        totalAnimalsHabitat += "\nLake: {0} animals".format(lake.animalsQuantity())
        totalAnimalsHabitat += "\nCoop: {0} animals".format(coop.animalsQuantity())
        totalAnimalsHabitat += "\nAquarium: {0} animals".format(aquarium.animalsQuantity())
        totalAnimalsHabitat += "\nCage: {0} animals".format(cage.animalsQuantity())
        
        return totalAnimalsHabitat
    
    """Def """                  
    def totalAreaHabitat():
        totalArea = (vivarium.area + lake.area + coop.area + 
                       aquarium.area + cage.area)
        
        return ("{0} total habitat area".format(totalArea))
    
    """Def """        
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
        
    """Def  """                  
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
                
    """Def  """                  
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
    
    """Def  """                  
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
        print("1- Cadastrar Animal")
        print("2- Listar Animais")
        print("3- Quantidade de Animais no zoologio")
        print("4- Quantidade de animais no zoologico por tipo")
        print("5- Quantidade de animais no zoologico por habitat")
        print("6- Area total que os animais ocupam")
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





   






