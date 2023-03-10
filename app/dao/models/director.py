from app.setup_db import db
from marshmallow import Schema, fields


class Director(db.Model):
    __tablename__ = 'director'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)


class DirectorSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()
