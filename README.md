# Personaje
## Integrantes
Jose Manuel Mata Hernandez
Oscar Ramirez Sanchez
Valeria Gomez Herrera
## Nombre del personaje
Caballo Rey Mago
## Materiales utilizados
| Nombre de Componente   | Descripción del componente | Cantidad | Precio |
|------------------------|-----------------------------|----------|--------|
| esp32                  | Microcontrolador           | 2        | $140    |
| Sensor Ultrasonico           |  dispositivo que utiliza ondas ultrasónicas para medir la distancia entre el sensor y un objeto.| 1        | $45    |
| leds         | Los LEDs (diodos emisores de luz, por sus siglas en inglés) son dispositivos semiconductores que emiten luz cuando se les aplica una corriente eléctrica.| 5       | $1    |
| cable H-M M-H H-H                  | coneccines para la comunicacion entre el microcontrolador y componente.|   60     | $69    |
| motor a pasos con Driver                | motor eléctrico que convierte pulsos eléctricos en movimientos angulares discretos o pasos.| 1       | $69   |
| servomotor | motor utilizado para controlar el movimiento de un objeto o sistema mecánico de manera precisa| 1       | $40   |
| Matriz MAX7219| dispositivo que permite la conexión y el control de una matriz de diodos emisores de luz (LEDs) de manera eficiente. El MAX7219 es un controlador de matriz de LEDs que facilita la interfaz entre un microcontrolador y la matriz de LEDs, permitiendo el control de la iluminación de cada LED de manera independiente | 1        | $140    |
| buzzer| dispositivo electromecánico o piezoeléctrico que produce un sonido o zumbido continuo cuando se le aplica una corriente eléctrica.|   2  | $10    |
| cargador USB tipos v8 | conexion alambrica para cargar el codigo al microcontrolador y conectar ala energia electrica   | 1        | $140    |
| cargador USB tipos c | conexion alambrica para cargar el codigo al microcontrolador y conectar ala energia electrica   | 1        | $140    |
 Software Utilizado
|Nombre de Software|Versión|Tipo|
|--|--|--|
|Thonny|4.1.2|Software Libre|
|Visual Studio Code|1.82.2|Software Libre (Editor de código fuente independiente)|
|Platformio IDE|3.3.0|Software Libre (Herramienta Desarrollo C)|
|Arduino IDE|2.2.1|Aplicación multiplataforma|


## Comunicación



Describir el protocolo de comunicación que tendra el dispositivo. Describir o hablar sobre como va a interactuar un dispositivo móvil.
Como se conecta o como mandar una orden al dispositivo. (Cómo interactua el usuario con el prototipo)

Para crear un prototipo de un caballo de un rey mago eléctrico que se conecta a través de una placa ESP32 y utilizar sensores para emitir luz, sonido y moverse, estamos considerando la comunicación y la interacción con el usuario. Nos basamos en el uso de tecnologías inalámbricas comunes, como Wi-fi o Bluetooth.
A continuación se describe como podría funcionar: 

Wi-Fi o Bluetooth: La placa ESP32 podría estar equipada con módulos Wi-Fi o Bluetooth para la comunicación. Estas tecnologías permiten que el dispositivo sea detectado y controlado por un dispositivo móvil cercano.
Configuración Inicial: Cuando el dispositivo se encienda por primera vez o entre en modo de configuración, podría actuar como un punto de acceso Wi-Fi o activar la función de emparejamiento Bluetooth. El usuario podría conectarse a este punto de acceso o emparejar el dispositivo desde su dispositivo móvil.
Aplicación Móvil: El usuario podría descargar una aplicación móvil específica para interactuar con el pastor eléctrico.
Interfaz de Usuario: La aplicación móvil proporcionaría una interfaz de usuario que permite al usuario configurar y controlar el pastor eléctrico. Esto incluiría ajustar la intensidad de la luz, mover las partes movibles, que podría ser la mano para hacer un saludo y emitir el sonido.

## Arquitectura
Colocar una imagen donde coloques los sensores, los actuadores, el microcontrolador
![Imagen de los componentes, la arquitectura](https://github.com/RamiroHerreraX/Personaje/blob/main/imagenes/Arquitectura.jpg?raw=true)

## Base de Datos
Colocar una imagen del modelo relacional de la base de datos (2 tablas) tabla de sensores y actuadores
![Imagen del modelo relacional de la base de datos](https://github.com/RamiroHerreraX/Personaje/blob/main/imagenes/Modelo%20Relacional%20BD.jpg?raw=true)

## Video esplicacion


## Prototipo en dibujo
![Imagen de WhatsApp 2023-11-08 a las 22 07 55_495f7ef4](https://github.com/18Manu/Personaje/assets/116208760/d20bba6b-53a1-44a6-b7f2-bc16c7301c58)


## Diagrama en Wokwi
![Captura de pantalla 2023-11-08 224230](https://github.com/18Manu/Personaje/assets/116208760/f76099b5-0a13-466f-8a16-abd65436611f)
