import media
import costumer
import rent

class rentalCompany():
        
    """Menu to select a Media to rent"""
    def menuMedia():
        option = 0
        mediaOption = 0
        costumerOption = 0
        
        
        while(option != 4):
        
            print("\n----Select a media to rent----")
            print("1- Movie")
            print("2- Book")
            print("3- Game")
            print("4- Back")
            option = int(input("Select a option: "))
    
            if option == 1:           
                mediaOption = rentalCompany.selectMedia(1)
                costumerOption = rentalCompany.selectCostumer()
                rentalCompany.addRent(mediaOption, costumerOption)
                 
            elif option == 2:
                mediaOption = rentalCompany.selectMedia(2)
                costumerOption = rentalCompany.selectCostumer()
                rentalCompany.addRent(mediaOption, costumerOption)
                
            elif option == 3:
                mediaOption = rentalCompany.selectMedia(3)
                costumerOption = rentalCompany.selectCostumer()
                rentalCompany.addRent(mediaOption, costumerOption)

            elif option == 4:
                break
                
            else:
                print("\nInvalid Option")
    
    """def to show and select the media """
    def selectMedia(optionMedia):   
        print("\n---- Medias Available ----")
        for i in medias:
            if isinstance(i, media.Movie) and optionMedia == 1:
                if (i.rented is not True):
                    print("\n{0}".format(i))
                    
            elif isinstance(i, media.Book) and optionMedia == 2:
                if (i.rented is not True):
                    print("\n{0}".format(i))
                    
            elif isinstance(i, media.Game) and optionMedia == 3:
                if (i.rented is not True):
                    print("\n{0}".format(i))
                          
        return (int(input("\nSelect a option: ")) - 1)
    
    """def to show and select  a costumer"""
    def selectCostumer():    
        print("\n---- CLientes ----")
        for i in costumers:
            print("\n{0}".format(i))  
        
        return (int(input("\nSelect a option: ")) - 1)
         
    """def to show and select a rent"""
    def selectRent():    
        j = 0
        
        print("\n---- Costumers ----")
        for i in rents:
            j  += 1
            print("\nId:{0}\n{1} ".format(j, i))  
            
        return (int(input("\nSelect a option: ")) - 1)
                                              
    """Def to add a rent in the list"""
    def addRent(mediaOption, costumerOption):
        paid = False
        resp = input("Do you want pay now? (y/n) ")
        
        if(resp == "y"):
            print("You need to pay {0} dollars".format(medias[mediaOption].price))
            paid = True
            
        medias[mediaOption].rented = True
        rents.append(rent.Rent(costumers[costumerOption], medias[mediaOption], paid))
        
    """Def to add movie in the list medias"""                  
    def addMovies():
        with open('movies.txt', mode = 'r') as movies:
            file = movies.read()
            
            file = file.split('\n')
            
            for i in file:
                fileList = i.split(';')
                code = int(fileList[0])
                title = fileList[1]
                types = fileList[2]
                genre = fileList[3]
                price = float(fileList[4])
                classification = fileList[5]
                time = int(fileList[6])
                
                medias.append(media.Movie(code, title, types, genre, price, classification, time))
    
    """Def to add game in the list medias"""          
    def addGames():
        with open('games.txt', mode = 'r') as games:
            file = games.read()
            
            file = file.split('\n')
            
            for i in file:
                fileList = i.split(';')
                code = int(fileList[0])
                title = fileList[1]
                types = fileList[2]
                genre = fileList[3]
                price = float(fileList[4])
                videoGame = fileList[5]
                
                medias.append(media.Game(code, title, types, genre, price, videoGame))

    """Def to add book in the list medias"""      
    def addBooks():
        with open('books.txt', mode = 'r') as books:
            file = books.read()
            
            file = file.split('\n')
            
            for i in file:
                fileList = i.split(';')
                code = int(fileList[0])
                title = fileList[1]
                types = fileList[2]
                genre = fileList[3]
                price = float(fileList[4])
                author = fileList[5]
                publisher = fileList[6]
                edition = int(fileList[7])
                
                medias.append(media.Book(code, title, types, genre, price, author, publisher, edition))
    
    """Def to add costumer in the list costumers"""      
    def addCostumers():
        with open('costumers.txt', mode = 'r') as costumersList:
            file = costumersList.read()
            
            file = file.split('\n')
            
            for i in file:
                fileList = i.split(';')
                code = int(fileList[0])
                name = fileList[1]
                age = int(fileList[2])
                
                costumers.append(costumer.Costumer(code, name, age))
        
def main():    
    
    global medias
    global costumers
    global rents
    global option
    
    option = 0
    medias = []
    costumers = []
    rents = []
    option = 0

    rentalCompany.addMovies()
    rentalCompany.addBooks()
    rentalCompany.addGames()
    rentalCompany.addCostumers()

    while(option != 3):
        
        print("\n----Options----")
        print("1- Rent a media")
        print("2- Return a media")
        print("3- Exit")
        option = int(input("Select a option: "))

        if option == 1:
             rentalCompany.menuMedia()
             
        elif option == 2:
            
            if  (not rents):
                print("\nDoesn't exist rents")
            
            else:
                print("\nSelect a rent to return")
                selectRent = rentalCompany.selectRent()
                
                if (rents[selectRent].paid is not True):
                    print("You need to pay {0} dollars".format(rents[selectRent].media.price))
                    rents.pop(selectRent)
                    
                else:
                     rents.pop(selectRent)
                    
                print("thank you for the preference!")
            
        elif option == 3:
            break
            
        else:
            print("\nInvalid Option")
        
if __name__ == '__main__':
    main()
                      
                          






