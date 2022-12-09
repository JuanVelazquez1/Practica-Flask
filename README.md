# practica-flask
 Práctica 2 Arquitecturas Avanzadas.

El objetivo de esta práctica es que 3 agentes intenten llegar a un consenso respecto a la elección de un número aleatorio a través del estilo de arquitectura Restful (usando Flask).

El funcionamiento es el siguiente:
 - Se generarán 3 números aleatorios entre 0 y 9 mediante un post en ("/generateNumber"),
 cada uno de estos se añadirá al array numbers[].
  - Se printearán los 3 números aleatorios mediante un get de ("/numbers").
  - Se comprobará si 2 de los 3 números generados son iguales mediante un get de ("/check"),
  si lo son, se devolverá el número elegido, si no lo son, se devolverá "No consensus".
   - Si se ha devuelto un número, se terminará la ejecución. Si, en cambio, se ha devuelto "No consensus", se repetirá todo el proceso.

Una vez se llegue a un consenso, se calculará cuantos intentos se han necesitado para conseguirlo.

Para ejecutar se deberá lanzar en una terminal la app.py con el comando: python -m flask run y en otra lanzarse el programa agents.py
