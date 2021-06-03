"""robot_controller controller."""

from controller import Robot

robot = Robot()

timestep = int(robot.getBasicTimeStep())

vel_mult = 3.0

motores = []
motor_nomes = ['MotorFL', 'MotorFR', 'MotorBL', 'MotorBR']

for nome in motor_nomes:
    device = robot.getDevice(nome)
    device.setPosition(float('inf'))
    device.setVelocity(0.0)
    motores.append(device)

while robot.step(timestep) != -1:
    velL = 1.0
    velR = 1.0

    motores[0].setVelocity(velL * vel_mult)
    motores[1].setVelocity(velR * vel_mult)
    motores[2].setVelocity(velL * vel_mult)
    motores[3].setVelocity(velR * vel_mult)
