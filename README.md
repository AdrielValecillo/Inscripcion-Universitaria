# Sistema de Inscripción Universitaria

Este proyecto es un sistema de inscripción universitaria desarrollado con FastAPI para el backend. A continuación se detallan los pasos necesarios para configurar y ejecutar el proyecto localmente.

## Requisitos previos

- Python 3.9 o superior instalado en tu sistema.
- Git instalado para clonar el repositorio.
- Un gestor de bases de datos compatible (como Oracle, PostgreSQL, etc.).

## Pasos para ejecutar el proyecto

### 1. Crear un entorno virtual con Python

```bash
py -m venv env
```

Esto creará un entorno virtual aislado en el directorio `env`.

### 2. Activar el entorno virtual

En Windows:

```bash
.\env\Scripts\activate
```

En macOS/Linux:

```bash
source env/bin/activate
```

### 3. Instalar las dependencias del proyecto

Ejecuta el siguiente comando para instalar todas las dependencias necesarias:

```bash
pip install -r requirements.txt
```

### 4. Configurar las variables de entorno

1. Crea un archivo llamado `.env` en el directorio raíz del proyecto.
2. Copia el contenido del archivo `env.txt` dentro del archivo `.env`.
3. Ajusta los valores de las variables de entorno según las necesidades del proyecto, como la configuración de la base de datos y claves secretas.

### 5. Iniciar el proyecto

Ejecuta el siguiente comando para iniciar el servidor de desarrollo:

```bash
fastapi dev app/main.py
```

### 6. Abrir la aplicación en el navegador

Abre tu navegador web y accede a la siguiente URL:

[http://localhost:8000/](http://localhost:8000/)

## Contribuciones

Si deseas contribuir al proyecto, crea un *fork* del repositorio, realiza tus cambios en una nueva rama y envía un *pull request*. Agradecemos cualquier mejora o corrección.
