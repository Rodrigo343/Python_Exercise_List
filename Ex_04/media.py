class Media():
    
    def __init__(self, code, title, types, genre, price):
         self.code = code
         self.title = title
         self.types = types
         self.genre = genre
         self.price = price
         self.rented = False
  
    @property
    def code(self):
        return self.__code

    @code.setter  
    def code(self, code):
        self.__code = code
        
    @property
    def title(self):
        return self.__title    
        
    @title.setter  
    def title(self, title):
        self.__title = title
        
    @property
    def types(self):
        return self.__types
    
    @types.setter  
    def types(self, types):
        self.__types = types
    
    @property
    def genre(self):
        return self.__genre
    
    @genre.setter  
    def genre(self, genre):
        self.__genre = genre
    
    @property
    def price(self):
        return self.__price    
    
    @price.setter  
    def price(self, price):
        self.__price = price
    
    @property
    def rented(self):
        return self.__rented   
    
    @rented.setter  
    def rented(self, rented):
        self.__rented = rented

    def __str__(self):        
        return "Code: {0}\nTitle: {1}\nType: {2}\nGenre: {3}\nPrice: {4}\nRented: {5}".format(
            self.code, self.title, self.types, self.genre, self.price, self.rented)

"""Book Media"""
class Book(Media):
    
    def __init__(self,  code, title, types, genre, price, author, publisher, edition):
        super().__init__(code, title, types, genre, price)
        self.author = author
        self.publisher = publisher
        self.edition = edition

    @property  
    def author(self):
        return self.__author
    
    @author.setter  
    def author(self, author):
        self.__author = author
        
    @property  
    def publisher(self):
        return self.__publisher
    
    @publisher.setter  
    def publisher(self, publisher):
        self.__publisher = publisher
        
    @property  
    def edition(self):
        return self.__edition
    
    @edition.setter  
    def edition(self, edition):
        self.__edition = edition
        
    def __str__(self):
        return super().__str__() + "\nAuthor: {0}\nPublisher: {1}\nEdition: {2}".format(
            self.author, self.publisher, self.edition)     
     
"""Game Midia"""
class Game(Media):
    
    def __init__(self,  code, title, types, genre, price, videoGame):
        super().__init__(code, title, types, genre, price)
        self.videoGame = videoGame

    @property  
    def videoGame(self):
        return self.__videoGame
    
    @videoGame.setter  
    def videoGame(self, videoGame):
        self.__videoGame = videoGame
        
    def __str__(self):
        return super().__str__() + "\nVideo Game: {0}".format(self.videoGame)  

"""Movie Midia"""
class Movie(Media):
    
    def __init__(self,  code, title, types, genre, price, classification, time):
        super().__init__(code, title, types, genre, price)
        self.classification = classification
        self.time = time

    @property  
    def classification(self):
        return self.__classification
    
    @classification.setter  
    def classification(self, classification):
        self.__classification = classification
        
    @property  
    def time(self):
        return self.__time
    
    @time.setter  
    def time(self, time):
        self.__time = time
        
    def __str__(self):
        return super().__str__() + "\nClassification: {0}\nTime: {1}".format(self.classification, self.time)  
   

