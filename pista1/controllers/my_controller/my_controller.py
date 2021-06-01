"""my_controller controller."""

from controller import Robot

robot = Robot()

timestep = int(robot.getBasicTimeStep())

rodas = []
rodas_nomes = ['RodaFL']#, 'RodaFR', 'RodaBL', 'RodaBR']
for nome in rodas_nomes:
    print(nome)
    device = robot.getDevice(nome)
    device.setPosition(float('inf'))
    device.setVelocity(0.0)
    rodas.append(device)

while robot.step(timestep) != -1:
    velEsq = 1.0
    velDir = 1.0
    
    rodas[0].setVelocity(velEsq)
    #rodas[1].setVelocity(velEsq)
    #rodas[2].setVelocity(velDir)
    #rodas[3].setVelocity(velEsq)
