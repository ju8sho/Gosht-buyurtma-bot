# Python 3.12 rasmiy tasviridan foydalanish
FROM python:3.12-slim

# Zarur bo'lgan tizim paketlarini o'rnatish
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Poetry o'rnatish va PATH-ga qo'shish
ENV POETRY_HOME=/opt/poetry
RUN curl -sSL https://install.python-poetry.org | python3 - && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

# Ish katalogini o'rnatish
WORKDIR /app

# pyproject.toml va poetry.lock fayllarini nusxalash
COPY pyproject.toml poetry.lock* ./

# Loyiha bog'liqliklarini o'rnatish
RUN poetry install --no-root --no-dev

# Loyiha fayllarini nusxalash
COPY . .

# Dasturni ishga tushirish
CMD ["python", "main.py"]