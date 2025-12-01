import streamlit as st
from views import View
from PIL import Image
from pathlib import Path

class PerfilUI:
    CWD = Path.cwd()
    @staticmethod
    def fill(session_name, default=""):
        if session_name not in st.session_state:
            return default
        return st.session_state[session_name]
    
    @classmethod
    def main(cls):
        cls.usuario = View.usuario_listar_id(st.session_state.usuario_id)
        opcoes = ["Perfil"]
        if "tutorial" in st.session_state:
            st.header("Escolha um dos seus cursos na esquerda!")
        else:
            opcoes.extend(["Editar Perfil", "Excluir Perfil"])
        if cls.usuario.get_mat():
            opcoes.append("Matemática")
        if cls.usuario.get_pt():
            opcoes.append("Português")

        tabs = st.tabs(opcoes)
        for tab_name, tab in zip(opcoes, tabs):
            with tab:
                if tab_name == "Perfil":
                    PerfilUI.perfil()
                elif tab_name == "Matemática":
                    PerfilUI.mat()
                elif tab_name == "Português":
                    PerfilUI.pt()
                elif tab_name == "Editar Perfil":
                    PerfilUI.editar()
                elif tab_name == "Excluir Perfil":
                    PerfilUI.excluir()
                
    @classmethod
    def perfil(cls):
        st.text(cls.usuario.get_nome())
        img = Image.open(cls.CWD / "src" / "app" / "images" / "no_profile.png")
        st.image(img, caption="Foto de perfil", width=100)

    @classmethod
    def mat(cls):
        if st.button("Ir para o curso de matemática"):
            st.session_state.course = "mat"
            st.session_state.screen = "course"
            st.rerun()
        
    @classmethod
    def pt(cls):
        if st.button("Ir para o curso de português"):
            st.session_state.course = "pt"
            st.session_state.screen = "course"
            st.rerun()
        
    @classmethod
    def editar(cls):
        st.text(cls.usuario.get_nome())
        img = Image.open(cls.CWD / "src" / "app" / "images" / "no_profile.png")
        st.image(img, caption="Foto de perfil", width=100)
        
    @classmethod
    def excluir(cls):
        st.text(cls.usuario.get_nome())
        img = Image.open(cls.CWD / "src" / "app" / "images" / "no_profile.png")
        st.image(img, caption="Foto de perfil", width=100)