def ejercicio6():
    print "Dime un numero"
    a=input("A= ")
    print "Dime otro numero"
    b=input("B= ")
    
    print "Que operacion quieres realizar?"
    print "Pon S para suma, R para Resta, M para multiplicación y D para división."
    c=raw_input(": ")
    if (c=="S"):
        print a+b
    if(c=="R"):
        print a-b
    if(c=="M"):
        print a*b
    if(c=="D"):
        print a/b

ejercicio6()
