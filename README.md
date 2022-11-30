# ProyectoFinalCoder-Pares-Lezcano-Bazalar

Desarrollado en Windows 10.

Proyecto Final entregable para CODERHOUSE.


Explicacion para poner el proyecto en funcionamiento:

En Git bash o bash
Realizar un:
```bash
git clone https://github.com/SleepD4rt/ProyectoFinalCoder-Pares-Lezcano-Bazalar.git
```
Ya cuenta con una base de datos para mostrar su contenido. 

Entrar en el directorio del proyecto.

```bash
cd ProyectoFinalCoder-Pares-Lezcano-Bazalar
```
En bash tipear para entrar en el IDE de VisualStudioCode (si se lo tiene como IDE predeterminado).

```bash
code .
```

En el VSC tipear en el terminal para crear el ambiente de desarrollo "venv".
Copiar y pegar/Escribir y ejecutar por linea.
```bash
python -m venv venv

venv/Scrips/activate
```
Teniendo en funcionamiento el entorno venv.
instalar los requerimientos para ejecutar el proyecto:
```bash
pip install -r requirements.txt
```


Crear un super usuario:
Se va a requerir ya que tiene que haber un superadmin, capaz de permitir que ciertos usuarios tengan roles de Staff, para poder agregar, editar o eliminar series/peliculas: (Decision de funcionamiento para la aplicación)
```bash
python manage.py createsuperuser
```

Escribir si se quiere un nombre de usuario, puede darle Enter, es opcional introducir un nombre de usuario. Lo mismo para el email. (No es de importancia).
Contraseña una sencilla como para probarlo. si es sencilla le va a salir un cartel de advertencia ignorelo tipeando "y" y pulse Enter.

ejecutar el servidor:

```bash
python manage.py runserver
```
Explicacion de uso de la App desde el video en este link:

https://www.youtube.com/watch?v=axqEmfKFEII


Trabajo divido entre los participantes.

Gastón Pares:

Realice la App "serie", y acomode el HTML, realize herencias sobre el mismo, aplique la capa de seguridad al proyecto, corregi varios errores de sintaxis y logica, realice los templates de login y registro.

Lucas Ivan Lezcano:

Realice la app "movies" , use herencia de HTML , realice los templates de detail , editar y eliminar movies , editar y cambiar contraseñas de usuario y  fui aportando ayuda al resto del proyecto trabajando con mi compañero.


Laureano Bazalar:
Se presto a realizar el proyecto los primeros dias, pero se notaba que no sabia como avanzar en el proyecto, con lo basico, requeria ayuda constante, no dijo nada realicionado con el mismo hasta el dia 28/11/2022, dia de entrega del proyecto, por lo que basicamente no realizo nada. 

