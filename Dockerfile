FROM python:3.7

RUN apt-get update -y && apt-get install libgl1-mesa-glx -y



COPY . /app
WORKDIR /app
RUN python3 setup.py install --user