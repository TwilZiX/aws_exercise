import random
from datetime import datetime
from pymongo import MongoClient
from flask import Flask, request, jsonify

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False

client = MongoClient("mongodb://datastore:27017/aws")
db = client["awsdb"]
table = db["statuses"]


@app.route("/")
def thanks():
    return "Thank you for testing my app :)"


@app.route("/echo", methods=["POST"])
def show_message():
    data = request.get_json()
    if "msg" in data and len(data) == 1:
        msg = data["msg"]
        try:
            post = {"status": "ok", "time": datetime.utcnow()}
            table.insert_one(post)
            return jsonify(status="ok", msg=msg)
        except:
            return "Something went wrong with database"
    else:
        try:
            post = {"status": "error", "time": datetime.utcnow()}
            table.insert_one(post)
            return jsonify(status="error")
        except:
            return "Something went wrong with database"


@app.route("/random", methods=["GET"])
def random_number():
    number = random.randint(0, 100)
    return jsonify(status="ok", number=number)


@app.route("/list", methods=["GET"])
def show_table():
    _my_data = table.find()
    my_data = [item for item in _my_data]
    result = []
    for item in my_data:
        result.append(
            {
                "status": str(item["status"]),
                "time": str(item["time"].strftime("%Y-%m-%d %H:%M:%S")),
            }
        )
    return jsonify(result)


if __name__ == "__main__":
    app.run("0.0.0.0", debug=True)
