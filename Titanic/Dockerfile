
FROM python:3.6

ADD kaggle.json ./.kaggle/kaggle.json
WORKDIR ./
#COPY kaggle.json /.kaggle
#ADD . /app

RUN pip install -r requirements.txt

EXPOSE 80
CMD [ "python", "titanic_predictions.py" ]
