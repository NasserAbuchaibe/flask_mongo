from flask import Flask, request
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['MONGO_URI']='mongodb://localhost/pythonmongodb'

mongo = PyMongo(app)

@app.route('/users', methods=['POST'])
def create_user():
    username = request.json['username']
    email = request.json['email']
    password = request.json['password']

    if username and email and password:
        hashed_password = generate_password_hash(password)
        id = mongo.db.users.insert(
            {'username': username, 'email': email, 'password': hashed_password}
        )
        response = {
            'id': str(id),
            'username': username,
            'passwors': hashed_password,
            'email': email
        }
        return response
    else:
        pass
    
if __name__ == "__main__":
    app.run(debug=True)
