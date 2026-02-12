# Dockerfile de un solo stage
FROM python:3.12-slim
WORKDIR /app

# Dependencias del sistema
RUN apt-get update && apt-get install -y build-essential libffi-dev libssl-dev curl && rm -rf /var/lib/apt/lists/*

# Copiar pyproject.toml y poetry.lock
COPY pyproject.toml poetry.lock ./

# Instalar Poetry y dependencias directamente en este contenedor
RUN pip install --no-cache-dir poetry \
    && poetry config virtualenvs.create false \
    && poetry install --no-root --no-interaction --no-ansi

# Asegurar que uvicorn esté disponible en el PATH
RUN pip install --no-cache-dir uvicorn[standard]

# Copiar la app
COPY advance_level/laboratory16/app ./app

# Exponer puerto
EXPOSE 8000

# CMD para correr uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
