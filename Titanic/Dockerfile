
FROM python:3.6

RUN mkdir -p ~/.kaggle
ADD . ~/.kaggle

COPY kaggle.json ./.kaggle/kaggle.json

COPY . /
WORKDIR ./
#COPY kaggle.json /.kaggle
#ADD . /app

RUN pip install -r requirements.txt

EXPOSE 80
CMD [ "python", "titanic_predictions.py" ]
