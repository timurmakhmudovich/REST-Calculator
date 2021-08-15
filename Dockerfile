FROM python:3.6

WORKDIR /calcapp
COPY . /calcapp

RUN pip3 install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python3"]
CMD ["main.py"]
