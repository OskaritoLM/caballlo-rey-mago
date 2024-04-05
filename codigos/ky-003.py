from machine import Pin, I2C
import time
import network
from umqtt.simple import MQTTClient
from ssd1306 import SSD1306_I2C  

Pin_Sensor = 14  
Pin_LED = 13  # Cambia esto al número de pin adecuado

sensor = Pin(Pin_Sensor, Pin.IN)
led = Pin(Pin_LED, Pin.OUT)

# Configuración de la pantalla OLED
i2c = I2C(scl=Pin(22), sda=Pin(21))  # Cambia los pines SCL y SDA según tu configuración
oled_width = 128
oled_height = 64
oled = SSD1306_I2C(oled_width, oled_height, i2c)

MQTT_BROKER = "broker.hivemq.com"
MQTT_USER = ""
MQTT_PASSWORD = ""
MQTT_CLIENT_ID = ""
MQTT_TOPIC = "utng/ors/ky-003"
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

def verificar_magnetismo():
    while True:
        magnetismo = sensor.value()  # Lee el valor del sensor (0 o 1)

        if magnetismo == 0:
            led.on()
            print("¡Línea magnética detectada!")
            oled.fill(0)
            oled.text("Línea magnética", 0, 0)
            oled.text("detectada", 0, 10)
           oled.show()
            publicar_mensaje(b'1')  # Enviar el valor numérico 1 al broker MQTT
        else:
            led.off()
            print("No hay línea magnética detectada")
            oled.fill(0)
            oled.text("No hay línea", 0, 0)
            oled.text("magnética", 0, 10)
            publicar_mensaje(b'0')  # Enviar el valor numérico 0 al broker MQTT
            oled.show()
        time.sleep(5)

conectar_wifi()
client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER, port=MQTT_PORT, user=MQTT_USER, password=MQTT_PASSWORD, keepalive=0)
client.connect()

verificar_magnetismo()


