from machine import Pin, I2C
from ssd1306 import SSD1306_I2C 
import time
import network
from umqtt.simple import MQTTClient

Pin_Led = 2  
Pin_Laser = 14  

led = Pin(Pin_Led, Pin.OUT)
laser = Pin(Pin_Laser, Pin.IN)

# Configura la conexión I2C para la pantalla OLED  # Cambia los pines SCL y SDA según tu configuración
i2c = I2C(scl=Pin(22), sda=Pin(21))  # Cambia los pines SCL y SDA según tu configuración
oled_width = 128
oled_height = 64
oled = SSD1306_I2C(oled_width, oled_height, i2c)


MQTT_BROKER = "broker.hivemq.com"
MQTT_USER = ""
MQTT_PASSWORD = ""
MQTT_CLIENT_ID = ""
MQTT_TOPIC = "utng/ors/ky-008"
MQTT_PORT = 1883

# Crea el cliente MQTT fuera de la función verificar_laser


def conectar_wifi():
    print("Conectando...", end="")
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    sta_if.connect('UTNG_Alumnos', '')  
    while not sta_if.isconnected():
        print(".", end="")
        time.sleep(0.3)
    print("WiFi Conectada!")
    return sta_if

def publicar_mensaje(msg):
    if isinstance(msg, int):
        msg = str(msg).encode()  # Convert integer to bytes
    client.publish(MQTT_TOPIC, msg)

def verificar_laser():
    while True:
        laser_state = laser.value()  # Recogemos la señal que se recibe por el pin del láser

        if laser_state == 1:
            led.on()
            oled.fill(0) 
            oled.text("Laser: Si", 0, 0)
            oled.show()
            
            time.sleep(1)  
        else:
            led.off()
            oled.fill(0)  
            oled.text("Laser: No", 0, 0)
            oled.show()
            publicar_mensaje(laser_state)  # Send integer data directly
            print(laser_state)
        
        time.sleep(0.1)

def toggle_laser():
    laser_pin = Pin(13, Pin.OUT)
    while True:
        laser_pin.on()
        time.sleep(1)
        laser_pin.off()
        time.sleep(3)

conectar_wifi()
client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER, port=MQTT_PORT, user=MQTT_USER, password=MQTT_PASSWORD, keepalive=0)
client.connect()
verificar_laser()