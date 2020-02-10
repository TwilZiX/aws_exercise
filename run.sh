#!/bin/bash
app="flaskdock"
docker build -t ${app} .
docker run -p 5000:80 --volume $PWD/app:/app ${app}