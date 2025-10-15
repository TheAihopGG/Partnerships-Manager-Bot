FROM python:3.14.0-slim-bookworm
WORKDIR /pmbot
RUN pip install pip wheel poetry --upgrade
COPY ./poetry.lock ./poetry.lock
COPY ./pyproject.toml ./pyproject.toml
RUN poetry config virtualenvs.create false
RUN poetry install -n
COPY . .
RUN chmod +x ./prestart.sh
RUN chmod +x ./start.sh
ENTRYPOINT [ "./prestart.sh" ]
CMD [ "./start.sh" ]