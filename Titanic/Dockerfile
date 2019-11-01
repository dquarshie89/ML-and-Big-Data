
FROM python:3.6
#ADD . /app
WORKDIR ./app
COPY kaggle.json /.kaggle/kaggle.json 

# Install any necessary dependencies
#RUN mkdir .kaggle
#RUN cp "kaggle.json" ".kaggle"

RUN pip install -r requirements.txt

EXPOSE 80
CMD [ "python", "titanic_predictions.py" ]
