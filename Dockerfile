
FROM python:3.6


COPY .kaggle/kaggle.json ./.kaggle
COPY requirements.txt .
COPY titanic_predictions.py .

WORKDIR /usr/src/app

RUN pip install -r requirements.txt
#pip install -r requirements.txt

EXPOSE 500
CMD ["python", "titanic_predictions.py"]
