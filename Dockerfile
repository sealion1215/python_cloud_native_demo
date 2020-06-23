FROM python:3.7-alpine
WORKDIR /code
ADD my_script.py /code
COPY requirements.txt requirements.txt
RUN apt install tesseract-ocr
RUN apt install libmysqlclient-dev
RUN apt install python-dev
RUN pip install -r requirements.txt

ENV ddl=NONE
ENV docker_build=true
ENV port_number=8080
CMD ["python", "/code/my_script.py"]