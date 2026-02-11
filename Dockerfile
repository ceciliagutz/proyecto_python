FROM python:3.12-slim
WORKDIR /app

# Dependencias del sistema
RUN apt-get update && apt-get install -y build-essential libffi-dev libssl-dev curl && rm -rf /var/lib/apt/lists/*

# Copiar archivos de proyecto
COPY pyproject.toml poetry.lock ./

# Instalar Poetry y dependencias *sin flags raros*
RUN pip install --no-cache-dir poetry && poetry install

# Copiar la app
COPY advance_level/laboratory16/app ./app

EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
