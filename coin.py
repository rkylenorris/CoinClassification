

class Coin:
    """
    Class representing a british circular coin
    """
    def __init__(self, center, radius, brightness):
        """
        initializer
        :param center: coordinate value of the coins center in picture
        :param radius: radius of the coin
        :param brightness: apparent brightness in img found using a subsection of img values
        """
        # set coin properties
        self.center = center
        self.radius = radius
        self.brightness = brightness
        self.color: str = self.get_color()
        self.value: int = self.get_value()

    def get_color(self) -> str:
        """
        determine if coin is silver or copper
        :return: str
        """
        if self.brightness > 170:
            return 'SILVER'
        else:
            return 'COPPER'

    def get_value(self) -> int:
        """
        determines value based on color and radius
        :return: int
        """
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
        else:
            return 0
