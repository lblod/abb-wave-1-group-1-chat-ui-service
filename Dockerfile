FROM python:3.12-slim

ENV GRADIO_SERVER_NAME="0.0.0.0"

COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

WORKDIR /usr/src/app
COPY src/ src/

CMD ["python", "-m", "src.main"]