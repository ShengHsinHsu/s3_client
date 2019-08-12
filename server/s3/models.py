from s3 import db


class S3(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=True)
    name = db.Column(db.String(64), index=True, nullable=False)
    endpointurl = db.Column(db.String(120), index=True, unique=True, nullable=True)
    access_key_id = db.Column(db.String(128), unique=True, nullable=True)
    access_key = db.Column(db.String(128), unique=True, nullable=True)

    def __repr__(self):
        return '<User {}>'.format(self.name)


db.create_all()
