# Aplicación de registro de mascotas

Pequeña app FastAPI para capturar nombre, peso, edad y nombre del dueño de una mascota, usando SQLite.

Instalación:
1. Crear entorno virtual (recomendado):
   python -m venv .venv && source .venv/bin/activate
2. Instalar dependencias:
   pip install -r requirements.txt

Ejecutar:
uvicorn main:app --reload --host 127.0.0.1 --port 8000

Acceder en: http://127.0.0.1:8000

Base de datos: sqlite:///./app.db (connect_args={'check_same_thread': False})