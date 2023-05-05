#imagen de linux a usar
FROM node:lts-alpine

#instalar el server http
RUN npm install -g http-server

#crear el directorio de trabajo
RUN mkdir /app

#asignar /app como directorio de trabajo
WORKDIR /app

#copiar archivos en /app
COPY package*.json ./

#instalar la app en el contenedor
RUN npm install

#copiar todos los archivos locales al contenedor
COPY . .

#construir la app dentro del contenedor
RUN npm run build

#exponer el puerto del contenendor
EXPOSE 8080

#correr el comando para correr la app final
CMD [ "http-server", "dist" ]