class Linha:

    def __init__(self, ir_l, ir_r, ir_l_ext, ir_r_ext, ir_thresh, mult_curva) -> None:
        self.ir_l = ir_l
        self.ir_r = ir_r
        self.ir_l_ext = ir_l_ext
        self.ir_r_ext = ir_r_ext
        self.ir_thresh = ir_thresh
        self.mult_curva = mult_curva

    def seguir_linha(self):
        vel = 1.0, 1.0
        if self.vejo_linha_left_ext() and not self.achouLinha():
            print('entrou')
            vel = 0.0, 1.0
        elif self.vejo_linha_right_ext() and not self.achouLinha():
            print('entrou2')
            while not self.achouLinha():
                vel = 1.0, 0.0
        elif self.vejo_linha_left() == self.vejo_linha_right():
            vel = 1.0, 1.0
        elif self.vejo_linha_left():
            vel = 0.0, 1.0 
        elif self.vejo_linha_right():
            vel = 1.0, 0.0

        return vel

    def vejo_linha_left(self):
        val = self.__vejo_linha(self.ir_l)
        #print('left ' + str(val))
        return val

    def vejo_linha_right(self):
        val = self.__vejo_linha(self.ir_r)
        #print('right ' + str(val))
        return val

    def vejo_linha_left_ext(self):
        val = self.__vejo_linha(self.ir_l)
        #print('left_ext ' + str(val))
        return val

    def vejo_linha_right_ext(self):
        val = self.__vejo_linha(self.ir_r)
        #print('right_ext ' + str(val))
        return val
    
    def __vejo_linha(self, ir):
        val = ir.getValue()
        return val < self.ir_thresh
    
    def achouLinha(self):
        val1 = self.vejo_linha_right()
        val2 = self.vejo_linha_left()
        print('val1: ' + str(val1) + ' val2: ' + str(val2))
        if val1:
            return val1
        elif val2:
            return val2
        return 0