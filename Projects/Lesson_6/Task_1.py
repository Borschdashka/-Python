import time


class TrafficLight:
    def __init__(self):
        self.__color = ""

    def run(self):
        while True:
            self.__color = "красный"
            print(self.__color)
            time.sleep(7)

            self.__color = "желтый"
            print(self.__color)
            time.sleep(2)

            self.__color = "зелёный"
            print(self.__color)
            time.sleep(5)


traffic_light = TrafficLight()
traffic_light.run()
