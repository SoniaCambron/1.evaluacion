def ejercicio5():
    
    print"Dime un día"

    while(a<1 or a>31):
        a=input("A= ")
        if(a<1 or a>31):
            print "ERROR en el dia"
    
    print"Dime un numero de mes"
    
    while(b<1 or b>12):
        b=input("B= ")
        if(b<1 or b>12):
            print "ERROR en el mes"
            
    if(b==1):
        b="Enero"
    if(b==2):
        b="Febrero"
    if(b==3):
        b="Marzo"
    if(b==4):
        b="Abril"
    if(b==5):
        b="Mayo"
    if(b==6):
        b="Junio"
    if(b==7):
        b="Julio"
    if(b==8):
        b="Agosto"
    if(b==9):
        b="Septiembre"
    if(b==10):
        b="Octubre"
    if(b==11):
        b="Noviembre"
    if(b==12):
        b="Diciembre"
        
    print"Dime un año"
    c=input("C= ")
    print a, "de", b, "de", c

ejercicio5()
