from machine import Pin, PWM, SoftI2C
import ssd1306
from time import sleep
import network
from umqtt.simple import MQTTClient

# Configuración de los pines para el LED RGB
green_pin = 33
blue_pin = 32
red_pin = 25

# Inicialización de PWM para controlar los LED RGB
green_pwm = PWM(Pin(green_pin), freq=5000)
blue_pwm = PWM(Pin(blue_pin), freq=5000)
red_pwm = PWM(Pin(red_pin), freq=5000)

# Configuración del cliente MQTT
MQTT_BROKER = "broker.hivemq.com"
MQTT_USER = ""
MQTT_PASSWORD = ""
MQTT_CLIENT_ID = ""
MQTT_TOPIC = "utng/ors/ky-009"
MQTT_PORT = 1883

# Función para manejar los mensajes MQTT recibidos
def llegada_mensaje(topic, msg):
    print("Mensaje recibido:", msg)

# Función para suscribirse al topic MQTT
def subscribir():
    client = MQTTClient(MQTT_CLIENT_ID,
                        MQTT_BROKER, 
                        user=MQTT_USER,
                        password=MQTT_PASSWORD)
    client.set_callback(llegada_mensaje)
    client.connect()
    client.subscribe(MQTT_TOPIC)
    print("Conectado a %s, en el topico %s" % (MQTT_BROKER, MQTT_TOPIC))
    return client

# Función para conectar a la red WiFi
def conectar_wifi():
    print("Conectando a WiFi", end="")
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    sta_if.connect('UTNG_Alumnos', '')
    while not sta_if.isconnected():
        print(".", end="")
        sleep(0.1)
    print("  Connected!  ")

# Función para mostrar el color en la pantalla OLED
def mostrar_color(color, valor):
    oled.fill(0)
    oled.text("Color: " + color, 0, 0)
    oled.text("Valor: " + str(valor), 0, 10)
    oled.show()

colores = [
    {"nombre": "rojo", "green": 0, "blue": 0, "red": 1023},
    {"nombre": "blanco", "green": 1023, "blue": 1023, "red": 1023},
    {"nombre": "verde", "green": 1023, "blue": 0, "red": 0},
    {"nombre": "azul", "green": 0, "blue": 1023, "red": 0}
]


# Conexión a WiFi y suscripción al broker MQTT
conectar_wifi()
client = subscribir()

# Configuración de la pantalla OLED
i2c = SoftI2C(scl=Pin(22), sda=Pin(21))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

while True:
    for color in colores:
        # Configurar los PWM de los LED RGB con los valores correspondientes al color
        green_pwm.duty(color["green"])
        blue_pwm.duty(color["blue"])
        red_pwm.duty(color["red"])

        # Mostrar el color y su valor en la pantalla OLED
        mostrar_color(color["nombre"], color[color["nombre"].lower()])
        
        # Publicar el valor numérico del color en el topic MQTT
        msg = str(color[color["nombre"].lower()])
        client.publish(MQTT_TOPIC, msg)
        
        # Esperar 10 segundos antes de cambiar al siguiente color
        sleep(10)

