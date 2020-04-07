FROM python:3

LABEL maintainer Kaj Oskar Rusilowski

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8001

COPY . .

ENTRYPOINT [ "python" ]
CMD [ "shortener.py" ]