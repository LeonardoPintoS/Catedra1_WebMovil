# Cátedra I - Introducción al Desarrollo Web Móvil

**Universidad Católica del Norte - Departamento de Ingeniería en Sistemas y Computación**
**Segundo Semestre 2026**

---

## Descripción

La plataforma de backend tiene como objetivo resolver el problema de la gestión de reservas de espacios en una institución, para ello debe de cumplir con ciertas funciones y parámetros como evitar reservas duplicadas, que siempre este disponible la visibiliidad de los datos y del historial, evitar inconsistencias de datos, entre otras. La plataforma esta desarrollada con FastAPI la cual implementa una API REST completa para gestionar a los usuarios, realizar reservas, consultar espacios, etc, validando la regla del negocio principal de superposición de horarios.

---

## Instalación

Para instalar y ejecutar el proyecto localmente se debe seguir los siguientes pasos:

### 1. Prerrequisitos

Debe tener instalado python en la versión 3.10 o superior, para saber que versión tiene puede revisarlo en la terminal escribiendo:

```bash
python --version
```

### 2. Código del proyecto

Debe clonar el repositorio en su computadora o también puede descargar el archivo como .zip y descomprimirlo en su computador.

Para clonarlo debe crear una carpeta nueva, acceder a la terminal de esta y escribir:

```bash
git clone <URL_DEL_REPOSITORIO>
cd Catedra1.1
code .
```

De esta manera accederá al proyecto.

### 3. Entorno Virtual

Para que las librerias se instalen en el entorno del proyecto debe activar un entorno virtual, este depederá de su sistem operativo.

Primero créalo ejecutando:

```bash
python -m venv venv
```

* Para inicializarlo con powershell:

```powershell
venv\Scripts\activate
```

* Para inicializarlo con CMD:

```bat
venv\Scripts\activate.bat
```

* Para inicializarlo en MAC o Linux:

```bash
source venv/bin/activate
```

### 4. Instalar las dependencias

Para instalar las dependencias:

```bash
pip install -r requirements.txt
```

### 5. Configurar base de datos

Para configurar la base de datos debe verificar que el archivo alembic.ini contenga la ruta local de SQLite configurada en el parámetro sqlalchemy.url:

```ini
sqlalchemy.url = sqlite:///./database.db
```

Luego debe ejecutar el comando de Alembic para poder crear las tablas automáticamentes en la base de datos:

```bash
alembic upgrade head
```

### 6. Cargar datos iniciales

Para poder poblar la base de datos con los valores mínimos debe ejecutar:

```bash
python -m app.seed
```

### 7. Ejecutar la aplicación

Para arrancar el servidor utilizando Uvicorn debe ingresar:

```bash
python -m uvicorn main:app --reload
```

### 8. Acceder a la interfaz

Una vez que el servidor haya notificado que el servidor se ha iniciado debe ingresar a su navegador y tendrá dos opciones:

* Ingresar a la documentación Interactiva: http://127.0.0.1:8000/docs
* Ingresar a la documentación alternativa: http://127.0.0.1:8000/redoc

## Arquitectura
```
Catedra1.1/
├── app/
│   ├── models.py           # Modelos ORM de SQLAlchemy (Usuario, Espacio, Reserva)
│   ├── schemas.py          # DTOs y validaciones de entrada/salida con Pydantic
│   ├── database.py         # Configuración central de la sesión y conexión SQLite
│   ├── dependencies.py     # Inyección de dependencias para las sesiones de la base de datos
│   ├── middleware.py       # Middleware para registro y medición de tiempos de respuesta
│   ├── seed.py             # Script reproducible para poblar datos iniciales mínimos
│   ├── routers/            # Controladores HTTP por entidad (usuarios, espacios, reservas)
│   ├── services/           # Lógica de negocio y validación de reglas
│   └── repositories/       # Capa de persistencia y consultas mediante Patrón Repository
├── alembic/                # Control de versiones del esquema de base de datos
│   └── versions/           # Archivos de migración generados
├── alembic.ini             # Configuración principal de Alembic y conexión a BD
├── main.py                 # Punto de entrada de la aplicación FastAPI y registro de routers
├── requirements.txt        # Dependencias de Python del proyecto
└── database.db             # Archivo de base de datos SQLite local
```