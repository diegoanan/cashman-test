FROM python:3-alpine

#confifuracion del servicio de nginx asi como su ejecucion

#comando de actualizacion y creacion de los archivos losg y error que detallan los sucesos
#otras configuraciones adicionales
RUN apk --update add nginx && \
    ln -sf /dev/stdout /var/log/nginx/access.log && \
    ln -sf /dev/stderr /var/log/nginx/error.log && \
    mkdir /etc/nginx/sites-enabled/ && \
    mkdir -p /run/nginx && \
    rm -rf /etc/nginx/conf.d/default.conf && \
    rm -rf /var/cache/apk/*
#se hace la clonacion del archivo de configuracion
COPY conf.d/app.conf /etc/nginx/conf.d/app.conf

#puerto de escucha
EXPOSE 80
#comando a consola
CMD ["nginx", "-g", "daemon off;"]