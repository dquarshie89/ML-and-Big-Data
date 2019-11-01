
FROM python:3.6

#RUN mkdir -p ~/.kaggle
#ADD . ~/.kaggle

#COPY kaggle.json ./.kaggle/kaggle.json

COPY . /app
WORKDIR ./app

#ADD . /app

RUN pip install -r requirements.txt
ADD kaggle.json /.kaggle
EXPOSE 80
CMD [ "python", "titanic_predictions.py" ]
