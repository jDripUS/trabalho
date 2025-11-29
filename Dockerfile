FROM python:3.11-slim

WORKDIR /app

# Instala o PDM
RUN pip install pdm

# Copia arquivos de configuração
COPY pyproject.toml ./

# Instala dependências
RUN pdm install --prod --no-lock

# Copia código fonte
COPY src/ ./src/
COPY data/ ./data/

# Comando padrão
CMD ["pdm", "run", "python", "-m", "csv_analyzer"]
