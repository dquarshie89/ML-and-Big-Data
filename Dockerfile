
FROM python:3.6

COPY . /
COPY kaggle.json ~/.kaggle
#RUN mkdir -p ~/.kaggle
#ADD . ~/.kaggle




#ADD . /app

RUN pip install -r requirements.txt

WORKDIR ./

EXPOSE 80
CMD [ "python", "titanic_predictions.py" ]
