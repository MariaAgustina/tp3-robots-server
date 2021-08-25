#Readme
## Creacion de carpetas
- Debe estar descargado el repo de yolov5 en la raiz del proyecto
- Debe haber una carpeta creada vacia, llamada results, en donde se guardaran las corridas de yolo
- Debe haber una carpeta creada vacia, llamada uploaded-images, en donde se guardaran las imagenes que vienen de la app

## Librerias de python
- Se debe instalar la libreria falcon con el comando: `pip install falcon gunicorn`

## Server
- Para correr el server local usar el siguiente comando:  `gunicorn upload-image:api` que servirá el endpoint en http://127.0.0.1:8000/upload-image
