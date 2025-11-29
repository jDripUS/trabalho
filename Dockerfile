
FROM python:3.11-slim

WORKDIR /app

RUN pip install pdm

COPY pyproject.toml .pdm-python ./

RUN pdm install --prod --no-lock

COPY src/ ./src/
COPY data/ ./data/

ENV PYTHONPATH=/app/src
ENV PYTHONUNBUFFERED=1

CMD ["pdm", "run", "python", "-m", "csv_analyzer.analyzer", "--help"]
