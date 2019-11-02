
FROM python:3.6

WORKDIR /usr/src/app
COPY kaggle.json .
#WORKDIR /app
#ADD . /app

#ADD kaggle.json /.kaggle/kaggle.json
#RUN chmod +x /.kaggle/kaggle.json


#RUN mkdir -p ~/.kaggle
#ADD . ~/.kaggle
#ADD . /app

RUN pip install -r requirements.txt


EXPOSE 80
CMD [ "python", "titanic_predictions.py" ]
