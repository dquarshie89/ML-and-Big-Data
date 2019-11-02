
FROM python:3.6

COPY . /app
COPY kaggle.json  .

WORKDIR ./app
#RUN mkdir -p ~/.kaggle
#ADD . ~/.kaggle
#ADD . /app

RUN pip install -r requirements.txt


EXPOSE 80
CMD [ "python", "titanic_predictions.py" ]
