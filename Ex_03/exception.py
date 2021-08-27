class NotPositiveException(Exception):
    pass

class ExceptionTest():
    
    def exceptionInt(test):
        try:
            intValue = int(test)
            if( intValue < 0 ): raise NotPositiveException
            return True
        
        except ValueError:
           print("Ops!! You typed a invalid value!! Try Again")
           return False
                   
        except NotPositiveException: 
            print("The number was not positive, please try again.") 
            return False
        
    def exceptionFloat(test):
        try:
            floatValue = float(test)
            if( floatValue < 0 ): raise NotPositiveException
            return True
        
        except ValueError:
           print("Ops!! You typed a invalid value!! Try Again")
           return False
                   
        except NotPositiveException: 
            print("The number was not positive, please try again.") 
            return False