
FROM python:3.6

COPY . /
WORKDIR ./
#/usr/src/app
#COPY kaggle.json .
COPY requirements.txt ./
#COPY titanic_predictions.py .

RUN pip install -r requirements.txt

EXPOSE 500
CMD ["python", "titanic_predictions.py"]
