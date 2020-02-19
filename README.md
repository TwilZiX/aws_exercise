# aws_exercise

Webapp based on Flask / MongoDB

### Building and running

Go to directory with this app and build + run with command

```
bash run.sh
```

### Running the tests

Port: 5000 (default Flask port)

#### /random (GET)

On this page you can see JSON data (status and random number from 0 to 100)

#### /echo (POST)

There you can post a massage using JSON, which will be added to database. Your data should look like this:

```
{
  "msg": Your message
}
```

#### /list (GET)

Prints all statuses added to the database along with the time it happened

### Warning

At the start database is empty, you have to put something there with /echo to see the content
