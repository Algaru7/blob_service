FROM debian-base

RUN mkdir src
COPY src /src/
RUN pip install -r /src/requirements.txt

WORKDIR /src/

ENV ADMIN_TOKEN=admin
ENV PORT=3001
ENV ADDRESS=0.0.0.0
ENV DB_FILE=/src/persistence-auth/users.json

RUN mkdir -p $(dirname ${DB_FILE}) \
    && echo "{}" >> ${DB_FILE}

ENTRYPOINT python3 auth_server.py -a "${ADMIN_TOKEN}" -p "${PORT}" -l "${ADDRESS}" -d "${DB_FILE}"
