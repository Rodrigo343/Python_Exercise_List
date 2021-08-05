from product import Product

class Cart:
        
    def main():
        option = 0
        answer = 'yes'
        
        products = Product()

        while answer.lower() == 'yes':

            print ('\n-- Products Options ---')
            print ('1- Candy - R$30,00')
            print ('2- Meat - R$10,00')
            print ('3- Bread - R$5,00')
            print ('4- Vegetable - R$25,00')
            option = int(input('Select a prduct: '))
            
            products.quantity = int(input('Desired quantity: '))

            if products.isFull():
                print ('Full cart!')
                
            else:
                products.addItem(option)

            
            answer = input('Do you want something else? (yes/no)\n')

        print ('\nTotal: $' + products.total())
        
    if __name__ == '__main__':
        main()