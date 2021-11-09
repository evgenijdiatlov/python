#models.py
from auth import db
class Dessert(db.Model):
    # We always need an id
    id = db.Column(db.Integer, primary_key=True)
    # A dessert has a name, a price and some calories:
    name = db.Column(db.String(100))
    price = db.Column(db.Float)
    calories = db.Column(db.Integer)
    def __init__(self, name, price, calories):
        self.name = name
        self.price = price
        self.calories = calories


if __name__ == '__main__':
    print('Start creating db')
    db.create_all()
    print('Finish creating db')
    
