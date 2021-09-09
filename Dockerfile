# Using lightweight alpine image
#por poblemas con la configuracion se recomienda ejecutar este documento para instalar dependencias y hacer pruebas
#posteriormente ejecuetar el docker-composer para el lanzamiento con el proxy
FROM python:3-alpine

#definicion de variable de entorno
ENV GRUP_ID=1000 \  
    USER_ID=1000


# instalacion de dependencias
RUN apk update
RUN pip install --no-cache-dir pipenv

# definicion de direccion de trabajo y adicion de recursos
WORKDIR /usr/src/app
COPY Pipfile Pipfile.lock bootstrap.sh ./
COPY cashman ./cashman

# intalacion de dependencias de la api
RUN pipenv install

# puerto de salida
EXPOSE 5000
#en este caso bostrap hace la funcion de lanzador y da la salida por la ip publica o localhost
ENTRYPOINT ["/usr/src/app/bootstrap.sh"]