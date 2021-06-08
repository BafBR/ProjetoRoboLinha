class Linha:

    def __init__(self, ir_l, ir_r, ir_thresh, mult_curva, buffer_size) -> None:
        self.ir_l = ir_l
        self.ir_r = ir_r
        self.ir_thresh = ir_thresh
        self.mult_curva = mult_curva
        self.buffer_size = buffer_size

        self.buffer = 1.0, 1.0
        self.buffer_count = self.buffer_size

    def seguir_linha(self):
        if self.buffer_count > 0:
            self.buffer_count -= 1
        else:
            self.buffer_count = self.buffer_size
            if self.get_linha_left():
                self.buffer = -1 * self.mult_curva, 1.0
            elif self.get_linha_right():
                self.buffer = 1.0, -1 * self.mult_curva
            else:
                self.buffer = 1.0, 1.0

        return self.buffer

    def get_linha_left(self):
        return self.__get_linha(self.ir_l)

    def get_linha_right(self):
        return self.__get_linha(self.ir_r)

    def __get_linha(self, ir):
        val = ir.getValue()
        return val < self.ir_thresh
