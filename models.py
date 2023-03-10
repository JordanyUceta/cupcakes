"""Models for Cupcake app."""
from flask_sqlalchemy import SQLAlchemy 

Default_img = 'https://tinyurl.com/demo-cupcake'

db = SQLAlchemy() 

def connect_db(app): 
    db.app = app 
    db.init_app(app) 

class Cupcake(db.Model): 

    __tablename__ = 'cupcakes'

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)

    flavor = db.Column(db.String(100), nullable = False)

    size = db.Column(db.String(50), nullable = False) 

    rating = db.Column(db.Float, nullable = False) 

    image = db.Column(db.Text, default = Default_img)

    def serialize(self): 
        return {
            'id': self.id, 
            'flavor' : self.flavor, 
            'size' : self.size, 
            'rating' : self.rating, 
            'image' : self.image
        }