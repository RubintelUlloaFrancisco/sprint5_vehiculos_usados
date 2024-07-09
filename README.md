# Proyecto de Análisis de Vehículos Usados

## Descripción del Proyecto
Este proyecto se centra en el análisis de un conjunto de datos de vehículos usados en los Estados Unidos. El objetivo principal es proporcionar información valiosa sobre los precios de los vehículos, la relación entre el odómetro y el precio, y otros factores importantes que afectan el valor de un vehículo. La aplicación web desarrollada permite a los usuarios visualizar estos datos de manera interactiva.

## Características de la Aplicación
- **Visualización de datos**: Histogramas y gráficos de dispersión interactivos que permiten explorar la distribución de los precios y el odómetro de los vehículos.
- **Interfaz amigable**: Utiliza Streamlit para una presentación limpia y fácil de usar.
- **Análisis en tiempo real**: Los usuarios pueden cargar nuevos conjuntos de datos y realizar análisis instantáneamente.

## Instalación
Para ejecutar este proyecto localmente, sigue estos pasos:

1. **Clonar el repositorio**:
   ```bash
   git clone https://github.com/RubintelUlloaFrancisco/pp_sprint5.git
   cd pp_sprint5
   ```

2. **Crear y activar un entorno virtual**:
   ```bash
   python -m venv vehicles_env
   .ehicles_env\Scriptsctivate
   ```

3. **Instalar las dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

## Uso
Para ejecutar la aplicación web localmente:

1. **Activar el entorno virtual**:
   ```bash
   .ehicles_env\Scriptsctivate
   ```

2. **Ejecutar la aplicación de Streamlit**:
   ```bash
   streamlit run app.py
   ```

3. **Abrir el navegador web** y acceder a la URL proporcionada por Streamlit, típicamente:
   ```
   http://localhost:8501
   ```

## Estructura del Proyecto
- `app.py`: Script principal que ejecuta la aplicación web.
- `vehicles_us.csv`: Conjunto de datos de vehículos usados.
- `notebooks/EDA.ipynb`: Notebook de Jupyter para el análisis exploratorio de datos.
- `requirements.txt`: Archivo de requisitos para instalar las dependencias necesarias.
- `.streamlit/config.toml`: Archivo de configuración para Streamlit.
- `README.md`: Este archivo, con la descripción y guía del proyecto.

## Análisis Exploratorio de Datos
El análisis exploratorio de datos (EDA) se realiza en el notebook `notebooks/EDA.ipynb`. Este análisis incluye:

- **Carga y descripción de datos**: Información básica y estadística descriptiva.
- **Limpieza de datos**: Manejo de valores nulos y eliminación de duplicados.
- **Análisis univariado**: Distribución del odómetro y precios.
- **Análisis bivariado**: Relación entre el odómetro y el precio, y entre el año y el precio.

## Despliegue en la Nube
La aplicación web puede ser desplegada en Render o cualquier otro servicio de alojamiento compatible con Streamlit.

1. **Configurar el comando de construcción en Render**:
   ```bash
   pip install --upgrade pip && pip install -r requirements.txt
   ```

2. **Configurar el comando de inicio**:
   ```bash
   streamlit run app.py
   ```

3. **Acceder a la URL proporcionada por Render** para interactuar con la aplicación.

## Contribuciones
Las contribuciones son bienvenidas. Por favor, crea un "issue" para discutir cualquier cambio importante antes de enviar un "pull request".

## Licencia
Este proyecto está bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.

## Contacto
Rubintel Ulloa Francisco - [rubintel7@gmail.com](mailto:rubintel7@gmail.com)

GitHub: [https://github.com/RubintelUlloaFrancisco](https://github.com/RubintelUlloaFrancisco)
