### API Restful with Flask

- At first, I have to say this project is inspired in a web course (that I did) present on Udemy, if you wanna know which one is, just click [here](https://github.com/schoolofcode-me/rest-api-sections/tree/master/section11).
- This project (only) does relational databases such as Sqlite, Mysql, and Postgress.
- A skeleton API with MongoDB is coming soon... **Be patient =)**

### Virtualenv commands:

- For you start and load you virtual env, simply execute the following commands in your bash.
  ```bash
  virtualenv venv --python=python3.7
  source venv/bin/activate
  ```

### Dependencies

- Probably you start and load the virtual env, but you don't have any dependencies installed in your environment. For fix this you must install! see the line below.
  ```bash
  pip install flask flask-jwt flask.restful flask-sqlalchemy
  ```

### Play

- Now we just have to start the code, right? For that you'd think about the core of the application, is the file app.py, there have the start and firsts imports of our application.
  ```bash
  python app.py
  ```

### How the API works?

#### Routes ( Views )

- Your routes necessity be declared in 'app/views.py', each method inside the Resource represents an HTTP verb.
  ```python
  from resources.exemple import Exemple
  api.add_resource(Exemple, '/exemple/<int:id>')
  ```

#### Controllers ( Resources )

- Your controllers here are called `resources`, `app/resources`, but to be honest, call as you want... when you create a new resource remember to follow one example inside the folder.
  The parser is responsible to validate fields on a request. @jwt_required specify (explicitly) authentication to access the route. The class method get is your route for a GET HTTP.

  ```python
  class Item(Resource):
      parser = reqparse.RequestParser()
      parser.add_argument('price',
                          type=float,
                          required=True,
                          help="This field cannot be left blank!"
                          )
      parser.add_argument('store_id',
                          type=int,
                          required=True,
                          help="Every item needs a store_id."
                          )

      @jwt_required
      def get(self, name):
          item = ItemModel.find_by_name(name)
          if item:
              return item.json()
          return {'message': 'Item not found'}, 404
  ```

#### Models

- Your models use SQL Alchemy to save, read, edit and delete. For describe your data structure in your database, you can use the reserved propriety '\_\_tablename\_\_' to say your table name. The others proprieties to specify columns.

  ```python
  from database import db
    class ItemModel(db.Model):
        __tablename__ = 'items'

        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(80))
        price = db.Column(db.Float(precision=2))

        store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
        store = db.relationship('StoreModel')
  ```
