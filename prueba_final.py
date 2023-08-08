import datetime
from random import randint

recaudacion = 0.0

def comprobante(dni, cifra, monto):
    global tiquet
    tiquet = 0
    print("*******************")
    print("*QUINIELA APROBABA*")
    print("*******************")
    print("-------------------")
    print("Fecha: ", datetime.datetime.now())
    tiquet+=1
    print(f"Número de comprobante: 000 - 0000{tiquet}")
    print("D.N.I: ", dni)
    print("Cifra apostada: ", cifra)
    print("Monto apostado: ", monto)

def monto_apostado():
    global recaudacion
    montoA = float(input("Ingrese el monto de la apuesta: "))
    recaudacion += montoA
    return montoA

def quiniela(dni):
    global cifra, cf
    
    cifra = int(input("Ingrese la cifra a apostar: "))

    while True:
        if cifra >= 00 and cifra<= 99:
            cf = 2
            monto = monto_apostado()
            break
        elif cifra >=100 and cifra <= 999:
            cf= 3
            monto = monto_apostado()
            break
        elif cifra >= 1000 and cifra <= 9999:
            cf = 4
            monto = monto_apostado()
            break
        else:
            print("ERROR, la cifra del número debe ser de 2, 3 o 4")
    comp = comprobante(dni, cifra, monto)

def quini6(dni):
    global numQ
    numQ=[]

    dec = int(input("Ingrese 1 para ingresar los numeros o 2 al azar: "))
    if dec == 1:
        for i in range(6):
            while True:
                print(f"Ingrese el número {i+1} (enre 00 y45 inclusive):")
                num = int(input())
                if num > 00 and num < 46:
                    numQ.append(num)
                    break
                else:
                    print("ERROR el numero debe estar entre 00 y 46, ingrese otra vez un  numero.")  
                      
        monto = monto_apostado()
    elif dec == 2:
        for i in range(6):
            num = randint(00, 46)
            numQ.append(num)
        monto = monto_apostado()
    else:
        print("La opción ingresada es incorrecta")
    comprobante(dni, numQ, monto)

def arqueo():
    estado = recaudacion * 0.47
    ganancia = recaudacion - estado
    print("****************")
    print("*ARQUEO DE CAJA*")
    print("****************")
    print(f"La retención del Estado es $: {estado}")
    print(f"La ganancia para el comercio es $: {ganancia}")

def comprobar_apuesta():
    apuestaQ=[]
    dec = {"1": "Comprobar Quiniela",
           "2": "Comprobar Quini 6"}
    for opcion, decision in dec.items():
        print(f'{opcion} - {decision}')
    opcion = int(input("Ingrese la opción deseada: "))
    if opcion==1:
        if cf == 2:
            apuesta = randint(00,99)
            if apuesta == cifra:
                print("HA GANADO!!")
            else:
                print("La apuesta no ha sido ganadora")
        elif cf == 3:
            apuesta = randint(100,999)
            if apuesta == cifra:
                print("HA GANADO!!")
            else:
                print("La apuesta no ha sido ganadora")
        else:
            apuesta = randint(1000,9999)
            if apuesta == cifra:
                print("HA GANADO!!")
            else:
                print("La apuesta no ha sido ganadora")
    if opcion==2:
        apuestaQ=[]
        for i in range(6):
            num = randint(00, 46)
            apuestaQ.append(num)
            aciertos=0
        for i in range(6):
            if numQ[i]==apuestaQ[i]:
                aciertos=aciertos+1
        if aciertos==6:
            print("HA GANADO!!")
        else:
                print("La apuesta no ha sido ganadora")
            
def Menu():
    print("................................")
    print("Bienvenido a Quiniela 'aprobado'")
    print("................................")

    menu={"1":"Quiniela",
        "2":"Quini 6",
        "3":"Comprobar mi apuesta",
        "4":"Arquero de caja",
        "5":"Salir"}
    
    print("Escoja una de las siguientes opciones")
    for opcion, descripcion in menu.items():
        print(f'*{opcion} - {descripcion}', end="\n") 
             

while True:
    DNI = input("Ingrese el DNI del apostador: ")
    paso1= Menu()
    print(paso1)
    opcion = int(input("Número de opción: "))
    if opcion==1:
        paso2 = quiniela(DNI)
    elif opcion==2:
        paso3 = quini6(DNI)
    elif opcion==3:
        paso4 = comprobar_apuesta()
    elif opcion==4:
        paso5 = arqueo()
    elif opcion==5:
        print("Hasta luego!")
        break
    else:
        print("La opciòn ingresada es incorrecta")