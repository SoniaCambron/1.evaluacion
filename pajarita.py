def pajarita():
    filas=input("Dime cuanta altura y ancho quieres: ")
    espacios=" "
    asterisco="*"
    for i in range (0,filas/2):
        for nespacios in range (i,0):
            espacios=espacios+" "+" "
        for nasteriscos in range(0,i):
            asterisco=asterisco+"*"
        
        if(filas==filas/2):
            asterisco=filas
        print asterisco+espacios+asterisco
        espacios=" "
        asterisco="*"
pajarita()
    
