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

andar = DriveBase(motor_esq, motor_dir, 63, 133)
andar.settings(straight_speed=150)

hub.imu.reset_heading(0)

bat = hub.battery.voltage()
print(bat)
while True:
    # Captura o objeto de cor bruta (sem arredondamentos)
    cor_atual = cordir.hsv()
    
    # Extrai os componentes individuais
    matiz = cor_atual.h       # Hue (0 a 359)
    saturacao = cor_atual.s   # Saturation (0 a 100)
    brilho = cor_atual.v      # Value/Brightness (0 a 100)
    
    # Exibe formatado no terminal
    print(f"H: {matiz:3d} | S: {saturacao:3d} | V: {brilho:3d}")
    
    wait(200) # Pequena pausa para o terminal não rolar rápido demais
