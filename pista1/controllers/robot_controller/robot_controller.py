"""robot_controller controller."""

import linha
import camera
import obstaculo

from controller import Robot

vel_mult = 3.0
ir_thresh = 615
obj_thresh = 1000
mult_curva = 2.0

procurando_linha = 0

backstep_max = 20
backstep_count = backstep_max

curva_max = 30
curva_count = curva_max

desviando = 0
inicio_desvio = False
inicio_retorno = False

# instanciar robô e obter timestep
robot = Robot()
timestep = int(robot.getBasicTimeStep())

# obter e inicializar motores
motores = []
motor_nomes = ['MotorFL', 'MotorFR', 'MotorBL', 'MotorBR']
for nome in motor_nomes:
    device = robot.getDevice(nome)
    device.setPosition(float('inf'))
    device.setVelocity(0.0)
    motores.append(device)

# obter e inicializar sensores IR de linha
ir_l = robot.getDevice('IR_L')
ir_l.enable(timestep)

ir_l_ext = robot.getDevice('IR_L_ext')
ir_l_ext.enable(timestep)

ir_r = robot.getDevice('IR_R')
ir_r.enable(timestep)

ir_r_ext = robot.getDevice('IR_R_ext')
ir_r_ext.enable(timestep)

# obter e inicializar sensores de obstáculo
obj_front = robot.getDevice('OBJ_F')
obj_front.enable(timestep)

obj_b = robot.getDevice('OBJ_B')
obj_b.enable(timestep)

desviar = obstaculo.Obstaculo(obj_front, obj_b, obj_thresh)

# obter e inicializar camera
camera_device = robot.getDevice("camera")
camera_device.enable(timestep)

camera_obj = camera.Camera(camera_device)

# instanciar classes de controle
seguelinha = linha.Linha(ir_l, ir_r, ir_l_ext, ir_r_ext, ir_thresh, mult_curva)


def set_velocidade(velL, velR):
    # print(velL, velR)
    motores[0].setVelocity(velL * vel_mult)
    motores[1].setVelocity(velR * vel_mult)
    motores[2].setVelocity(velL * vel_mult)
    motores[3].setVelocity(velR * vel_mult)


# loop principal
while robot.step(timestep) != -1:
    if desviando != 0:
        if inicio_retorno:
            print('retornando')
            set_velocidade(1, 0.2)
            if seguelinha.vejo_linha_left():
                desviando = 0
                inicio_desvio = False
                inicio_retorno = False
                backstep_count = backstep_max
                curva_count = curva_max
                procurando_linha = 0
                print('na linha')
        elif not inicio_desvio:
            if backstep_count == 0:
                print('desviando')
                set_velocidade(0, 1)
                inicio_desvio = curva_count == 0
                curva_count -= 1
            else:
                set_velocidade(-1, -1)
                backstep_count -= 1
        else:
            print('ultrapassando')
            set_velocidade(1, 1)
            inicio_retorno = desviar.get_obstaculo_back()
            #inicio_retorno = desviar.get_obstaculo_right()
    elif procurando_linha > 0:  # procurando na esquerda
        if seguelinha.vejo_linha_right_ext():
            procurando_linha = 0
    elif procurando_linha < 0:  # procurando na direita
        if seguelinha.vejo_linha_left_ext():
            procurando_linha = 0
    else:
        vel_l, vel_r, dir_procura = seguelinha.seguir_linha()
        procurando_linha = dir_procura
        if desviar.get_obstaculo_front():
            print('obstaculo!')
            desviando = 1
        set_velocidade(vel_l, vel_r)
