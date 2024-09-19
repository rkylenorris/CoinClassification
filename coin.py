

class Coin:

    def __init__(self, center, radius, brightness):
        self.center = center
        self.radius = radius
        self.brightness = brightness
        self.color = self.get_color()
        self.value = self.get_value()

    def get_color(self):
        if self.brightness > 170:
            return 'SILVER'
        else:
            return 'COPPER'

    def get_value(self):
        if self.color == 'SILVER':
            if self.radius < 100:
                return 5
            else:
                return 10
        elif self.color == 'COPPER':
            if self.radius < 110:
                return 1
            else:
                return 2