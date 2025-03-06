from .database import db
class Location(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(),nullable=False)
    lat=db.Column(db.Integer,nullable=False)
    lon=db.Column(db.Integer,nullable=False)
    about=db.Column(db.String)
    role=db.Column(db.Integer,nullable=False)


