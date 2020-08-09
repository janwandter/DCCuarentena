# Tarea 00: DCCahuín <img src="img4.jpg height="5%" width="5%">

## Consideraciones generales :warning:
* La plataforma comienza bien, da la bienvenida y ofrece las opciones de iniciar sesion, resgistrarse y salir. En cuanto al registro de un usuario, al crear uno nuevo, se vuelve al menú principal, donde se tiene que iniciar sesión con este.

* Todo menú tiene incluido la posibilidad de un error de tecleo, por lo que si no se indica una opción ofrecida se indicará el error. En el caso del menú de ingreso, estará de vuelta en ese menú; en el caso del menú principal (donde se ofrece acceder al menú de prograpost o seguidores), estará de vuelta en ese menú; en el caso de cualquier menú de aquí en adelante, el error enviará al usuario de vuelta al menu principal. 

* Cabe mencionar que la eleccion Descendiente de orden, se refiere a ver los últimos posts creados al principio y los primeros al final, y viceversa al elegir la opción Ascendente.

### Cosas implementadas y no implementadas :heavy_check_mark: :x:

* **Menú de Usuarios**:
    * **Menú de Inicio**: Hecho completo
* **Flujo del Programa**:
    * **Menú de Posts**: Hecho completo
    * **Menú Seguidores**: Hecho completo
    * **Menú Posts**: Hecho completo
* **Archivos**:
    * **usuarios.csv**: Hecho completo
    * **seguidores.csv**: Hecho completo
    * **posts.csv**: Hecho completo 
   


## Ejecución :rewind: :arrow_forward: :fast_forward:
El módulo principal de la tarea a ejecutar es  ```MenuDCC.py```. Además se debe crear los siguentes archivos:
1. Carpeta ```ArchivosDCC``` en directorio
2. ```posts.csv``` en ```ArchivosDCC```
3. ```seguidores.csv``` en ```ArchivosDCC```
4. ```usuarios.csv``` en ```ArchivosDCC```



## Librerías :books:
### Librerías externas utilizadas :closed_book:
La lista de librerías externas que utilicé fueron las siguientes:

1. ```datetime```: ```date.today()```
2. ```os```: ```path.join()``` 
3. ```sys``` : ```exit()```

### Librerías propias :notebook:
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```ClasesDCC```: contiene a las clases ```Usuario```, ```Seguidos```, ```Posts```


## Supuestos y consideraciones adicionales :memo:
Los supuestos que realicé durante la tarea son los siguientes:

1. El orden de visualización de los posts está realizado según la fecha, por lo que al crearse  dos posts en un dia estos no cambiaran el orden según se elija Descendiente o Ascendente, ya que el orden no se maneja de acuerdo a la hora de creación.

2. Los usuarios al entrar a las opciones: Iniciar sesión, registrarse, crear prograpost, seguir un usuario, dejar de seguir un usuario. Van a ejecutarlas y no volver atrás. Si necesitan volver atrás pueden no cumplir con las condiciones


-------




## Referencias de código externo :link:

Para la realización de la tarea no hubo utilización de códigos externos.