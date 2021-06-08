"""robot_controller controller."""

import linha

from controller import Robot

vel_mult = 1.5
ir_thresh = 270.0
mult_curva = 2.0

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

    ir_r = robot.getDevice('IR_R')
    ir_r.enable(timestep)

# instanciar classes de controle
seguelinha = linha.Linha(ir_l, ir_r, ir_thresh, mult_curva)


def set_velocidade(velL, velR):
    motores[0].setVelocity(velL * vel_mult)
    motores[1].setVelocity(velR * vel_mult)
    motores[2].setVelocity(velL * vel_mult)
    motores[3].setVelocity(velR * vel_mult)


# loop principal
while robot.step(timestep) != -1:
    vel_l, vel_r = seguelinha.seguir_linha()
    #vel_l, vel_r = 5.0, -5.0
    print(vel_l, vel_r)
    set_velocidade(vel_l, vel_r)
