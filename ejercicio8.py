def ejercicio8():
    print"De que cifra quieres sacar el IVA?"
    a=input("A= ")
    print "Que tipo de IVA vamos a aplicarle?"
    b=input("= ")

    if (b=="general"):
        b=16
            
    if (b=="reducido"):
        b=7
    if (b=="superreducido"):
        b=4
    precio=a+a*(b/100)
    print precio, "euros"
ejercicio8()
