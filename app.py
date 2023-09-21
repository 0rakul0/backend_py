from flask import Flask
from flask_restful import Api
from resources.hotel import Hoteis, Hotel
from resources.usuario import Usuario
from sql_alchemy import banco

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

banco.init_app(app)  # Inicialize o banco de dados aqui

api = Api(app)
@app.before_request
def cria_banco():
    banco.create_all()

## get simples
api.add_resource(Hoteis, '/hoteis')

## get por id
api.add_resource(Hotel, '/hoteis/<string:hotel_id>')
api.add_resource(Usuario, '/usuario/<int:user_id>')

if __name__ == '__main__':
    app.run(debug=True)
