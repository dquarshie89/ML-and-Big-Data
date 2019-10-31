FROM python:3.6
WORKDIR /app

COPY requirements.txt ./

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
#RUN git clone https://github.com/dquarshie89/Data-602 /usr/src/app/Data-602
EXPOSE 5000
# Run app.py when the container launches
CMD ["python", "titanic predictions.py"]

