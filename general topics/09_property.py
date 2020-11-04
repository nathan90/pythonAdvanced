class Celsius:
    def __init__(self, temperature=0):
        self.set_temperature(temperature)
    
    def to_farenheit(self):
        return (self.get_temperature() * 1.8) + 32
    #getter method
    def get_temperature(self):
        return self._temperature
    #setter method
    def set_temperature(self, value):
        if value < -273.5:
            raise ValueError('Temperature below -273.5 is not possible')
        self._temperature = value
    

# human = Celsius()
# human.temperature = 37
# print(human.temperature)
# print(human.to_farenheit())

# print(human.__dict__)

# create a new object
human = Celsius(37)
# get the temperature via getter 
print(human.get_temperature())
# get the farenheit method, get_temperature() called by the method itself
print(human.to_farenheit())

# new constraint implementation
human.set_temperature(-300)
print(human.searc)
