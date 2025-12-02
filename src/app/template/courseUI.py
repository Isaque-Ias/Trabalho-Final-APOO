import streamlit as st
from views import View
from pathlib import Path
import streamlit.components.v1 as components

class CourseUI:
    CWD = Path.cwd()
    @staticmethod
    def fill(session_name, default=""):
        if session_name not in st.session_state:
            return default
        return st.session_state[session_name]
    
    @classmethod
    def main(cls):
        cls.usuario = View.usuario_listar_id(st.session_state.usuario_id)
        if not "course" in st.session_state:
            st.session_state.course = "pt"
            if cls.usuario.get_xp_mat() > cls.usuario.get_xp_pt():
                st.session_state.course = "mat"

        if st.button("voltar"):
            st.session_state.screen = "perfil"
            st.rerun()

        if st.session_state.course == "mat":
            cls.course(0)
        else:
            cls.course(1)
        
    @classmethod
    def course(cls, cat):
        questoes = View.questoes_listar_categoria(cat)
        html_questoes = ""
        for idx, questao in enumerate(questoes):
            message = f"{idx} - {questao.get_text()} - <button id='{idx}'>ir</button>"
            html_questoes += f"<li style='margin-left: 0;'>{message}</li>\n"

        d_val = "\{id, action:'open'\}"
        html = f"""
        <!DOCTYPE html>
        <html>
        <body>
            <ul style='list-style-type: none;'>
                {html_questoes}
            </ul>

            <script>
            console.log('c');
            Streamlit.setComponentValue({d_val});
            </script>
        </body>
        </html>
        """

        components.html(html, height=400)