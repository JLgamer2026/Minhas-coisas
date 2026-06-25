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

reflection = 36
vel = 200
kp = 2

hub.light.on(Color.BLUE)

while True:
    esq = coresq.color()
    dir = cordir.color()
    meio = cormeio.reflection()
    erro = (reflection - meio)
    certo = (kp * erro)
    if esq != Color.WHITE or dir != Color.WHITE:
        if esq != Color.WHITE and meio < reflection:
            while esq != Color.WHITE:
                motor_esq.run(vel / 3)
                motor_dir.run(vel / 3)
                wait(20)
                esq = coresq.color()
        elif dir == dir != Color.WHITE and meio < reflection:
            while dir == dir != Color.WHITE:
                motor_esq.run(-vel / 3)
                motor_dir.run(-vel / 3)
                wait(20)
                dir = cordir.color()
        else:
            if esq == esq != Color.WHITE:
                motor_esq.run_angle(vel, 90, wait=False)
                motor_dir.run_angle(vel, 45, wait=True)
                motor_esq.run_angle(-vel, 90, wait=False)
                motor_dir.run_angle(vel, 90, wait=True)
            elif dir == dir != Color.WHITE:
                motor_esq.run_angle(-vel, 90, wait=False)
                motor_dir.run_angle(-vel, 45, wait=True)
                motor_esq.run_angle(-vel, 90, wait=False)
                motor_dir.run_angle(vel, 90, wait=True)
    else:
        if meio < reflection:
            motor_esq.run(-vel - certo)
            motor_dir.run(vel)
        elif meio > reflection:
            motor_esq.run(-vel)
            motor_dir.run(vel - certo)
    wait(10)
    print("esquerda: {}, meio: {}, direita: {}".format(esq, meio, dir))