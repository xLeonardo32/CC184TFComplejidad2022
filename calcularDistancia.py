import math

def calcularDistancia(fromOrigen, toDestino):
    resX = toDestino.coordX - fromOrigen.coordX
    resY = toDestino.coordY - fromOrigen.coordY
    resX2 = resX ** 2
    resY2 = resY ** 2
    dist = math.sqrt(resX2 + resY2)
    return dist