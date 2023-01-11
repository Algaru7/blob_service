FROM debian
RUN apt-get update && \
    apt-get install -y \
        nano \
        less \
        curl \
        sudo \
        python3 \
        python3-pip \
        tox \
        && \
    apt-get clean