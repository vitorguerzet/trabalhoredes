FROM python:3

WORKDIR /usr/src/app

COPY requirements ./

COPY prog3.py ./

RUN pip install --no-cache-dir -r requirements

COPY . .

CMD [ "python" ,"./prog3.py"]

