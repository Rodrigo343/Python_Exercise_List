class Rent():
    
    def __init__(self, costumer, media, paid):
         self.costumer = costumer
         self.media = media
         self.paid = paid
        
    @property
    def costumer(self):
        return self.__costumer

    @costumer.setter  
    def costumer(self, costumer):
        self.__costumer = costumer
        
    @property
    def media(self):
        return self.__media  
        
    @media.setter  
    def media(self, media):
        self.__media = media
        
    @property
    def paid(self):
        return self.__paid
    
    @paid.setter  
    def paid(self, paid):
        self.__paid = paid

    def __str__(self):        
        return "Costumer: {0}, {1}\nMedia: {2}, {3}\nPaid: it's {4}paid".format(self.costumer.code, self.costumer.name, self.media.code, self.media.title,("" if self.paid else "not "))