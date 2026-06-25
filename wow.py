from pybricks.hubs import PrimeHub 
from pybricks.pupdevices import Motor, UltrasonicSensor, ColorSensor 
from pybricks.parameters import Color, Port, Direction 
from pybricks.tools import wait
from pybricks.robotics import DriveBase  

hub = PrimeHub(broadcast_channel=1, observe_channels=[2]) 
ultra = UltrasonicSensor(Port.C) 
cordir = ColorSensor(Port.D) 
cormeio = ColorSensor(Port.A) 
coresq = ColorSensor(Port.B) 
motor_esq = Motor(Port.F) 
motor_dir = Motor(Port.E)
andar =  DriveBase(motor_esq, motor_dir, 62.4, 133)

Color.SILVER = Color(h=0, s=0, v=75) 
cores = (Color.GREEN, Color.SILVER, Color.BLACK, Color.WHITE, Color.BLUE) 
reflection = 36 
vel = 200 
kp = 3    
ki = 0.01   
kd = 15.0   
integral = 0
erro_anterior = 0

hub.light.on(Color.BLUE) 

while True:
    dist = ultra.distance() 
    esq = coresq.color() 
    dir = cordir.color() 
    meio = cormeio.reflection() 
    erro = reflection - meio 
    integral = integral + erro
    if dist < 100:
        while 
    else: 
        if meio < 45:
            if integral > 100: integral = 100
            if integral < -100: integral = -100
            derivada = erro - erro_anterior
            correcao = (kp * erro) + (ki * integral) + (kd * derivada)
            if correcao < -200: correcao = -200 
            motor_esq.run(-(vel + correcao)) 
            motor_dir.run(vel - correcao) 
            erro_anterior = erro
        else:
            if esq != Color.WHITE:
                motor_esq.run(100)
                motor_dir.run(200)
            elif dir != Color.WHITE:
                motor_esq.run(-200)
                motor_dir.run(-100)
    wait(10) 
    print("esquerda: {}, meio: {}, direita: {}, distância: {}".format(esq, meio, dir, dist))