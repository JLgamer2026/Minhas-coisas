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

hub.light.on(Color.BLUE)

while True:
    dist = ultra.distance()
    esq = coresq.color()
    dir = cordir.color()
    meio = cormeio.reflection()
    
    # --- 1. CONDICIONAL DE OBSTÁCULO (OBR) ---
    if dist < 100:
        # Para os motores individuais antes de usar o DriveBase
        motor_esq.stop()
        motor_dir.stop()
        
        # Desvio do obstáculo usando arco síncrono ou controlado
        andar.turn(-105)
        
        # Inicia o arco ao redor do obstáculo
        andar.arc(radius=210, angle=215, wait=False)
        wait(1000)
        # Monitora os sensores enquanto faz a curva para voltar à linha com segurança
        while not andar.done():
            # Se o sensor do meio achar a linha preta antes do fim do arco, interrompe
            if cormeio.reflection() < 45:
                andar.stop()
                break
            wait(10)
            
        # Reseta as variáveis do PID para evitar pulos bruscos ao voltar para a linha
        integral = 0
        erro_anterior = 0

    # --- 2. SEGUIDOR DE LINHA PID CONTÍNUO ---
    else:
        if esq == Color.GREEN and dir == Color.GREEN:
            # Meia volta (Beco sem saída)
            motor_esq.stop()
            motor_dir.stop()
            andar.turn(180)
            andar.straight(50)
        elif esq == Color.GREEN:
            # Noventa graus para a esquerda
            motor_esq.stop()
            motor_dir.stop()
            andar.turn(-90)
            andar.straight(50)
        elif dir == Color.GREEN:
            # Noventa graus para a direita
            motor_esq.stop()
            motor_dir.stop()
            andar.turn(90)
            andar.straight(50)
        else:
            if meio < 90:
                erro = reflection - meio
                integral = integral + erro
                if integral > 100: integral = 100
                if integral < -100: integral = -100
                derivada = erro - erro_anterior
                correcao = (kp * erro) + (ki * integral) + (kd * derivada)
                if correcao > 200: correcao = 200
                if correcao < -200: correcao = -200
                motor_esq.run(vel + correcao)
                motor_dir.run(vel - correcao) 
                erro_anterior = erro
            else:
                if esq != Color.WHITE:
                    motor_esq.run(-75)
                    motor_dir.run(0)
                elif dir != Color.WHITE:
                    motor_esq.run(0)
                    motor_dir.run(-75)
                else:
                    if esq == Color.WHITE and meio > 90 and dir == Color.WHITE:
                        motor_esq.run(vel)
                        motor_dir.run(vel)
        # --- 3. VERIFICAÇÃO DE QUADRADOS VERDES (INTERSEÇÃO OBR) ---
        # Deixamos os sensores laterais focados em achar o verde ou correções extremas
    wait(10)
    print("esquerda: {}, meio: {}, direita: {}, distância: {}".format(esq, meio, dir, dist))