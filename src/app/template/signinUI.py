import streamlit as st
from views import View

class SigninUI:
    @staticmethod
    def fill(session_name, default=""):
        if session_name not in st.session_state:
            return default
        return st.session_state[session_name]
    
    @classmethod
    def main(cls):
        if "sign_step" not in st.session_state:
            st.session_state.sign_step = 0

        
        if st.session_state.sign_step == 0:
            st.header("Criar conta")
            email = st.text_input("Informe o e-mail", cls.fill("email"))
            senha = st.text_input("Informe a senha", value=cls.fill("senha"), type="password")
            if st.button("Continuar"):
                st.session_state.email = email
                st.session_state.senha = senha
                st.session_state.sign_step = 1
                st.rerun()

        elif st.session_state.sign_step == 1:
            st.header("Diga um pouco mais sobre você...")

            nome = st.text_input("Informe o nome", value=cls.fill("nome"))
            matematica = st.checkbox("Quero estudar matemática", value=cls.fill("matematica", False))
            portugues = st.checkbox("Quero estudar português", value=cls.fill("portugues", False))
            col1, col2 = st.columns(2)
            with col1:
                if st.button("Voltar"):
                    st.session_state.sign_step = 0
                    st.rerun()
                    
            with col2:
                if st.button("Continuar"):
                    if not matematica and not portugues:
                        st.warning("Escolha pelo menos um curso")
                    else:
                        st.session_state.nome = nome
                        st.session_state.matematica = matematica
                        st.session_state.portugues = portugues
                        st.session_state.sign_step = 2
                        st.rerun()
            
        elif st.session_state.sign_step == 2:
            st.header(f"Certo {st.session_state.nome}! Agora... uma última pergunta")
            beta = st.checkbox("Gostaria de ingressar como um testador beta? (você sempre poderá mudar depois...)", value=cls.fill("beta", False))
            col1, col2 = st.columns(2)
            with col1:
                if st.button("Voltar"):
                    st.session_state.sign_step = 1
                    st.rerun()
                    
            with col2:
                if st.button("Criar conta"):
                    st.session_state.beta = beta
                    data = [
                        st.session_state.nome,
                        st.session_state.email,
                        st.session_state.senha,
                        st.session_state.matematica,
                        st.session_state.portugues,
                        st.session_state.beta,
                    ]
                    user_id = View.inserir_usuario(*data)
                    if user_id == None:
                        st.warning("Não foi possível criar a conta.")
                    else:
                        st.session_state.usuario_id = user_id
                        st.session_state.perfil_id = user_id
                        st.session_state.tutorial = True
                        st.session_state.screen = "perfil"
                        st.rerun()