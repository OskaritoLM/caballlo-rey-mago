from machine import Pin, I2C
from time import sleep
import network
from ssd1306 import SSD1306_I2C

KY_PIN = 14

ky = Pin(KY_PIN, Pin.IN)

# OLED Configuration
i2c = I2C(scl=Pin(22), sda=Pin(21))
oled_width = 128
oled_height = 64
oled = SSD1306_I2C(oled_width, oled_height, i2c)

def conectar_wifi():
    print("Conectando a WiFi", end="")
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    sta_if.connect('Adrian', '123456ad')
    while not sta_if.isconnected():
        print(".", end="")
        sleep(0.1)
    print("  Connected!  ")

conectar_wifi()

while True:
    valor = ky.value()
    if valor == 1:
        print("Libre")
        oled.fill(0)
        oled.text("Libre", 0, 0)
    elif valor == 0:
        print("Obstáculo")
        oled.fill(0)
        oled.text("Obstáculo", 0, 0)
    
    oled.show()
    sleep(4)
