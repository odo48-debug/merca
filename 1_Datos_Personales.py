import os
import streamlit as st

# Configuración de título y subtítulo
st.subheader("Bienvenido a tu planificador de compras en Mercadona 🛒")

# Inicializar variables de sesión si no existen
if "nombre" not in st.session_state:
    st.session_state["nombre"] = ""
    st.session_state["despensa"] = ""

# Capturar datos del usuario
nombre = st.text_input("¿Cómo te llamas?", st.session_state["nombre"])
despensa = st.text_input("¿Qué cosas no pueden faltar en tu despensa?", st.session_state["despensa"])

# Botón para enviar los datos
submit = st.button("Enviar")
if submit:
    if nombre.strip() == "" or despensa.strip() == "":
        st.error("Por favor, completa todos los campos antes de continuar.")
    else:
        # Guardar los datos en la sesión
        st.session_state["nombre"] = nombre
        st.session_state["despensa"] = despensa

        # Mostrar mensaje de bienvenida
        st.success(f"¡Hola {nombre}, anotado! Ahora puedes ir al asistente.")

      


