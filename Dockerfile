FROM python:3.12-alpine

WORKDIR /app

COPY pyproject.toml pyproject.toml
RUN pip install uv

RUN uv sync

COPY project project
COPY entrypoint.sh entrypoint.sh

RUN chmod +x entrypoint.sh

CMD ["sh", "./entrypoint.sh"]
