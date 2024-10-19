# Proyecto CURA Healthcare Service

CURA Healthcare Service es una app web en la que puedes agendar una cita médica.

## Descripción

El proyecto de estas pruebas automatizadas, se basan en una cita médica.

- La prueba realizada en este proyecto, está basada en el verificar el Login de la aplicación web y la información del Home Page.

## Características

- El proyecto se ha realizado en Python - Selenium
- Se ha tenido en cuenta las pruebas de la página de inicio y el funcionamiento del Login.
- Se tuvo en cuenta la creación de funciones para reducir el código y así reducir el tiempo de ejecución de las pruebas
- Se organizó el proyecto por medio de una estructura para su facil mantenimiento

## Pasos

- Clona el proyecto
- Instala Python, en caso de no tenerlo
- Instala selenium, en caso de no tenerlo
- Ejecuta prueba a prueba o todas las pruebas directamente desde RUN en Pycharm desde el archivo "main"

## Tecnologías utilizadas

En el proyecto, se realizaron las pruebas usando Selenium y el lenguaje de programación Python.
Se necesitó importar las librerías:
- webdriver
- By

El código se organizó según el patrón de diseño POM (Page Object Model) y Helper classes, por lo que se inluyeron los siguientes archivos.
- TestHomePage: como el archivo donde se crearon las funciones tests para la verificación de la interfax y funcionamiento del Home Page
- HomePage: es el archivo donde se encuentra cada uno de los localizadores de la página y de cada modal que se muestra a lo largo del proceso, tambien en donde se desarrolla cada función del proceso para cada acción.
- TestLoginPage: como el archivo donde se crearon las funciones tests para la verificación de la interfax y funcionamiento del Login Page
- LoginPage: es el archivo donde se encuentra cada uno de los localizadores de la página y de cada modal que se muestra a lo largo del proceso, tambien en donde se desarrolla cada función del proceso para cada acción.
- Actions: es el archivo en donde se crearon todas las funciones básicas para reducir el código al máximo.
  las acciones son:
  - Escribir en un campo de texto
  - Obtener el texto de un campo de texto
  - Obtener el texto de un elemento
  - Hacer click en un elemento
  - Verificar que el texto actual coincide con el esperado

## Nota

Se están desarrollando más pruebas. POr eso hay archivos aún vacíos.

## Creditos

- Jenny Nataly Pabón Yañez, QA Engineer - Proyecto - Creación de pruebas automatizadas del loging y el home page.
