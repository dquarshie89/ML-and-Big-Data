
FROM python:3.6
RUN MKDIR -p .kaggle
COPY /.kaggle/kaggle.json .kaggle
#RUN mkdir -p ~/.kaggle
#ADD . ~/.kaggle

COPY . /app
#COPY /.kaggle .
WORKDIR ./app

#ADD . /app

RUN pip install -r requirements.txt

EXPOSE 80
CMD [ "python", "titanic_predictions.py" ]
