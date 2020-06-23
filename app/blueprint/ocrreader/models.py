from app import db


class RecognitionResult(db.Model):
    __tablename__ = 'recognition_result'
    id = db.Column(
        db.BigInteger,
        primary_key=True
    )
    language = db.Column(db.String(20))
    result = db.Column(db.String(10))
    date = db.Column(db.DateTime)

    def __repr__(self):
        return '<recognition_result(id = \'%r\')>' % self.id
