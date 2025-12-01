import streamlit as st
from views import View
from PIL import Image
from pathlib import Path

class ScreenNotFoundUI:
    CWD = Path.cwd()
    @staticmethod
    def fill(session_name, default=""):
        if session_name not in st.session_state:
            return default
        return st.session_state[session_name]
    
    @classmethod
    def main(cls):
        st.header("Tela não encontrada... :(")
        if st.button("Voltar para o meu perfil"):
            st.session_state.screen = "perfil"
            st.rerun()