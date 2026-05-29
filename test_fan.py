from encapsulated_fan_class import Fan

reset = "\033[0m"
red = "\033[31m"
green = "\033[32m"
yellow = "\033[33m"
blue = "\033[34m"
cyan = "\033[36m"
bold = "\033[1m"

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
    print(first_fan.get_radius())
    print(first_fan.get_color())
    print(first_fan.get_on())

    print("---------------------------------------------")

    print("SECOND FAN")
    print(second_fan.get_speed())
    print(second_fan.get_radius())
    print(second_fan.get_color())
    print(second_fan.get_on())

if __name__ == "__main__":
    main()