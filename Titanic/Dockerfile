
FROM python:3.6

WORKDIR /
#COPY kaggle.json /.kaggle
ADD kaggle.json /app/.kaggle
#ADD . /app

RUN pip install -r requirements.txt

EXPOSE 80
CMD [ "python", "titanic_predictions.py" ]
