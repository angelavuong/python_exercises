class musicalInstruments:
    numberOfMajorKeys = 12

class stringInstruments(musicalInstruments):
    typeOfWood = 'Tonewood'

class Guitar(stringInstruments):
    def __init__(self):
        self.numberOfStrings = 6
        print("This guitar consists of {} strings. It is made of {} and it can play {} keys.".format(self.numberOfStrings,self.typeOfWood,self.numberOfMajorKeys))

guitar = Guitar()
