import streamlit as st
from views import View

class LoginUI:
    def main():
        st.header("Entrar")
        email = st.text_input("Informe o e-mail")
        senha = st.text_input("Informe a senha", type="password")
        if st.button("Entrar"):
            c = View.cliente_autenticar(email, senha)
            # a = View.administrador_autenticar(email, senha)
            if c == None: st.write("E-mail ou senha inválidos")
            else:
                st.session_state.usuario_id = c.get_id()
                st.session_state.screen = "course"
                st.rerun()