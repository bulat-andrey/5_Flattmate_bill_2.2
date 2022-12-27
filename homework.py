class Water:
    boiling_temperature = 100
    freezing_temperature = 0

    def __init__(self, temperature):
        self.temperature = temperature

    def state(self):
        if self.temperature <= self.freezing_temperature:
            return 'solid'
        elif self.temperature < self.boiling_temperature:
            return 'liquid'
        else:
            return 'gas'

water = Water(temperature=20)
water.boiling_temperature = 212
water.freezing_temperature = 32
print(water.state())