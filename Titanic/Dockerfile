
FROM python:3.6

COPY kaggle.json ~/.kaggle/kaggle.json

WORKDIR /app
ADD . /app

RUN pip install -r requirements.txt

EXPOSE 80
CMD [ "python", "titanic_predictions.py" ]
