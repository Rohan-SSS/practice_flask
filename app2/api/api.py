from flask import Flask, json, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///example.db"
# creating a db model

db = SQLAlchemy(app)
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)

    def __str__(self):
        return f'{self.id} {self.content}'

def todo_serializer(todo):
    return {
        'id':todo.id,
        'content':todo.content
    }

@app.route('/api', methods=['GET'])
def index():
    # important * is used to unpack the maped data

    return jsonify([*map(todo_serializer, Todo.query.all())])

@app.route('/api/create', methods=['POST'])
def create():
    request_data = json.loads(request.data)
    todo = Todo(content=request_data['content'])

    db.session.add(todo)
    db.session.commit()

    return {'201':'noice'}

if __name__ =='__main__':
    app.run(debug=True)

