def inventado():
    print"que numero te interesa multiplicar"
    a=input("A= ")

    if(a>20):
        print "Esto es muy largo y me da pereza"
    else:
        for i in range (0,a+1):
            print a*i
    while(a<1):
        a=input("A= ")
        if (a>=1):
            print "se puede yupiii"
            for i in range (0,a+1):
                print a*i

inventado()
