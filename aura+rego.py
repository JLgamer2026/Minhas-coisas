from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, UltrasonicSensor, ColorSensor 
from pybricks.parameters import Color, Port
from pybricks.tools import wait

hub = PrimeHub(broadcast_channel=1, observe_channels=[2])

ultra = UltrasonicSensor(Port.C)
cordir = ColorSensor(Port.D)
cormeio = ColorSensor(Port. A)
coresq = ColorSensor(Port.B)

motor_esq = Motor(Port.F)
motor_dir = Motor(Port.E)

Color.SILVER = Color(h=0, s=0, v=75)

cores = (Color.GREEN, Color.SILVER, Color.BLACK, Color.WHITE, Color.BLUE)
esq = cordir.color(cores)
dir = coresq.color(cores)

meio = cormeio.reflection()

reflection = 40
vel = 220
kp = 3

hub.light.on(Color.BLUE)

while True:
    esq = coresq.color()
    dir = cordir.color()
    meio = cormeio.reflection()
    erro = (reflection - meio)
    certo = (kp * erro)
    
    if meio < reflection:
            motor_esq.run(-vel - certo)
            motor_dir.run(vel / 2.2)
    elif meio > reflection:
            motor_esq.run(-vel / 2.2)
            motor_dir.run(vel - certo)
    wait(10)
    print("esquerda: {}, meio: {}, direita: {}".format(esq, meio, dir))