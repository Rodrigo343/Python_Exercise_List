from product import Product
from exception import ExceptionTest

class Cart:
    
    """def to verify and validate input """
    def testExceptionInt(message):
        exceptionConfirm = True
                
        while (exceptionConfirm):
            test = input(message)
            
            if(ExceptionTest.exceptionInt(test)): 
                test = int(test)
                exceptionConfirm = False 
                return test         
            
def main():
    option = 0
    answer = 'yes'
    
    products = Product()

    while (answer.lower() == 'yes'):
        
        print ('\n-- Products Options ---')
        print ('1- Candy - R$30,00')
        print ('2- Meat - R$10,00')
        print ('3- Bread - R$5,00')
        print ('4- Vegetable - R$25,00')
        
        option = Cart.testExceptionInt('Select a prduct: ')
            
        if(option >= 1 and option <= 4):
            products.quantity = Cart.testExceptionInt('Desired quantity: ')
            if products.isFull():
                print ('Full cart!')
                
            else:
                products.addItem(option)
       
            answer = input('Do you want something else? (yes/no)\n')
        
        else:             
            print('Invalid Option')

    print ('\nTotal: ${0}'.format(products.total()))
    
if __name__ == '__main__':
    main()