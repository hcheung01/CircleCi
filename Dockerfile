FROM ubuntu as build

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

ENV VIRTUAL_ENV=/tmp/testEnv
RUN python3 -m pip install virtualenv && \
    python3 -m virtualenv ${VIRTUAL_ENV}
ENV PATH="${VIRTUAL_ENV}/bin:$PATH"

COPY requirements.txt /tmp/
RUN pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt

COPY src/ /tmp/src/
COPY test/ /tmp/test/

WORKDIR /tmp/test
CMD ["python", "-m", "pytest", "math.py"]
