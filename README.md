# Pacific DevOps Music Fest

## Descripción

Pacific DevOps Music Fest es un proyecto desarrollado como práctica de DevOps utilizando tecnologías de desarrollo web, control de versiones y contenedores. El proyecto incluye un frontend para mostrar información del festival y un backend desarrollado con Flask que expone una API con datos del evento.

## Tecnologías Utilizadas

### Frontend

* HTML5
* CSS3

### Backend

* Python 3
* Flask

## Docker

Docker permite empaquetar la aplicación junto con todas sus dependencias en contenedores, garantizando que funcione de manera consistente en diferentes entornos.

Comando para construir la imagen:

```bash
docker build -t festival-api .
```

Comando para ejecutar el contenedor:

```bash
docker run -p 5000:5000 festival-api
```

## Docker Compose

Docker Compose facilita la administración y ejecución de múltiples servicios mediante un único archivo de configuración.

Comando para iniciar los servicios:

```bash
docker compose up -d
```

Comando para detener los servicios:

```bash
docker compose down
```

## Git

Git es un sistema de control de versiones que permite registrar cambios en el código fuente y gestionar el desarrollo mediante ramas y commits.

Comandos utilizados:

```bash
git init
git add .
git commit -m "mensaje"
git checkout -b nombre-rama
git merge nombre-rama
```

## GitHub

GitHub es una plataforma que permite alojar repositorios Git en la nube y facilitar el trabajo colaborativo.

Comandos utilizados para publicar el proyecto:

```bash
git remote add origin URL_REPOSITORIO
git push -u origin main
```

## Autor

Santiago Jaramillo

Proyecto realizado para la actividad de aprendizaje de Git y GitHub del programa DevOps y Contenedores (Docker) del SENA.
