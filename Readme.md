#Readme

## Versiones requeridas
- Python 3.8  

## Dependencias adicionales
- tensorflow: `pip install tensorflow`  
- tensorflow-hub: `pip install tensorflow-hub`  
- annoy: `pip install annoy`  
- falcon: `pip install falcon gunicorn`

## Modo de ejecucion
- Para correr el server local usar el siguiente comando:  `gunicorn upload-image:api` que servirá el endpoint en http://127.0.0.1:8000/upload-image

