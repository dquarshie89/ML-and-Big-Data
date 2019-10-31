FROM python:3.6
WORKDIR /app

COPY requirements.txt ./

# Install any necessary dependencies
RUN pip install -r requirements.txt
#RUN pip install --no-cache-dir -r requirements.txt
#RUN git clone https://github.com/dquarshie89/Data-602 /usr/src/app/Data-602
EXPOSE 80
# Run titanic_predictions.py when the container launches
CMD ["python", "titanic_predictions.py"]

