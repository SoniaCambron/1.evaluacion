def par_impar ():
    a=input("Hasta que numero cuento: ")
    for i in range (1, a):
        if(i%2==0):
            print i, "=par"

        else:
            print i, "=impar"
    
par_impar()
