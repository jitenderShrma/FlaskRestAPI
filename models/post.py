from db import db

class PostModel(db.Model):
    __tablename__="posts"
    id=db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(80))
    desc=db.Column(db.String(1000))
    def __init__(self, title, desc):
        self.title = title
        self.desc = desc
    
    def json(self):
        return {'title':self.title, 'desc':self.desc}

    @classmethod
    def find_by_title(cls, title):
        return cls.query.filter_by(title=title).first()
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_to_db(self, title):
        db.session.delete(self)
        db.session.commit()