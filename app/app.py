import random
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"

db = SQLAlchemy(app)


class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(10), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return self.id


@app.route("/echo", methods=["POST"])
def show_message():
    data = request.get_json()
    if "msg" in data and len(data) == 1:
        msg = data["msg"]
        new_data = Data(status="ok")
        try:
            db.session.add(new_data)
            db.session.commit()
            return jsonify(status="ok", msg=msg)
        except:
            return "Something went wrong with database"
    else:
        new_data = Data(status="error")
        try:
            db.session.add(new_data)
            db.session.commit()
            return jsonify(status="error")
        except:
            return "Something went wrong with database"


@app.route("/random", methods=["GET"])
def random_number():
    number = random.randint(0, 100)
    return jsonify(status="ok", number=number)


@app.route("/list", methods=["GET"])
def show_table():
    my_data = Data.query.order_by(Data.date).all()
    return render_template("table.html", data=my_data)


if __name__ == "__main__":
    app.run("0.0.0.0", port=80, debug=True)
