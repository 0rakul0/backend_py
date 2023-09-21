from flask_restful import Resource, reqparse
from models.usuario import UserModel

class Usuario(Resource):
    # /usuario/{user_id}
    def get(self, user_id):
        usuario = UserModel.find_usuario(user_id)
        if usuario:
            return usuario.json()
        else:
            return {"erro": "user_id não encontrado"}, 404 # not found

    def delete(self, user_id):
        usuario = UserModel.find_usuario(user_id)
        if usuario:
            try:
                usuario.save_hotel()
            except:
                return {"message": "erro interno 500 ao deletar"}, 500
            return {"message":"Ususario deletado"}
        else:
            return {"message":"Usuario não encontrado, erro ao apagar"}, 404
class UsuarioRegistro(Resource):
    # cadastro
    def post(self):
        atributos = reqparse.RequestParser()
        atributos.add_argument('login', type=str, required=True, help="o campo login deve ser preenchido")
        atributos.add_argument('senha', type=str, required=True, help="o campo senha deve ser preenchido")

        dados = atributos.parse_args()

        if UserModel.find_usuario(dados['login']):
            return {"message":f"o Login {dados['login']}, já existe."}

        usuario = UserModel(**dados)