# Proyecto-IA

## Descripción del Problema
El proyecto aborda el desafío de entrenar a un agente de inteligencia artificial para jugar VizDoom, un entorno de simulación que simula diferentes escenarios de combate en primera persona.

## Solución Propuesta
La solución propuesta implica el entrenamiento de un agente de IA utilizando técnicas de aprendizaje por refuerzo para que pueda aprender a navegar y tomar decisiones óptimas dentro del entorno de VizDoom.

## Tipo de Proyecto: Resolver un Juego

### Descripción del Ambiente
- **Tipo**: Dinámico, Estocástico.
- **Discreto/Continuo**: Discreto.
- **Determinista/Estocástico**: Estocástico.

### Representación del Estado del Juego
El estado del juego se representa mediante una matriz que captura la información relevante del entorno, como la disposición de los obstáculos, la ubicación del jugador, y otros elementos del juego.

### Acciones del Agente
- **Tipo**: Discretas.
- **Dominio**: Las acciones del agente están limitadas a un conjunto discreto de movimientos y acciones dentro del juego.

### Representación de las Acciones
Las acciones del agente se representan mediante un conjunto de vectores de acción, donde cada vector codifica una acción específica que el agente puede realizar en el juego.

## Contenido del Repositorio

### Requisitos
El archivo `requirements.txt` contiene las dependencias del proyecto:

### Código Fuente
El archivo `main.py` contiene el código fuente del proyecto, que incluye la inicialización del entorno de VizDoom, la definición de acciones para el agente, y el bucle principal de entrenamiento.

