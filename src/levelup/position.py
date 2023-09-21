class Position:

    coordinates = list((-1,-1))

    def __init__(self):
        # do nothing
        self.coordinates = (-1, -1)

    def __init__(self, xCoordinate,yCoordinate):
        self.coordinates = (xCoordinate,yCoordinate)