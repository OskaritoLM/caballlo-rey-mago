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



 ## Software Utilizado
|Nombre de Software|Versión|Tipo|
|--|--|--|
|Thonny|4.1.2|Software Libre|
|Visual Studio Code|1.82.2|Software Libre (Editor de código fuente independiente)|
|Platformio IDE|3.3.0|Software Libre (Herramienta Desarrollo C)|
|Arduino IDE|2.2.1|Aplicación multiplataforma|


## Comunicación
la comunicacion entre laprimera Esp32 se dirige al movimiento, contiene un sensor ultrasonico colocado a un costado de la carreta integrada, ese sensor activa el primer movimiento al detectar una distancia de 10cm activando el movimiento de las patas del caballo y encendiendo los leds integrados en la carreta, despues de que temine la cabalgata procede a ejecutar el movimiento del brazo del jinete dando la impresion de que esta arreandolo y al mismo tiempo enciende dos buzzers conetados en la carreta y el encendido de los leds cambia a prenderse al ritmo de las dos melodias integradas, esto es en cuanto al movimiento por sensor.
En lo programado en la segunda Esp realizamos la comunicacion remotamente usando la app de telegrama usando la llamada ala una API de comunicacion a un bot creado mediante la misma aplicacion, esto nos proporciona la capacidad de mandarle mensajes al bot y que los reprodusca una Led Matriz MAX7219 conectada a esta y tambien mediante el bot recibir un mensaje de conexion en donde el usuario resiva un mensaje de "Feliz navidad" en su chat de Telegram.
## Arquitectura
Colocar una imagen donde coloques los sensores, los actuadores, el microcontrolador
![Imagen de los componentes, la arquitectura](https://github.com/RamiroHerreraX/Personaje/blob/main/imagenes/Arquitectura.jpg?raw=true)

## Base de Datos
![Imagen del modelo relacional de la base de datos](https://github.com/RamiroHerreraX/Personaje/blob/main/imagenes/Modelo%20Relacional%20BD.jpg?raw=true)

## Video Funcionamiento

https://github.com/OskaritoLM/caballlo-rey-mago/assets/116208760/3e999ee5-30a9-44be-b821-5c7649ee1d26


## Prototipo en dibujo
![Imagen de WhatsApp 2023-11-08 a las 22 07 55_495f7ef4](https://github.com/18Manu/Personaje/assets/116208760/d20bba6b-53a1-44a6-b7f2-bc16c7301c58)


## Diagrama en Wokwi
![image](https://github.com/OskaritoLM/caballlo-rey-mago/assets/116208760/7b31bd00-4875-4e54-883b-53685c4a57b0)


## Flujo de conexion remota
### creacion de bot en telegram
![image](https://github.com/OskaritoLM/caballlo-rey-mago/assets/116208760/1d5e96b7-9179-45e8-8b91-a14a67ef500a)

### Codigo para enlazar 
![Captura de pantalla 2023-12-12 222815](https://github.com/OskaritoLM/caballlo-rey-mago/assets/116208760/557a354a-9e1b-4bd8-ab05-b4dafac54546)

### link para mandar el mensaje generado 
![Imagen de WhatsApp 2023-12-12 a las 21 16 23_2600e4df](https://github.com/OskaritoLM/caballlo-rey-mago/assets/116208760/01443951-accd-4f65-a085-f32eb70cdf2b)
