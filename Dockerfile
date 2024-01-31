FROM python:3.11

ENV PYTHONUNBUFFERED 1
ENV XDG_RUNTIME_DIR /tmp_pdf
# RUN mkdir -p /tmp && chmod 1777 /tmp

WORKDIR /opt/oracle
RUN sed -i 's@http@https@g' /etc/apt/sources.list.d/debian.sources
RUN apt update && apt install -y --no-install-recommends wkhtmltopdf

WORKDIR /api
RUN python -m venv venv
RUN . ./venv/bin/activate
COPY requirements.txt .
RUN pip install -r ./requirements.txt

COPY main.py .


EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]