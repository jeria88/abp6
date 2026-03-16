# 🌌 Alke Astral - Calculadora de Carta Astral

**Desarrollado por:** Franco Jeria  
**Módulo:** Desarrollo Web con Django: Fundamentos (ABP6)

Alke Astral es una herramienta web moderna diseñada para entusiastas de la astrología. Permite calcular el "Big Three" (Sol, Luna y Ascendente) de forma rápida y visual, utilizando una interfaz basada en *Glassmorphism* y el flujo de trabajo del framework Django.

---

## 🚀 Instalación y Uso

Siga estos pasos para ejecutar el proyecto en su entorno local:

### 1. Requisitos Previos
* Python 3.12+
* Entorno virtual configurado

### 2. Configuración del Entorno
```bash
# Crear el entorno virtual
python -m venv venv

# Activar el entorno (Linux/Mac)
source venv/bin/activate

# Instalar dependencias (Django 6.0.3)
pip install -r requirements.txt

```

### 3. Base de Datos y Servidor

```bash
# Aplicar migraciones iniciales
python manage.py migrate

# Iniciar el servidor
python manage.py runserver

```

La aplicación estará disponible en: `http://127.0.0.1:8000/`

---

## 🔐 Acceso al Administrador

Para revisar el panel de administración de Django, utilice las siguientes credenciales:

| Usuario | Correo | Contraseña |
| --- | --- | --- |
| **admin** | admin@alke.cl | `123456` |

---

## 📂 Estructura del Proyecto

El proyecto sigue la arquitectura MVT (Model-View-Template) de Django:

ABP6/
├── mi_proyecto/                      # Carpeta contenedora principal
│   ├── mi_proyecto/                  # Directorio raíz de Django
│   │   ├── mi_app/                   # Aplicación "Alke Astral"
│   │   │   ├── migrations/           # Registros de cambios en la base de datos
│   │   │   ├── static/               # Archivos estáticos
│   │   │   │   └── css/
│   │   │   │       └── style.css     # Estilos personalizados (Glassmorphism)
│   │   │   ├── templates/            # Plantillas HTML
│   │   │   │   └── inicio.html       # Interfaz de la calculadora
│   │   │   ├── admin.py              # Configuración del panel de administración
│   │   │   ├── apps.py               # Configuración de la aplicación
│   │   │   ├── astrologia.py         # Lógica de cálculo de signos
│   │   │   ├── models.py             # Modelos de datos
│   │   │   ├── tests.py              # Pruebas unitarias
│   │   │   ├── urls.py               # Rutas internas de la app
│   │   │   └── views.py              # Lógica de las vistas y procesamiento
│   │   ├── mi_proyecto/              # Configuración global del proyecto
│   │   │   ├── settings.py           # Ajustes generales (INSTALLED_APPS, STATIC, etc.)
│   │   │   ├── urls.py               # Rutas principales del sitio
│   │   │   ├── asgi.py               # Interfaz de servidor asíncrono
│   │   │   └── wsgi.py               # Interfaz de servidor síncrono
│   │   ├── db.sqlite3                # Base de datos local (creada tras migrate)
│   │   └── manage.py                 # Comando central para ejecutar el proyecto
│   └── venv/                         # Entorno virtual (no se incluye en el .zip final)
├── informe.pdf                       # Documento explicativo final
└── README.md                         # Archivo de documentación del repositorio

---

## ⚙️ Flujo de una Petición

1. **Request:** El usuario ingresa su nombre, fecha y hora de nacimiento en el formulario raíz (`/`).
2. **URLs:** `mi_proyecto/urls.py` delega la petición a `mi_app/urls.py`.
3. **View:** La función `inicio` en `views.py` detecta el método `POST`.
4. **Logic:** Se procesan los datos mediante `astrologia.py`.
5. **Response:** Se renderiza `inicio.html` con los resultados del "Big Three" inyectados en el contexto.

---

## 🛠️ Tecnologías Utilizadas

* **Django 6.0.3** (Framework backend)
* **Python 3.12**
* **Bootstrap 5** (Layout y componentes)
* **CSS3 Custom** (Efectos de transparencia y animaciones)
* **SQLite** (Base de datos por defecto)

```# abp6
