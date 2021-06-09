"""robot_controller controller."""

import linha
import camera

from controller import Robot

vel_mult = 3.0
ir_thresh = 615.0
mult_curva = 2.0

procurando_linha = 0

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

# obter camera
camera_device = robot.getDevice("camera")
camera_device.enable(timestep)

camera_obj = camera.Camera(camera_device)

# instanciar classes de controle
seguelinha = linha.Linha(ir_l, ir_r, ir_l_ext, ir_r_ext, ir_thresh, mult_curva)


def set_velocidade(velL, velR):
    #print(velL, velR)
    motores[0].setVelocity(velL * vel_mult)
    motores[1].setVelocity(velR * vel_mult)
    motores[2].setVelocity(velL * vel_mult)
    motores[3].setVelocity(velR * vel_mult)


# loop principal
while robot.step(timestep) != -1:
    if procurando_linha > 0:  # procurando na esquerda
        if seguelinha.vejo_linha_right():
            procurando_linha = 0
    elif procurando_linha < 0:  # procurando na direita
        if seguelinha.vejo_linha_left():
            procurando_linha = 0
    else:
        vel_l, vel_r, dir_procura = seguelinha.seguir_linha()
        procurando_linha = dir_procura
        set_velocidade(vel_l, vel_r)
