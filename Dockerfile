
FROM python:3.6

WORKDIR /usr/src/app

COPY kaggle.json .
RUN pip install -r requirements.txt
COPY requirements.txt .
COPY titanic_predictions.py .


EXPOSE 500
CMD ["python", "titanic_predictions.py"]
