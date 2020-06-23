FROM ubuntu:18.04
WORKDIR /code
ADD . .
COPY requirements.txt requirements.txt
RUN apt-get update
RUN apt-get install tesseract-ocr -y
RUN apt-get install libmysqlclient-dev -y
RUN apt-get install python-dev -y
RUN apt-get install python3-pip -y
RUN pip3 install -r requirements.txt
RUN apt-get clean
RUN apt-get autoremove

ENV ddl=NONE
ENV docker_build=true
ENV port_number=8080
CMD ["python3", "/code/my_script.py"]