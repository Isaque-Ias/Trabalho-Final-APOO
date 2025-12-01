from models.dao import DAO
from models.user import Usuario, UsuarioDAO
import bcrypt

class View:
    @staticmethod
    def setup_db():
        DAO.setup_db()

    @staticmethod
    def cliente_autenticar(email, senha):
        data = UsuarioDAO.listar_email(email)
        if bcrypt.checkpw(senha.encode(), data[3]):
            return Usuario(*data)

    @staticmethod
    def inserir_usuario(nome, email, senha, matematica, portugues, beta):
        u = Usuario(0, nome, email, senha, matematica, portugues, beta)
        return UsuarioDAO.salvar(u)
    
    @staticmethod
    def usuario_listar_id(id):
        result = UsuarioDAO.listar_id(id)
        return Usuario(*result)