
FROM python:3.6

WORKDIR /usr/src/app
COPY kaggle.json ./.kaggle
COPY requirements.txt .
COPY titanic_predictions.py .

RUN pip install -r requirements.txt


EXPOSE 80
CMD [ "python", "titanic_predictions.py" ]
