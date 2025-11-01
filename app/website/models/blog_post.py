from website.connection import db


class BlogPost(db.Model):
    __tablename__ = 'blog'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)  # optional: add a title
    body = db.Column(db.Text(), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now(), nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'body': self.body,
            'created_at': self.created_at.isoformat()
        }
