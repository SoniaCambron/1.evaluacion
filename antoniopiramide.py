def piramide2():
    filas=input("Dime la altura de la piramide: ")
    espacios=' '
    asteriscos='*'
    for i in range(filas):
    #Constuimos la secuencia de espacios
        for nespacios in range(1,filas-i-1): #hacemos muchas cuentas para unirlo
        #Cuando i=1 y tenemos 4 filas nespacios ira de 1 a 2 y se suman espacios
        #dependiendo de ese numero, por lo tanto aqui habra 2 espacios (uno del 1
        #y despues se suma otro por el dos.
            espacios=espacios+' '
        for nasteriscos in range(1,2*i): #cuando tenemos i=1 nos va a dar 2, pero ese
        #numero no lo cnatara asi que la relacion es una mas.
            asteriscos=asteriscos+'*'
        #escribo de golpe toda la fila
        print  espacios + asteriscos
        espacios=' '
        asteriscos='*'
        #paso a la siguiente fila.
#se vaya sumando un espacio mas i=1 nespacios=3

piramide2()
        
