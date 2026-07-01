from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, UltrasonicSensor, ColorSensor 
from pybricks.parameters import Color, Port
from pybricks.tools import wait, StopWatch

hub = PrimeHub(broadcast_channel=2, observe_channels=[1])

hub.light.on(Color.RED)

motorgar = Motor(Port.E)
motorsel = Motor(Port.C)

cor = ColorSensor(Port.F)

omnitrix = StopWatch()

while True:
    motorgar.run(200)
    motorsel.run_angle(720, 180, wait=False)
    wait(5400)
    motorgar.run(-200)
    wait(3400)
    motorsel.run_angle(720, -180, wait=False)
    wait(2000)