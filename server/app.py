from flask import Flask, make_response
from flask_migrate import Migrate
from models import db, Zookeeper, Enclosure, Animal

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)


@app.route('/')
def home():
    return '<h1>Zoo app</h1>'


@app.route('/animal/<int:id>')
def animal_by_id(id):
    animal = Animal.query.get(id)
    if animal is not None:
        response = f'<h2>Animal {id}</h2>'
        response += f'<ul><li>Name: {animal.name}</li>'
        response += f'<li>Species: {animal.species}</li>'
        response += f'<li>Zookeeper: {animal.zookeeper.name}</li>'
        response += f'<li>Enclosure: {animal.enclosure.id}</li></ul>'
        return response
    else:
        return '<p>Animal not found</p>', 404


@app.route('/zookeeper/<int:id>')
def zookeeper_by_id(id):
    zookeeper = Zookeeper.query.get(id)
    if zookeeper is not None:
        response = f'<h2>Zookeeper {id}</h2>'
        response += f'<ul><li>Name: {zookeeper.name}</li>'
        response += f'<li>Birthday: {zookeeper.birthday}</li>'
        response += '<li>Animals:</li><ul>'
        for animal in zookeeper.animals:
            response += f'<li>{animal.name} - {animal.species}</li>'
        response += '</ul></ul>'
        return response
    else:
        return '<p>Zookeeper not found</p>', 404


@app.route('/enclosure/<int:id>')
def enclosure_by_id(id):
    enclosure = Enclosure.query.get(id)
    if enclosure is not None:
        response = f'<h2>Enclosure {id}</h2>'
        response += f'<ul><li>Environment: {enclosure.environment}</li>'
        response += f'<li>Open to Visitors: {enclosure.open_to_visitors}</li>'
        response += '<li>Animals:</li><ul>'
        for animal in enclosure.animals:
            response += f'<li>{animal.name} - {animal.species}</li>'
        response += '</ul></ul>'
        return response
    else:
        return '<p>Enclosure not found</p>', 404


if __name__ == '__main__':
    app.run(port=5555, debug=True)
