# Desafio LATAM

![badge1](https://img.shields.io/badge/language-Python-blue.svg)

## General

Este desafío consiste en desplegar un modelo de ML que busca predecir la probabilidad de atraso de un vuelo con origen Santiago de Chile y múltiples destinos.
Para mayor información, ver detalles del desafío en el documento [Challenge](https://github.com/jdpinedaj/desafio_latam_ML/blob/master/document/Challenge%20-%20ML%20Engineer.pdf).

### Para correr la API:

#### Localmente

La API puede utilizarse de la siguiente manera:
`pip install pipenv`
`pipenv install --system --deploy --ignore-pipfile`
`pipenv shell`
`cd TO/PATH`
`uvicorn main:app --reload`

#### Usando Docker

Sin embargo, recomiendo usar docker como se m uestra a continuación:

cd a la carpeta de la app: `cd PATH/TO/desafio_latam_ML`
Corre docker: `docker-compose up --build -d`

#### Para encontrar soluciones

Recomendación: ve a tu buscador en http://localhost/docs (Asumiendo que tu docker se aloje alli, si no es asi, revisa que `docker ps` esté en el puerto 80).
Después de esto, puedes testear la API directamente en el GUI: http://localhost/docs

### Archivos

'notebooks-implementation.ipynb' contiene el jupyter notebook donde los análisis al modelo entrregado por el data scientist son realizados.
'main.py' contiene el codigo relacionado con la API.
'test_main.py' contiene el test case para validar que el modelo esté funcionando correctamente.
'Dockerfile' configura el servidor e instala las dependencias. Para este desafío he utilizado Uvicorn/FastApi
'docker-compose.yml' simplifica la ejecución para desplegar Docker.
