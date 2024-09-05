# Usa una imagen base oficial de Python
FROM python:3.9-slim

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia el archivo de requerimientos (si existe) al directorio de trabajo
#COPY requirements.txt ./

# Instala las dependencias necesarias
RUN pip install streamlit

# Copia todos los archivos de la aplicación al directorio de trabajo
COPY . .

# Expone el puerto en el que Streamlit corre por defecto
EXPOSE 8501

# Comando para ejecutar la aplicación
CMD ["streamlit", "run", "main_web.py"]
