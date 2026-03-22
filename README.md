# Práctica 1: Planificación de Exámenes mediante Búsqueda Local - Ilias Ahmed Ahmed

**Asignatura:** Metaheurísticas  
**Grado:** Ingeniería Informática

## Descripción del Proyecto
Este proyecto se encarga del problema clásico de la planificación de exámenes universitarios utilizando técnicas de optimización combinatoria. 
El objetivo es asignar un conjunto de exámenes a diferentes franjas horarias (slots) y aulas (rooms), minimizando un conjunto de penalizaciones (función objetivo) y respetando restricciones duras como la capacidad de las aulas y evitar que un alumno tenga dos exámenes al mismo tiempo.

Para resolverlo, he implementado:
1. Una **heurística constructiva** para generar una solución inicial.
2. Dos metaheurísticas basadas en **Búsqueda Local**:
   - Estrategia de **Primer Mejor** (First Improvement).
   - Estrategia del **Mejor Vecino** (Best Improvement).

## Estructura del Repositorio
El código está modularizado en los siguientes scripts de Python:

* `main.py`: Script principal que orquesta la ejecución de los experimentos para 3 instancias de distinto tamaño (Pequeña, Media y Grande).
* `generaInstancias.py`: Script (basado en el proporcionado en la práctica) para generar instancias sintéticas reproducibles (estudiantes, exámenes, capacidades, aulas).
* `inicial.py`: Contiene la lógica para construir el mapa de estudiantes y generar la solución inicial desde la que se parte en los algoritmos.
* `funcionObjetivo.py`: Implementa el cálculo de penalizaciones (exámenes consecutivos, mismo día, mala distribución) y los incumplimientos de restricciones duras.
* `busquedaLocal.py`: Implementa la generación de vecindarios y los algoritmos de Búsqueda Local (Primer Mejor y Mejor Vecino).
* `graficas.py`: Funciones auxiliares para generar las curvas de convergencia y las gráficas comparativas de escalabilidad y tiempos que he usado en la memoria.

## Requisitos y Dependencias
El proyecto está desarrollado íntegramente en Python. Solo hace uso de librerías estándar y de análisis/visualización de datos. No se utilizan librerías externas de optimización.

Para ejecutar el código, necesitas instalar las siguientes dependencias:
```bash
pip install numpy pandas matplotlib
```
Y basta con ejecutar el main.py:
```bash
python main.py
```
