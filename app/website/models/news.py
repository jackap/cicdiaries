from website.connection import db


class News(db.Model):
    __tablename__ = 'news'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), primary_key=False)
    name = db.Column(db.String(), nullable=False)
    html_url = db.Column(db.String(), nullable=False)
    image_url = db.Column(db.String(), nullable=True)
    date = db.Column(db.String(), nullable=False)
    argument = db.Column(db.String(), nullable=False)

    def serialize(self):
        return {
            'description': self.description,
            'name': self.name,
            'html_url': self.html_url,
            'image_url': self.image_url,
            'date': self.date,
            'argument': self.argument
        }
