class AgenciaViajes:
    def __init__(self, travelCode, userCode, fromOrigen, toDestino, flightType, price, time, distance, agency, date):
        self.travelCode = travelCode
        self.userCode = userCode
        self.fromOrigen = fromOrigen
        self.toDestino =toDestino
        self.flightType = flightType
        self.price = price
        self.time = time
        self.distance = distance
        self.agency = agency
        self.date = date
    def __str__(self):
        return "%s D; %s P: "