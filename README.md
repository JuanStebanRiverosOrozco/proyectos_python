# Proyectos Python con Entornos Virtuales – Proyecto__A y Proyecto__B (Windows)

## Descripción General

Este repositorio contiene dos proyectos desarrollados en Python, cada uno con su propio entorno virtual configurado exclusivamente para Windows.

Cada proyecto demuestra cómo crear, activar y utilizar entornos virtuales, instalar paquetes específicos y ejecutar scripts o notebooks de manera independiente.

Los proyectos se han diseñado con el propósito de fomentar buenas prácticas en la gestión de entornos virtuales, aislar dependencias y mantener un control estructurado del código fuente.

---

## Versión de Python Utilizada

**Python 3.13.7**

Se recomienda utilizar esta versión para garantizar compatibilidad con los paquetes instalados y el funcionamiento correcto de los entornos virtuales.

---

## Estructura del Repositorio
```
PROYECTOS_PYTHON/
│
├─ proyecto__A/
│  ├─ venv_1/               ← No se incluye en el repositorio
│  ├─ img/                  ← Carpeta para evidencias o capturas
│  ├─ .gitignore
│  ├─ proyecto_1.py
│  ├─ proyecto_1.ipynb
│  ├─ requirements.txt
│  └─ readme.md
│
└─ proyecto__B/
   ├─ venv_2/  
   ├─ img/              ← No se incluye en el repositorio
   ├─ .gitignore
   ├─ proyecto_2.py
   ├─ proyecto_2.1.py
   ├─ requirements.txt
   └─ readme.md
```

---

## Proyecto__A

**Carpeta:** `proyecto__A`  
**Entorno virtual:** `venv_1`  
**Paquete instalado:** `jupyter`

El Proyecto__A muestra el uso de Jupyter Notebooks dentro de un entorno virtual creado en Windows.

Incluye un script Python y un notebook interactivo para demostrar el uso de bibliotecas y ejecución de código dentro del entorno controlado.

### Archivos Incluidos

- **`proyecto_1.py`**: Script principal del proyecto que ejecuta funciones básicas en Python.
- **`proyecto_1.ipynb`**: Notebook de Jupyter donde se documentan y ejecutan ejemplos.
- **`requirements.txt`**: Archivo que contiene las dependencias del entorno virtual.
- **`.gitignore`**: Archivo configurado para excluir el entorno virtual `venv_1/`.

### Pasos para la Ejecución (Windows)

**Crear el entorno virtual:**
```bash
python -m venv venv_1
```

**Activar el entorno virtual:**
```bash
venv_1\Scripts\Activate.bat
```

**Instalar el paquete requerido:**
```bash
pip install jupyter
```

**Generar el archivo requirements.txt:**
```bash
pip freeze > requirements.txt
```

**Ejecutar el script o notebook:**
```bash
python proyecto_1.py
jupyter notebook proyecto_1.ipynb
```

---

## Proyecto__B

**Carpeta:** `proyecto__B`  
**Entorno virtual:** `venv_2`  
**Paquete instalado:** `pandas`

El Proyecto__B se enfoca en el procesamiento de datos utilizando el paquete pandas.

Contiene dos scripts Python que realizan operaciones de lectura, manipulación y análisis básico de datos.

### Archivos Incluidos

- **`proyecto_2.py`**: Script principal que realiza operaciones con datos.
- **`proyecto_2.1.py`**: Script complementario con cálculos adicionales.
- **`requirements.txt`**: Archivo con las dependencias instaladas.
- **`.gitignore`**: Archivo configurado para excluir `venv_2/`.

### Pasos para la Ejecución (Windows)

**Crear el entorno virtual:**
```bash
python -m venv venv_2
```

**Activar el entorno virtual:**
```bash
venv_2\Scripts\Activate.bat
```

**Instalar el paquete requerido:**
```bash
pip install pandas
```

**Generar el archivo requirements.txt:**
```bash
pip freeze > requirements.txt
```

**Ejecutar los scripts:**
```bash
python proyecto_2.py
python proyecto_2.1.py
```

---

## Archivos y Carpetas Ignorados

Los entornos virtuales no deben subirse al repositorio.

Cada proyecto incluye su propio archivo `.gitignore` con las siguientes líneas:
```
venv_1/
venv_2/
```

Esto evita que las carpetas de entornos virtuales locales sean rastreadas por Git, manteniendo limpio el repositorio.

---

## Recomendaciones Generales

- Ejecuta cada proyecto desde su carpeta correspondiente (`proyecto__A` o `proyecto__B`).
- Activa el entorno virtual antes de instalar o ejecutar los paquetes.
- No edites manualmente los archivos `requirements.txt`; deben generarse con `pip freeze`.
- Los entornos virtuales no deben compartirse entre proyectos.
- Usa Visual Studio Code o una terminal configurada para Windows para evitar errores de activación.

---

## Evidencias Recomendadas

Capturas guardadas dentro de la carpeta `proyecto__A/img` y `proyecto__B/img`.

- Creación de los entornos virtuales (venv_1 y venv_2)
- Activación de los entornos
- Instalación de los paquetes (jupyter y pandas)
- Ejecución de los scripts y notebooks
- Contenido de los requirements.txt
- Vista de la estructura del proyecto en Visual Studio Code o terminal
