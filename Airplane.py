class Airplane:
    def __init__(self, serial, model, name, pilot):
        self.serial = serial
        self.model = model
        self.name = name
        self.pilot = pilot

    def getAirplaneInfo(self):
        return print (f'''
        Nombre: {self.name}
        Serial: {self.serial}
        Model: {self.model}
        Pilot: {self.pilot}
        ''')