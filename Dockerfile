
FROM python:3.6

WORKDIR /usr/src/app
COPY kaggle.json .
COPY requirements.txt .

RUN pip install -r requirements.txt


EXPOSE 80
CMD [ "python", "titanic_predictions.py" ]
