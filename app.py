from flask import Flask
import flask
from flask.ext.restless import APIManager
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import Column,Integer,Text,Float
from sqlalchemy.dialects.postgresql import JSON
import logging
import googleapiclient.client
import httplib2
logging.getLogger("sqlalchemy").setLevel("WARNING")
logging.getLogger("flask.ext.restless").setLevel("WARNING")

app = Flask(__name__,static_url_path='')
app.config['SQLALCHEMY_DATABASE_URI']= 'mysql://{user}:{password}@{hostname}/demo'.format(user="root",
   password="foomanchoo123!",hostname="mysql")
app.logger.setLevel("WARNING")
db=SQLAlchemy(app)

class Product(db.Model):
    id = Column(Integer,primary_key=True,unique=True)
    sku = Column(Text,unique=False)
    name= Column(Text,unique=False)
    type= Column (Text, unique=False)
    price= Column (Float, unique=False)
    upc= Column (Text,unique=False)
    shipping= Column (Float, unique=False)
    description= Column(Text,unique=False)
    manufacturer= Column (Text, unique=False)
    model = Column (Text, unique=False)
    url = Column (Text, unique=False)
    image = Column (Text, unique=False)




db.create_all()
api_manager=APIManager(app,flask_sqlalchemy_db=db)
api_manager.create_api(Product,methods=['GET','POST','DELETE','PUT'])
@app.route('/')
def index():
    return app.send_static_file("index.html")
@app.route('/static/templates/<path:path>')
def serve_partial(path):
    return flask.render_template('/templates/{}'.format(path))
app.debug=True

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=False)
