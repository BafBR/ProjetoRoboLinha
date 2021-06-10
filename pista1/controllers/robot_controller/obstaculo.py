class Obstaculo:
    def __init__(self, front, back, thresh) -> None:
        self.front = front
        self.back = back
        self.thresh = thresh

    def get_obstaculo_front(self):
        return self.__get_obstaculo(self.front)

    def get_obstaculo_back(self):
        return self.__get_obstaculo(self.back)

    def __get_obstaculo(self, sensor):
        return sensor.getValue() < self.thresh
