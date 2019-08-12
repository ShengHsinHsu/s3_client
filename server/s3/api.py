from s3.models import S3
from flask import jsonify
from flask import session
from s3 import app, db
from flask import request
import boto3


@app.route('/')
@app.route('/index')
def hello():
    return "Hello World from Flask!"


@app.route("/s3/credential", methods=['GET', 'POST', 'DELETE'])
def credential():
    if request.method == 'POST':
        data = request.form
        print(request.data)
        obj = S3(**data)
        db.session.add(obj)
        db.session.commit()
        user = obj.query.filter_by(name=data.get('name')).first()
        return jsonify({"name:": user.name})


@app.route("/get")
def get_db():
    obj = S3(name="test")
    print(obj.query.filter_by(name='test').first())
    users = db.session.query(S3).all()
    print(users[0].name)
    return jsonify()
