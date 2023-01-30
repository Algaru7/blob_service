FROM debian-base

RUN mkdir src
COPY src /src/
RUN pip install -r /src/requirements.txt

ENV AUTH_URI = http://172.17.0.3:3001
ENV PORT=3003
ENV ADDRESS=0.0.0.0
ENV STORAGE=directories.json
WORKDIR /src/
ENTRYPOINT python3 dir_server.py -p "${PORT}" -l "${ADDRESS}" -s "${STORAGE}" "${AUTH_URI}"
