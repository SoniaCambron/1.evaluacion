def n_primo():
    print"Dime un número"
    a=input ("A= ")
    for i in range (2,a):
        if (a%i==0):
            print "No es primo"
            break
    if(i==a-1):
        print "Es primo"
n_primo()
