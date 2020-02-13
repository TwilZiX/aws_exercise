# this is an official Python runtime, used as the parent image
FROM python:3.6

# set the working directory in the container to /app
WORKDIR /app

# add the current directory to the container as /app
ADD . /app

# execute pip command, pip install -r
RUN pip install -r requirements.txt

# execute the Flask app
CMD ["python", "app.py"]