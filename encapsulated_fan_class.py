class Fan:
#CONSTANTS
    SLOW = 1
    MEDIUM = 2
    FAST = 3

#CONSTRUCTOR
    def __init__(self, speed=SLOW, radius=5.0, color="blue", on=False):
    #PRIVATE DATA FIELD
        self.__speed = speed
        self.__radius = radius
        self.__color = color
        self.__on = on

    #GETTERS
    def get_speed(self):
        return self.__speed