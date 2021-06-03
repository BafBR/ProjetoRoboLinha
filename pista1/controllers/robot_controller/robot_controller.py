"""robot_controller controller."""

from controller import Robot

vel_mult = 3.0

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


def set_velocidade(velL, velR):
    motores[0].setVelocity(velL * vel_mult)
    motores[1].setVelocity(velR * vel_mult)
    motores[2].setVelocity(velL * vel_mult)
    motores[3].setVelocity(velR * vel_mult)


def teste():
    set_velocidade(1.0, 1.0)
    pass


# loop principal
while robot.step(timestep) != -1:
    teste()
