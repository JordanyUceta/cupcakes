"""Flask app for Cupcakes"""
from flask import Flask, request, render_template, redirect, session, jsonify
from models import db, connect_db, Cupcake

app = Flask(__name__)
app.app_context().push() 
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
app.config['SQLALCHEMY_ECHO'] = True 
app.config['SECRET_KEY'] = 'cup123'

connect_db(app) 

@app.route('/')
def main(): 

    return render_template("index.html")

@app.route('/api/cupcakes', methods=['GET'])
def all_cupcakes(): 
    cupcakes = [cupcake.serialize() for cupcake in Cupcake.query.all()]
    return jsonify(cupcakes=cupcakes)

@app.route('/api/cupcakes/<int:id>', methods=['GET'])
def get_cupcake(id): 
    cupcake = Cupcake.query.get_or_404(id) 
    return jsonify(cupcake=cupcake.serialize())

@app.route('/api/cupcakes', methods=['POST'])
def add_cupcake(): 
    new_cupcake = Cupcake(
        flavor=request.json['flavor'], 
        size=request.json['size'], 
        rating=request.json['rating'], 
        image=request.json['image'] or None)

    db.session.add(new_cupcake) 
    db.session.commit()
    return (jsonify(cupcake=new_cupcake.serialize()), 201)

@app.route('/api/cupcakes/<int:id>')
def update_cupcake(id): 
    cupcake = Cupcake.query.get_or_404(id) 
    cupcake.flavor = request.json('flavor', cupcake.flavor)
    cupcake.size = request.json('size', cupcake.size)
    cupcake.rating = request.json('rating', cupcake.rating)
    cupcake.image = request.json('image', cupcake.image)
    db.session.commit() 
    return jsonify(cupcake = cupcake.serialize())

@app.route('/api/cupcakes/<int:id>')
def delete_cupcake(id): 
    cupcake = Cupcake.query.get_or_404(id) 
    db.session.delete(cupcake)
    de.session.commit()
    return jsonify(message='deleted')
