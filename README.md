# 💰 Mi Gestor de Gastos

## 📌 Descripción del proyecto

**Mi Gestor de Gastos** es un programa desarrollado en Python que permite analizar los gastos semanales de una persona utilizando datos ficticios.

El objetivo de este proyecto es practicar conceptos básicos de programación, como listas, bucles, condiciones y funciones, para calcular gastos y comprobar si se supera un presupuesto semanal.

## 🎯 Objetivos

- Guardar varios gastos en una lista.
- Calcular el total de los gastos semanales.
- Calcular el gasto medio.
- Identificar los gastos que superan una cantidad determinada.
- Comprobar si el gasto total supera un presupuesto semanal de 100 €.
- Organizar el código utilizando funciones.
- Permitir al usuario introducir un límite personalizado para filtrar los gastos.

## ⚙️ Funcionalidades

El programa incluye las siguientes funcionalidades:

1. **Lista de gastos:** almacena cinco gastos ficticios.
2. **Cálculo del total:** suma todos los gastos mediante un bucle o una función.
3. **Cálculo de la media:** calcula el gasto medio dividiendo el total entre el número de gastos.
4. **Filtro de gastos:** muestra los gastos que superan el límite indicado por el usuario.
5. **Control del presupuesto:** comprueba si el gasto total supera los 100 € semanales.
6. **Funciones:** utiliza funciones para organizar las operaciones y facilitar la reutilización del código.
7. **Control de listas vacías:** evita errores al calcular la media cuando no hay gastos registrados.

## 🛠️ Tecnologías utilizadas

- **Python 3**
- **Git y GitHub**

## 📂 Estructura del proyecto

```text
mi-gestor-gastos/
│
├── mi_gestor_gastos.py
└── README.md
```

- `mi_gestor_gastos.py`: contiene el código fuente del programa.
- `README.md`: contiene la descripción, los objetivos y las instrucciones del proyecto.

## ▶️ Cómo ejecutar el programa

### 1. Requisitos previos

Tener Python 3 instalado en el ordenador.

### 2. Clonar el repositorio

```bash
git clone URL_DE_TU_REPOSITORIO
```

Sustituye `URL_DE_TU_REPOSITORIO` por la dirección de tu repositorio de GitHub.

### 3. Acceder a la carpeta del proyecto

```bash
cd mi-gestor-gastos
```

### 4. Ejecutar el programa

```bash
python mi_gestor_gastos.py
```

Si tu sistema utiliza el comando `python3`, puedes ejecutar:

```bash
python3 mi_gestor_gastos.py
```

## 🧪 Ejemplo de funcionamiento

El programa trabaja con cinco gastos ficticios. Por ejemplo:

```text
Gastos semanales: [12, 25, 8, 35, 15]

Total de gastos: 95 €
Gasto medio: 19 €

Gastos superiores a 20 €:
25 €
35 €

El gasto total está dentro del presupuesto semanal de 100 €.
```

Además, el usuario puede introducir un límite personalizado para consultar qué gastos lo superan.

*Nota: los resultados son ejemplos ilustrativos y pueden variar según los datos utilizados.*

## 📚 Conceptos de programación practicados

Durante el desarrollo de este proyecto se trabajan los siguientes conceptos:

- **Listas:** para almacenar los gastos.
- **Bucles `for`:** para recorrer la lista y calcular el total.
- **Condicionales `if` y `else`:** para filtrar gastos y comprobar el presupuesto.
- **Funciones:** para organizar y reutilizar el código.
- **Entrada de datos:** para permitir que el usuario introduzca un límite personalizado.
- **Operaciones matemáticas:** para calcular el total y la media.
- **Control de errores:** para evitar la división entre cero cuando la lista está vacía.

## 🚀 Posibles mejoras futuras

- Permitir introducir gastos nuevos por teclado.
- Añadir categorías, como alimentación, transporte y ocio.
- Guardar los gastos en un archivo para consultarlos más adelante.
- Mostrar estadísticas adicionales.
- Crear una interfaz gráfica.

## 👨‍💻 Autor

Proyecto educativo desarrollado para practicar los fundamentos de Python y aprender a utilizar GitHub.

## 📄 Licencia

Este proyecto se ha creado con fines educativos.

