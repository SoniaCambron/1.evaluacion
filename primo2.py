def primo():
    print"En que numero quieres empezar?"
    a=input ("= ")
    print"En que numero quieres acabar?"
    b=input ("= ")
    divisor=False
    salir=False
    for i in range (a,b):
        for cont in range (2,i):
            if(i%cont==0):
                divisor=True
                salir=True
            if(salir==True):
                cont=1
        if(divisor==True):
            print i, "No es primo"
        else:
            print i, "Es primo"
        divisor=False
            
            


        
primo()
