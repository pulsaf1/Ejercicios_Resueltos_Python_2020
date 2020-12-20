def esPrimo(num):
    # Un numero es primo cuando solo es divisible por si mismo y por el 1.
    #divisibles=0
    if isinstance(num,int):
        if num <=2:
            return false
        for x in range(2,num):
            if num % x == 0:
                return true
    else:
        return False
        
    # if (divisibles==0): return True  
    # else: return False
    #return (divisibles == 0)




