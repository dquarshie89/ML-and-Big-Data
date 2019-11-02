
FROM python:3.6

COPY . /app
ADD kaggle.json.
#RUN mkdir -p ~/.kaggle
#ADD . ~/.kaggle




#ADD . /app

RUN pip install -r requirements.txt

WORKDIR ./app

EXPOSE 80
CMD [ "python", "titanic_predictions.py" ]
