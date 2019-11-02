
FROM python:3.6

#COPY . /app
#COPY kaggle.json  .
RUN mkdir .kaggle

WORKDIR .
ADD kaggle.json /.kaggle/kaggle.json
RUN chmod +x /.kaggle/kaggle.json


#RUN mkdir -p ~/.kaggle
#ADD . ~/.kaggle
#ADD . /app

RUN pip install -r requirements.txt


EXPOSE 80
CMD [ "python", "titanic_predictions.py" ]
