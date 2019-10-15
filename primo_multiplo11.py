def primo_multiplo11():
    print"Dime un número"
    a=input ("A= ")
    for i in range (2,a):
        if (a%i==0):
            print "No es primo"
            break
        if(i==a-1):
            print "Es primo"
    if(a%11==0):
        print "Es multiplo de 11"
    else:
        print "No es multiplo de 11"
        
primo_multiplo11()
