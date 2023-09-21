from flask_restful import Resource, reqparse
from models.hotel import HotelModel

class Hoteis(Resource):
    def get(self):
        return {'hoteis':[hotel.json() for hotel in HotelModel.query.all()]}

class Hotel(Resource):
    argumentos = reqparse.RequestParser()
    ## somente o que será aceito no post
    ## sempre que enviar um json os itens que estar com aspas duplas ""
    argumentos.add_argument('nome', type=str, required=True, help="esse campo não pode ser deixado em branco")
    argumentos.add_argument('estrelas', type=float, required=True, help="esse campo não pode ser deixado em branco")
    argumentos.add_argument('diaria', type=float, required=True, help="esse campo não pode ser deixado em branco")
    argumentos.add_argument('cidade', type=str, required=True, help="esse campo não pode ser deixado em branco")


    def get(self, hotel_id):
        hotel = HotelModel.find_hotel(hotel_id)
        if hotel:
            return hotel.json()
        else:
            return {"erro": "hotel_id não encontrado"}, 404 # not found


    def post(self, hotel_id):
        if HotelModel.find_hotel(hotel_id):
            return {"message": f"Hotel id {hotel_id} já existe"}, 400
        dados = Hotel.argumentos.parse_args()

        ## metodo com modelo
        hotel = HotelModel(hotel_id, **dados)
        try:
            hotel.save_hotel()
        except:
            return {"message":"erro interno 500"}, 500
        return hotel.json(), 200


    def put(self, hotel_id):

        dados = Hotel.argumentos.parse_args()

        ## metodo com modelo
        hotel_encontrado = HotelModel.find_hotel(hotel_id)
        if hotel_encontrado:
            hotel_encontrado.update_hotel(**dados)
            hotel_encontrado.save_hotel()
            return hotel_encontrado.json(), 200 # codigo de tudo certo
        else:
            hotel = HotelModel(hotel_id, **dados)
            try:
                hotel.save_hotel()
            except:
                return {"message": "erro interno 500 ao atualizar"}, 500
            return hotel.json(), 201 # codigo de criado

    def delete(self, hotel_id):
        hotel = HotelModel.find_hotel(hotel_id)
        if hotel:
            try:
                hotel.save_hotel()
            except:
                return {"message": "erro interno 500 ao deletar"}, 500
            return {"message":"Hotel deletado"}
        else:
            return {"message":"Hotel não encontrado, erro ao apagar"}, 404