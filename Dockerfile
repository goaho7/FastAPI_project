FROM python:3.12

WORKDIR /app

COPY . .

RUN pip install poetry
RUN poetry install --no-dev --no-root


# CMD ["poetry", "run", "uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
