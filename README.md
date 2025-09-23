# Sistema de Evaluación de Proyectos Estudiantiles

## Descripción del proyecto

Este proyecto implementa un sistema automatizado para evaluar proyectos presentados por estudiantes en una feria de ciencias escolar.
A partir de los datos de varias rondas de evaluación, y mediante el procesamiento de información estructurada, se calcula un ranking final con los equipos más destacados.

---

## Requisitos

- Python 3.6 o superior  
- Módulos estándar de Python (sin dependencias externas)  
- Para la notebook interactiva: Jupyter Notebook (opcional)

---

## Instalación y Ejecución

1. Clonar el repositorio o descargar el proyecto.

2. Crear y activar un entorno virtual (opcional):

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
   ```
3. Para ejecutar el análisis interactivo abrir la notebook:
   jupyter notebook notebooks/feria_de_ciencias.ipynb
   (Si no está instalada se puede usar pip install notebook).

4. Para ejecutar scripts Python directamente (opcional), crear un archivo `.py` que importe las funciones desde `src/` y ejecutarlo con:

   ```bash
   python ruta/al_script.py
   ```
---

## Funcionamiento

- El programa carga los datos de evaluaciones desde un archivo JSON.
- Para cada ronda, calcula el puntaje de cada equipo según la fórmula:
  - +3 puntos por innovación
  - +1 punto por presentación
  - −1 punto si hubo errores graves
- Determina el Mejor Equipo de cada ronda (MER).
- Actualiza el acumulado total por equipo de:
  - Total de puntos de innovación
   - Total de puntos de presentación
   - Cantidad de errores
   - Veces que fue el mejor equipo
   - Puntos totales
- Muestra una tabla de resultados después de cada ronda y una final, ordenada por puntaje total en orden decreciente.
- Al finalizar, muestra una tabla y un resumen con el equipo ganador o ganadores.

---

##  Estructura del Proyecto

mi_proyecto/
├── src/                         # Código fuente con las funciones principales (evaluaciones.py, procesos.py)
│   ├── evaluaciones.py          # Funciones de cálculo y acumulado
│   └── procesos.py              # Funciones para procesar rondas y mostrar resultados (importa evaluaciones)
│
├── notebooks/                   # Notebook Jupyter para análisis y ejecución interactiva
│   └── feria_de_ciencias.ipynb  # Notebook principal que importa y ejecuta el código desde src
│
├── datos/                       # Archivo con datos de entrada
│   └── datos.json               # Datos con 5 rondas de evaluación
│
├── README.md                    # Documentación del proyecto
└── .gitignore                   # Archivos y carpetas que Git ignora

---

## Autor

- Nombre: Mariana Grau
- Curso: Taller de Lenguajes
- Universidad: Universidad Nacional de La Plata (UNLP)
- Email: marianagrau99@gmail.com

---



