import numpy as np
import json
    #Valores que ingresara el usuario
def simplex(numVar:int, numDes:int,tipoOpt:str,coeficientesFO:str,coeficientesDes:str,valoresIndependientes:str):
    #numVar =2
    #numDes = 4
    #tipoOpt = "Max"
    #coeficientesFO = "5 4"
    #coeficientesDes = " 6 4 1 2 -1 1 0 1"
    #valoresIndependientes = "24 6 1 2"
    #Convertir a matriz
    numeroscoeficientesFO  = list(map(float, coeficientesFO.split()))
    matrizcoeficientesFO = np.array(numeroscoeficientesFO).reshape(1, numVar)
    numeroscoeficientesDes = list(map(float, coeficientesDes.split()))
    matrizcoeficientesDes = np.array(numeroscoeficientesDes).reshape(numDes, numVar)
    numerosvaloresIndependientes = list(map(float, valoresIndependientes.split()))
    matrizvaloresIndependientes= np.array(numerosvaloresIndependientes).reshape(1, numDes)
    Tabla = np.zeros((1+numDes,1+numVar+numDes+1))
    Tabla[0][0] =1 
    #Guardando coeficientesFO 
    for i in range(numVar):
        Tabla[0][i+1] = -matrizcoeficientesFO[0][i] 
    #Guardando coeficientes des
    for i in range(numDes):
        for j in range(numVar):
            Tabla[1+i][1+j] =  matrizcoeficientesDes[i][j]
    #Guardando Valores Independientes
    for i in range(numDes):
        Tabla[1+i][(1+1+numVar+numDes)-1] =  matrizvaloresIndependientes[0][i]
    #Cr eando la matriz identidad
    for i in range(numDes):
        Tabla[i+1][i+1+numVar]= 1

    TablaVariablesDentro= np.zeros((1,numDes))
    for i in range(numDes):
        TablaVariablesDentro[0][i] = numVar +(i+1)
    TablaVariablesFuera= np.zeros((1,numVar))
    for i in range(numVar):
        TablaVariablesFuera[0][i] = i+1
    aux =0

    #ALGORITMO
    seguir =True
    while seguir: 
        seguir =False
        min = 9999999999999
        for i in range(numVar +numDes):
            if Tabla[0][i+1] <=min:
                min= Tabla[0][i+1]
                posicionEntra= i+1
        min = 9999999999999
        for i in range(numDes): 
            if Tabla[i+1][posicionEntra]!=0:
                if Tabla[i+1][(1+1+numVar+numDes)-1]/Tabla[i+1][posicionEntra]<=min and Tabla[i+1][(1+1+numVar+numDes)-1]/Tabla[i+1][posicionEntra]>=0:
                    min = Tabla[i+1][(1+1+numVar+numDes)-1]/Tabla[i+1][posicionEntra]
                    posicionSale = i+1
        valorPivote=Tabla[posicionSale][posicionEntra] 
        filaPivote= Tabla[posicionSale]/valorPivote
        Tabla[posicionSale] = Tabla[posicionSale]/valorPivote
        for i in range(numDes+1):
            if i != posicionSale: 
                Tabla[i] = Tabla[i] - Tabla[i][posicionEntra]*filaPivote 
        aux = TablaVariablesDentro[0][posicionSale-1]
        TablaVariablesDentro[0][posicionSale-1]=TablaVariablesFuera[0][posicionEntra-1]
        TablaVariablesFuera[0][posicionEntra-1] = aux
        #Verificando que ya no se puede optimizar mas 
        for i in range(1+numVar+numDes+1):
            if Tabla[0][i]<0:
                seguir=True
                break

    #IMPRIMIR LOS VALORES QUE DAN LA SOLUCION 
    solucion= np.zeros((1,numVar))
    cont =0
    for i in range(numVar):
        for j in range(numDes):
            if TablaVariablesDentro[0][j] ==i+1:
                solucion[0][cont]= Tabla[j+1][(1+1+numVar+numDes)-1]
        cont+=1

    solucionDic = []

    # Convertir la matriz en JSON (agregar diccionarios a la lista)
    for i in range(numVar):
        # Crear un diccionario y agregarlo a la lista
        solucionDic.append({"variable": "x" + str(i+1), "valor": solucion[0][i]})
    solucionDic.append({"variable":"z","valor":Tabla[0][1+numVar+numDes+1-1]})

        #json_data = json.dumps(solucionDic, sort_keys=True, indent=4)
    return solucionDic
