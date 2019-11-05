def ejercicio8():
    print"De que cifra quieres sacar el IVA?"
    a=input("A= ")
    print "Que tipo de IVA vamos a aplicarle?"
    b=raw_input("= ")

    if (b=="general"):
        b=16
    if (b=="reducido"):
        b=7
    if (b=="superreducido"):
        b=4
    precio=a+a*(0.01*b)
    print precio, "euros"
ejercicio8()
