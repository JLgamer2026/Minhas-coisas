from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, UltrasonicSensor, ColorSensor 
from pybricks.parameters import Color, Port, Direction
from pybricks.tools import wait
from pybricks.robotics import DriveBase

hub = PrimeHub(broadcast_channel=1, observe_channels=[2])

ultra = UltrasonicSensor(Port.C)
cordir = ColorSensor(Port.D)
cormeio = ColorSensor(Port. A)
coresq = ColorSensor(Port.B)

motor_esq = Motor(Port.F, positive_direction=Direction.COUNTERCLOCKWISE)
motor_dir = Motor(Port.E)
p = 10
andar = DriveBase(motor_esq, motor_dir, 63, 133)
andar.settings(straight_speed=500)
hub.imu.reset_heading(0)
while True:
    guinada = hub.imu.heading()
    motor_esq.run(200 - (p * guinada))
    motor_dir.run(200 + (p * guinada))