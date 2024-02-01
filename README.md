# Python web

## Preparación del entorno

  1. Crear un entorno virtual ``` python –m venv nombre_carpeta```
  ```bash
  python –m venv nombre_carpeta
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

 5. Crear proyecto de Django ```django-admin startproject nombre_proyecto```
  ```bash
  django-admin startproject nombre_proyecto
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
  ```


## Ejercicio 1 - Listado de nombres

  1. Url del ejercicio ```/ejemplo/usuario/```
  2. Url completa ```http://127.0.0.1:8000/ejemplo/usuario/```

### Ficheros
Los ficheros del ejercicio se encuentran en la carpeta ejemplo


OJO: recargar cache con: ctrl + shift +r (para  refrescar caché) o ctrl+ r (solo para actualizar)
