#!/bin/bash
docker stop aws_exercise_frontend || true && docker rm aws_exercise_frontend || true
docker stop mongo || true && docker rm mongo || true
docker-compose up