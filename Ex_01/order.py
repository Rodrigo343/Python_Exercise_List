import product

class Order():
    
    """Constructor. Create the Order"""
    def __init__(self):
        self.__order = []    
            
    """Add a prodoct in order"""    
    def updeteOrder(self, producty):      
        self.__order.append(producty)


    """Verification if the order is full"""
    def isFull(self):
        
        return (True if (len(self.__order) >= 99) else False)
        
    """Total price of order"""
    def total(self): 

        candy = 0
        meat = 0
        bread = 0
        vegetable = 0
        counter = 0
        
        for i in range( len(self.__order) ):
            
            if isinstance(self.__order[counter], product.Candy):
                candy += 1

                
            elif isinstance(self.__order[counter], product.Meat):
                meat += 1

            elif isinstance(self.__order[counter], product.Bread):
                bread += 1

            else:
                vegetable += 1
                
            counter += 1

        return str( ((candy*30) + (meat*10) + (bread*5) + (vegetable*25)) )
 