from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, UltrasonicSensor, ColorSensor
from pybricks.parameters import Color, Port, Direction
from pybricks.tools import wait
from pybricks.robotics import DriveBase

hub = PrimeHub(broadcast_channel=1, observe_channels=[2])

ultra = UltrasonicSensor(Port.C)
cordir = ColorSensor(Port.B)
cormeio = ColorSensor(Port.A)
coresq = ColorSensor(Port.D)

motor_esq = Motor(Port.F, positive_direction=Direction.COUNTERCLOCKWISE)
motor_dir = Motor(Port.E)

andar = DriveBase(motor_esq, motor_dir, 63, 133)

Color.SILVER = Color(h=0, s=0, v=75)
cores = (Color.GREEN, Color.SILVER, Color.BLACK, Color.WHITE, Color.BLUE)

reflection = 36  
vel = 150        
kp = 5
ki = 0.01
kd = 25
integral = 0
erro_anterior = 0

def mapeia_verde(sensor):
    # O método .hsv() retorna um objeto com atributos: h (matiz), s (saturação), v (valor/brilho)
    dados = sensor.hsv()
    
    # Validação do Verde: 
    # Matiz geralmente entre 110 e 150 (ajuste se necessário)
    # Saturação alta (linhas pretas/brancas têm saturação muito baixa, perto de 0)
    # Brilho intermediário (preto é muito baixo, branco é muito alto)
    if (100 <= dados.h <= 160) and (dados.s > 45) and (20 <= dados.v <= 70):
        return True
    return False

hub.light.on(Color.BLUE)

while True:
    esq_e_verde = mapeia_verde(coresq)
    dir_e_verde = mapeia_verde(cordir)
    dist = ultra.distance()
    esq = coresq.color()
    dir = cordir.color()
    meio = cormeio.reflection()
    if dist < 100:
        motor_esq.stop()
        motor_dir.stop()
        andar.turn(-105)
        andar.arc(radius=210, angle=215, wait=False)
        wait(1000)
        while not andar.done():
            if cormeio.reflection() < 45:
                andar.stop()
                break
            wait(10)
        integral = 0
        erro_anterior = 0
    else:
        if esq_e_verde and dir_e_verde:
            andar.turn(-210)
            andar.straight(100)
        elif esq_e_verde:
            andar.turn(-105)
            andar.straight(100)
        elif dir_e_verde:
            andar.turn(105)
            andar.straight(100)
        else:
            if esq == Color.WHITE and meio > 97 and dir == Color.WHITE:
                motor_esq.run(vel)
                motor_dir.run(vel)
            else:
                erro = reflection - meio
                integral = integral + erro
                if integral > 100: integral = 100
                if integral < -100: integral = -100
                derivada = erro - erro_anterior
                correcao = (kp * erro) + (ki * integral) + (kd * derivada)
                if correcao > 200: correcao = 200
                if correcao < -200: correcao = -200
                if dir != Color.WHITE: correcao = 500
                if esq != Color.WHITE: correcao = -300
                motor_esq.run(vel + correcao)
                motor_dir.run(vel - correcao) 
                erro_anterior = erro
    wait(10)
    print("esquerda: {}, meio: {}, direita: {}, distância: {}".format(esq, meio, dir, dist))