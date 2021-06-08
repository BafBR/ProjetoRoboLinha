class Linha:

    def __init__(self, ir_l, ir_r, ir_thresh, mult_curva) -> None:
        self.ir_l = ir_l
        self.ir_r = ir_r
        self.ir_thresh = ir_thresh
        self.mult_curva = mult_curva

    def seguir_linha(self):
        vel = 1.0, 1.0

        if self.get_linha_left() == self.get_linha_right():
            vel = 1.0, 1.0
        elif self.get_linha_left():
            vel = 0.0, 1.0
        elif self.get_linha_right():
            vel = 1.0, 0.0

        return vel

    def get_linha_left(self):
        val = self.__get_linha(self.ir_l)
        print('left ' + str(val))
        return val

    def get_linha_right(self):
        val = self.__get_linha(self.ir_r)
        print('right ' + str(val))
        return val

    def __get_linha(self, ir):
        val = ir.getValue()
        return val < self.ir_thresh
