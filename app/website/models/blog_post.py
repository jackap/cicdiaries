from website.connection import db


class BlogPost(db.Model):
    __tablename__ = 'blog'
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text(), nullable=False)
    news_id = db.Column(db.Integer, db.ForeignKey(
        'news.id'), nullable=False, index=True)
    news = db.relationship("News", foreign_keys=[news_id])

    def serialize(self):
        return {
            'news': self.news.serialize(),
            'body': self.body
        }
