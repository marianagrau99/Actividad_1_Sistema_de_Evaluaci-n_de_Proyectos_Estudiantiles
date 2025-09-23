# Sistema de Evaluación de Proyectos Estudiantiles

##  Enunciado

Este proyecto implementa un sistema automatizado para evaluar proyectos presentados por estudiantes en una feria de ciencias escolar.
A partir de los datos de varias rondas de evaluación, y mediante el procesamiento de información estructurada, se calcula un ranking final con los equipos más destacados.

---

##  Objetivos

1. Calcular el puntaje de cada equipo en cada ronda según:
   - +3 puntos por cada punto en **Innovación**
   - +1 punto por cada punto en **Presentación**
   - −1 punto si hubo **Errores graves**
2. Determinar el **Mejor Equipo de cada Ronda (MER)**.
3. Mantener un acumulado por equipo de:
   - Total de puntos de innovación
   - Total de puntos de presentación
   - Cantidad de errores
   - Veces que fue el mejor equipo
   - Puntos totales
4. Mostrar una tabla de resultados después de cada ronda y una final, ordenada por puntaje total en orden decreciente.
5. Mostrar el equipo ganador o ganadores al final del proceso.

---

##  Estructura del Proyecto

mi_proyecto/
│
├── src/ # Código fuente (funciones)
│ └── evaluaciones.py # Funciones principales para procesar los datos
│ └── programa.py # Script principal de ejecución
│
├── notebooks/ # Notebooks de ejecución
│ └── feria_de_ciencias.ipynb # Notebook que importa y ejecuta el código
│
├── datos.json # Datos de entrada con 5 rondas de evaluación
├── README.md # Este archivo
└── .gitignore # Archivos a ignorar por Git

---

##  Requisitos Técnicos

- Uso de funciones bien definidas en un módulo separado (`src/evaluaciones.py`)
- Uso de map() y filter()
- Diccionarios, listas y tuplas para manejo de datos
- Código ejecutable tanto desde `programa.py` como desde el Notebook
- Archivo `README.md` completo
- Estructura modular

---



