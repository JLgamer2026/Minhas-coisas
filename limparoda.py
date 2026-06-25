from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, UltrasonicSensor, ColorSensor 
from pybricks.parameters import Color, Port
from pybricks.tools import wait
from pybricks.robotics import DriveBase

hub = PrimeHub(broadcast_channel=1, observe_channels=[2])

ultra = UltrasonicSensor(Port.C)
cordir = ColorSensor(Port.D)
cormeio = ColorSensor(Port. A)
coresq = ColorSensor(Port.B)

motor_esq = Motor(Port.F)
motor_dir = Motor(Port.E)

andar =  DriveBase(motor_esq, motor_dir, 62.4, 133)

andar.turn(180)