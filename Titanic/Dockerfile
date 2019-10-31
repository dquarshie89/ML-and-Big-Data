FROM python:3.6
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --upgrade pip
EXPOSE 5000
CMD ["python", "titanic predictions.py"]

