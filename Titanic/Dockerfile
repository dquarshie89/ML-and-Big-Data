
FROM python:3.6

COPY . /
WORKDIR ./
#COPY kaggle.json /.kaggle
#ADD . /app
ADD kaggle.json ./.kaggle/kaggle.json
RUN pip install -r requirements.txt

EXPOSE 80
CMD [ "python", "titanic_predictions.py" ]
