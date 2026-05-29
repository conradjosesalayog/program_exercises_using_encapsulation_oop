from encapsulated_fan_class import Fan

def main():
    first_fan = Fan()

    #USE SETTERS
    first_fan.set_speed(Fan.FAST)
    first_fan.set_radius(10.0)
    first_fan.set_color("yellow")
    first_fan.set_on(True)

    #second_fan will be the default
    second_fan = Fan()

    print("FIRST FAN")
    print(first_fan.get_speed())