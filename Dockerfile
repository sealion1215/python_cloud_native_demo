FROM ubuntu:18.04
WORKDIR /code
ADD . .
COPY requirements.txt requirements.txt
RUN apt-get update
RUN apt-get install -y curl python3.7 python3.7-dev python3.7-distutils
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.7 1
RUN update-alternatives --set python /usr/bin/python3.7
RUN apt-get install tesseract-ocr -y
RUN apt-get install libmysqlclient-dev -y
RUN apt-get install python-dev -y
RUN apt-get install python3-pip -y
RUN pip3 install -r requirements.txt
RUN apt-get clean
RUN apt-get autoremove

ENV db_host=localhost
ENV db_port=3306
ENV db_user=root
ENV db_password=1234567
ENV db_schema=python_cloud_native_demo
ENV ddl=CREATE
ENV docker_build=true


CMD ["python3", "/code/run.py"]