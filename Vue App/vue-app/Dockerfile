#imagen de linux a usar
FROM node:lts-alpine

#eliminar los archivos de node_modules y package-lock.json si existen
RUN rm -rf /app/node_modules
RUN rm -f /app/package-lock.json

#crear el directorio de trabajo
RUN mkdir /app

#asignar /app como directorio de trabajo
WORKDIR /app

#copiar archivos en /app
COPY package*.json ./

#instalar la app en el contenedor
RUN npm install --silent

#instalar Firebase y http-server como dependencias
RUN npm install firebase@latest http-server --save
#instalar axios
RUN npm install axios

#copiar todos los archivos locales al contenedor
COPY . .

#construir la app dentro del contenedor
RUN npm run build

#exponer el puerto del contenendor
EXPOSE 8080

#correr el comando para correr la app final
CMD ["npx", "http-server", "dist"]