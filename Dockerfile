# Change arm64 to amd64 if not running arm processor
FROM --platform=linux/arm64 ghcr.io/chrislovering/python-poetry-base:3.11-slim

# Install deps
WORKDIR /bot
COPY pyproject.toml poetry.lock ./
RUN poetry install --without dev

COPY . .

ENTRYPOINT ["poetry"]
CMD ["run", "python", "-m", "bot"]