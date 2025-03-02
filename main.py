import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Inicializamos la lista de vectores en session_state para mantenerlos en la sesión
if "vectores" not in st.session_state:
    st.session_state.vectores = {}

st.title("Prueba de Vectores Interactiva")
st.write("Ingresa los datos de un vector y presiona **Agregar vector** para graficarlo.")

# Entradas para el vector
nombre = st.text_input("Nombre del vector (ej. A, B, W, etc.)", value="")
x = st.number_input("Coordenada X", value=0.0)
y = st.number_input("Coordenada Y", value=0.0)

# Botón para agregar el vector
if st.button("Agregar vector"):
    if nombre != "":
        st.session_state.vectores[nombre] = (x, y)
        st.success(f"Vector {nombre} agregado: ({x}, {y})")
    else:
        st.error("Por favor ingresa un nombre para el vector.")

# Botón para limpiar todos los vectores
if st.button("Limpiar vectores"):
    st.session_state.vectores = {}
    st.success("Se han eliminado todos los vectores.")

# Si hay vectores, se muestran y se grafica
if st.session_state.vectores:
    st.subheader("Vectores agregados:")
    st.write(st.session_state.vectores)

    # Creamos la figura para el gráfico
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.axhline(0, color='black', linewidth=1)
    ax.axvline(0, color='black', linewidth=1)
    ax.grid(True, linestyle='--')

    # Lista de colores para diferenciarlos
    colores = ['red', 'blue', 'green', 'purple', 'orange', 'cyan', 'brown', 'magenta']

    st.write("**Resultados de Cálculos:**")

    # Graficamos cada vector y mostramos sus cálculos
    for i, (nombre, (x, y)) in enumerate(st.session_state.vectores.items()):
        color = colores[i % len(colores)]
        ax.quiver(0, 0, x, y, angles='xy', scale_units='xy', scale=1, color=color, label=f"{nombre} = ({x}, {y})")

        # Calcular magnitud
        magnitud = np.sqrt(x ** 2 + y ** 2)
        # Calcular dirección
        if x == 0 and y != 0:
            direccion = 90 if y > 0 else 270
        else:
            direccion = np.degrees(np.arctan2(y, x))

        # Mostrar cálculos en la app
        st.write(f"**Vector {nombre}:** Magnitud = {magnitud:.2f}, Dirección = {direccion:.2f}°")

        # Mostrar texto en el gráfico
        ax.text(x * 1.1, y * 1.1, f"|{nombre}|={magnitud:.2f}", fontsize=10, color=color)

    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.set_title("Gráfico de Vectores")
    ax.set_xlabel("Eje X")
    ax.set_ylabel("Eje Y")
    ax.legend()

    st.pyplot(fig)
