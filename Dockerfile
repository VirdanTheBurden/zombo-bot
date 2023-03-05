# temp: ghcr is being a bitch so we're gonna have to do it the
# old fashioned way ffs

ARG python_version=3.11-alpine

FROM python:$python_version

# POETRY_VIRTUALENVS_IN_PROJECT is required to ensure in-projects venvs mounted from the host in dev
# don't get prioritised by `poetry run`
ENV POETRY_VERSION=1.3.1 \
  POETRY_HOME="/opt/poetry/home" \
  POETRY_CACHE_DIR="/opt/poetry/cache" \
  POETRY_NO_INTERACTION=1 \
  POETRY_VIRTUALENVS_IN_PROJECT=false

ENV PATH="$POETRY_HOME/bin:$PATH"

RUN apk -U upgrade \
  && apk --no-cache add curl gcc musl-dev python3-dev libffi-dev openssl-dev cargo pkgconfig

RUN curl -sSL https://install.python-poetry.org | python

# Install deps
WORKDIR /bot
COPY pyproject.toml poetry.lock /bot/
RUN poetry install

ENTRYPOINT ["poetry"]
CMD ["run", "python", "-m", "bot"]