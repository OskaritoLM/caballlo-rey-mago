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
MQTT_TOPIC = "utng/ors/ky-004"
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

def publicar_mensaje(msg):
    client.publish(MQTT_TOPIC, msg)

def verificar_presion():
    while True:
        boton = sensor.value()  # Lee el valor del sensor (0 o 1)

        if boton == 0:
            led.on()
            print("Presionado")
            oled.fill(0)
            oled.text("Presionado", 0, 0)
            oled.text("", 0, 10)
            oled.show()
            publicar_mensaje(b'1')  # Enviar el valor numérico 1 al broker MQTT
        else:
            led.off()
            print("Sin Presionar")
            oled.fill(0)
            oled.text("No Presion", 0, 0)
            oled.text("Presion", 0, 10)
            oled.text("detectada", 0, 20)
            oled.show()
            publicar_mensaje(b'0')  # Enviar el valor numérico 0 al broker MQTT
        time.sleep(1)

conectar_wifi()
client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER, port=MQTT_PORT, user=MQTT_USER, password=MQTT_PASSWORD, keepalive=0)
client.connect()

verificar_presion()
