from machine import Pin, I2C
import time
import network
from umqtt.simple import MQTTClient
from ssd1306 import SSD1306_I2C  

Pin_Led = 2  
Pin_Sensor = 14  

led = Pin(Pin_Led, Pin.OUT)
sensor = Pin(Pin_Sensor, Pin.IN)

# Configuración de la pantalla OLED
i2c = I2C(scl=Pin(22), sda=Pin(21))  # Cambia los pines SCL y SDA según tu configuración
oled_width = 128
oled_height = 64
oled = SSD1306_I2C(oled_width, oled_height, i2c)

MQTT_BROKER = "broker.hivemq.com"
MQTT_USER = ""
MQTT_PASSWORD = ""
MQTT_CLIENT_ID = ""
MQTT_TOPIC = "utng/ors/ky-020"
MQTT_PORT = 1883

def conectar_wifi():
    print("Conectando...", end="")
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    sta_if.connect('UTNG_Alumnos', '')  
    while not sta_if.isconnected():
        print(".", end="")
        time.sleep(0.3)
    print("WiFi Conectada!")

def publicar_mensaje(client, msg):
    client.publish(MQTT_TOPIC, str(msg))  # Convert boolean to string and publish

def verificar_movimiento():
    client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER, user=MQTT_USER, password=MQTT_PASSWORD, port=MQTT_PORT)
    client.connect()
    
    while True:
        magnetismo = sensor.value()  # Lee el valor del sensor (0 o 1)

        if magnetismo == 1:
            led.on()
            print(1)
            oled.fill(0)
            oled.text("Movimiento", 0, 0)
            oled.text("detectado!", 0, 10)
            oled.show()
            publicar_mensaje(client, 1)  # Publish numerical value 1
        else:
            led.off()
            print(0)
            oled.fill(0)
            oled.text("No hay campo", 0, 0)
            oled.text("movimiento", 0, 10)
            oled.text("detectado", 0, 20)
            oled.show()
            publicar_mensaje(client, 0)  # Publish numerical value 0
        time.sleep(1)

verificar_movimiento()
