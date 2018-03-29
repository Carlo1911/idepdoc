# idepdoc
**Plataforma para crear documentos**

## Instalación

```sh
sudo apt-get update
sudo apt-get install -y python3-pip git build-essential python3-dev
sudo apt-get install mysql-server libmysqlclient-dev
```

### Creación de entorno virtual (fuera de la carpeta del proyecto)

Instalar virtualenv:
```
sudo -H pip3 install virtualenv
```
-Crear directorio de entorno virtual: `mkdir env`

-Crear entorno: `virtualenv --python=python3 --no-site-package --distribute env`

-Levantar entorno: `source env/bin/activate`

-Instalar dependencias con el entorno activado: `pip3 install -r requirements.txt`

### Creación de BD

Acceder a mysql y ejecutar los comandos para la creación de la BD
```
mysql -u root -p

CREATE DATABASE docDB CHARACTER SET utf8 COLLATE utf8_general_ci;
CREATE USER 'doc_user'@'localhost' IDENTIFIED BY 'doc_password';
GRANT ALL PRIVILEGES ON docDB.* TO 'doc_user'@'localhost';
FLUSH PRIVILEGES;
quit

```

### Configuración extra

Una vez descargado el repositorio y dentro de este crear el archivo .env
```sh
touch .env
```
Copiar directamente de aquí o del archivo .env_copy dentro del proyecto

```sh
DB_NAME="docDB"
DB_USER="admin"
DB_PASSWORD="XXXXXXX"
DB_HOST="localhost"
DB_PORT="3306"

EMAIL_HOST="smtp.gmail.com"
EMAIL_HOST_USER="*****@gmail.com"
EMAIL_HOST_PASSWORD="*****"
EMAIL_HOST_PORT="587"

STATIC_URL="/static/"
MEDIA_URL="/media/"

``` 

### Correr el programa

-Activar el entorno virtual
```sh
source env/bin/activate
```
-Ingresar a la carpeta del proyecto y levantar el servidor
```sh
python manage.py runserver
```