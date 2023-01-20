#Readme

## Versiones requeridas
- Python 3.8  

## Dependencias adicionales
- tensorflow: `pip install tensorflow`  
- tensorflow-hub: `pip install tensorflow-hub`  
- annoy: `pip install annoy`  
- falcon: `pip install falcon gunicorn`

## Modo de ejecucion
- Para correr el server local usar el siguiente comando:  `gunicorn --bind 0.0.0.0:8000 upload-image:app` que servirá el endpoint en http://127.0.0.1:8000/upload-image
- Para poder pegarle desde un dispositivo externo hay que cambiar localhost por la ip de la computadora donde esté corriendo el server que se puede ver en la settings del wifi

 
