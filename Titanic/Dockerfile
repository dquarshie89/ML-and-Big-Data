
FROM python:3.6
WORKDIR /app
ADD . /app
#COPY requirements.txt ./
# Install any necessary dependencies
RUN mkdir .kaggle
RUN mv "kaggle.json" ".kaggle"

RUN pip install -r requirements.txt

EXPOSE 80
CMD [ "python", "titanic_predictions.py" ]
