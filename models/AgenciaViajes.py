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
        "%s Type of Flight: %s Price: %f time: %f distance: %s date: %d travelCode: %d userCode: %s from: %s to: %f"  % (self.agency, self.flightType, self.price, self.time, self.distance, self.date, self.travelCode, self.userCode, self.fromOrigen, self.toDestino)
