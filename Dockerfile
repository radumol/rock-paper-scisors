FROM python:3.10


ADD rps.py .

ADD test_rps.py .

RUN pip install pytest


CMD ["python", "./rps.py"]