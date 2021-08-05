from order import Order

class Product(Order):
    
    """Constructor"""
    def __init__(self):
        super().__init__()
        self.__quantity = 0
        self.__limit = 0
    
    @property  
    def quantity(self):
        return self.__quantity
    
    @quantity.setter  
    def quantity(self, quantity):
        self.__quantity = quantity
    
    "Add item in the order"
    def addItem(self, option):
        for i in range(self.__quantity):
            
            if self.__limit == 100: break
        
            if (option < 1 or option > 4):
                print("Invalid Option")    
                
            elif option == 1:
                Order.updeteOrder(self, Candy())
            
            elif option == 2:
                Order.updeteOrder(self, Meat())
                
            elif option == 3:
                Order.updeteOrder(self, Bread())
                
            elif option == 4:
                Order.updeteOrder(self, Vegetable())
          
            self.__limit += 1
        
            
class Candy(Product):
    
    def __init__(self):
        super().__init__()
        
class Bread(Product):

    def __init__(self):
        super().__init__()
        
class Meat(Product):
    
    def __init__(self):
        super().__init__()
        
class Vegetable(Product):
    
    def __init__(self):
        super().__init__()
        
        