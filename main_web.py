import random as rd
import streamlit as st

# Listas de caracteres
M = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
abc = [letra.lower() for letra in M]
S = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '', '{', '|', '}', '~']

# Título de la aplicación
st.title("Generador de Contraseñas")

# Entrada de usuario para la longitud de la contraseña
select = st.slider("Seleccione el número de caracteres de su contraseña:", min_value=6, max_value=128, value=12)

# Entrada de usuario para incluir caracteres especiales
incluir_especial = st.checkbox("¿Desea incluir caracteres especiales?")

# Inicializar la contraseña con el primer carácter en mayúscula
password = rd.choice(M)

# Generar el resto de la contraseña
for _ in range(select - 1):
    if incluir_especial:
        # Incluir caracteres especiales
        password += rd.choice(M + abc + S)
    else:
        # No incluir caracteres especiales
        password += rd.choice(M + abc)

# Mostrar la contraseña generada
st.write("Su nueva contraseña es:")
st.text(password)
