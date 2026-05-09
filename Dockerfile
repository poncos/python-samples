from python:3.9.19-bookworm

RUN groupadd --system ecollado --gid 444 && \
useradd --uid 444 --system --gid ecollado --home-dir /home/ecollado --create-home --shell /sbin/nologin --comment "Docker image user" ecollado

WORKDIR /home/ecollado

COPY ./requirements.txt ./requirements.txt
COPY ./sample_python_rest ./sample_python_rest
COPY ./config ./config
COPY ./resources ./resources

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

RUN apt update && \
    apt install -y python3.11-venv && \
    python3.11 -m venv /home/ecollado/venv && \
    /home/ecollado/venv/bin/pip3 install -r requirements.txt && \
    rm -rf /var/lib/apt/lists/*

EXPOSE 8081

# USER ecollado

CMD ["/home/ecollado/venv/bin/uvicorn", "sample_python_rest.main:app", "--host", "0.0.0.0", "--port", "8081"]