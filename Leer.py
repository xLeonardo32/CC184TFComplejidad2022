from platform import architecture
import re
from models.AgenciaViajes import AgenciaViajes

def leerArchivo(nombreArchivo):
    datos = []
    try:
        archivo = open(nombreArchivo)
        lineas = archivo.readlines()
        for linea in lineas:
            datos.append(linea.replace('\n',''))
    except FileNotFoundError:
        print("Archivo no encontrado")
    finally:
        archivo.close()
        return datos

def leerDataSet(nombreArchivo, inicio, fin=0):
    agenciaViajes = []
    try:
        archivo = open(nombreArchivo)
        lineas = archivo.readlines()
        if fin !=0:
            lineas = lineas[inicio:(fin+1)]
        else:
            lineas = lineas[inicio:]

        registros = []
        i = 0
        for linea in lineas:
            aux = linea.replace('\n','')
            if len(aux.split(',')) == 10:
                registros.append(aux)
        print(len(registros))
        for registro in registros:
            datos = registro.split(',')
            travelCode, userCode = datos[0:2]
            fromOrigen, toDestino, flightType = datos[2:5]
            price, time, distance = datos[5:8]
            price= float(price)
            time = float(time)
            distance = float(distance)
            agency, date = datos[8:10]
            agenciaViajes.append(AgenciaViajes(travelCode, userCode, fromOrigen, toDestino, flightType, price, time, distance, agency, date))
    except FileNotFoundError:
        print("Archivo no encontrado.")
    finally:
        archivo.close()
        return agenciaViajes

if __name__== "__main__":
    agenciaViajes = leerDataSet("flights.csv", 1)
    i = 0
    for vuelos in agenciaViajes:
        if vuelos.fromOrigen == 1:
            print(vuelos)
            i+=1
    print("Total de vuelos: " + str(i))
        
