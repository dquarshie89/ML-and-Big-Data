
FROM python:3.6

WORKDIR /usr/src/app

RUN mkdir .kaggle
RUN cp kaggle.json ./.kaggle
COPY requirements.txt .
COPY titanic_predictions.py .

RUN pip install -r requirements.txt

#pip install -r requirements.txt

EXPOSE 500
CMD ["python", "titanic_predictions.py"]
