def ejercicio9():
    print"Cuantas horas has trabajado este mes?"
    a=input("= ")
    while (a>0):
        for i in range (1,41):
            suma1=i*30
        for c in range (41,a):
            suma2=(c-40)*45
        print suma1+suma2
ejercicio9()
