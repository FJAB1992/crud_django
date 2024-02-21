# Python web

## Preparación del entorno

  1. Crear un entorno virtual ``` python –m venv nombre_entorno```
  ```bash
  python –m venv nombre_entorno
  ```

  2. Abrir el proyecto

  3. Activar el entorno virtual, para ello nos vamos a la carpeta Scripts y la activamos
  ```bash
  .\Scripts\activate
  ```

  4. Intalar Django ```pip install Django```, para una versión específica ```pip install Django==5.0.1```
  ```bash
  pip install Django
  ```

 5. Crear proyecto de Django ```django-admin startproject nombre_proyecto .```

### . No creará doble carpeta

  ```bash
  django-admin startproject nombre_proyecto .
  ``` 

  6. Ejecutar el proyecto Django
  ```bash
   python manage.py runserver
  ``` 

## Crear aplicación 

```bash
python manage.py startapp nombre
```

## Base de datos

### Modificar en settings.py, base de datos

  1. Instalar cliente de Mysql
  ```bash
  pip install mysqlclient
  ```

  2. Configurar la cadena de conexión en settings.py
  ```python
  DATABASES = {
    'default': {
      'ENGINE': 'django.db.backends.mysql',
      'NAME': 'nombre_de_la_bbdd',
      'USER': 'usuario',
      'PASSWORD': 'contraseña',
      'HOST': 'localhost',
      'POR T': '3306'
    }
  }
  ```

  3. Resolver los warnings de migración
  ```bash
  python manage.py migrate
  
  python manage.py makemigrations
  ```

Será necesario añadir los path de la aplicación (creados en esta), e incluirlos en el path del proyecto


### Nota:En caso de conflictos con la migración, eliminar carpeta migration y realizarla de nuevo. 

## Ejercicio 1 - Listado de nombres

  1. Url del ejercicio ```/ejemplo/usuario/```
  2. Url completa ```http://127.0.0.1:8000/ejemplo/usuario/```

### Ficheros
Los ficheros del ejercicio se encuentran en la carpeta ejemplo


### OJO: recargar cache con: ctrl + shift +r (para  refrescar caché) o ctrl+ r (solo para actualizar)

---------------------------------------------------------------------------------------
Nota: desde el archivo pyvenv.cfg, configuramos desde donde se usa python
---------------------------------------------------------------------------------------

## Configuración de Admin

```bash
python manage.py createsuperuser
```

USER: admin
Password: delorian

# Adicional
Sacar en terminal en models.py los modelos de las tablas, junto con este aviso sobre cómo usarlo: 

```python manage.py inspectdb```


Este es un módulo de modelos autogenerado de Django.
Tendrás que hacer lo siguiente MANUALMENTE para dejarlo limpio:
* Reordenar el orden de los modelos.
* Asegurarte de que cada modelo tiene un campo con primary_key=True
* Asegurarte de que cada ForeignKey y OneToOneField tiene `on_delete` ajustado al comportamiento que desees
* Eliminar las líneas con  `managed=False` si quieres dejar que Django cree, modifique y borre la tabla
* Renombra los modelos como gustes, pero NO renombres los valores de db_table o los campos de las tablas.
