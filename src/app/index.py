import streamlit as st
from template.loginUI import LoginUI
from template.signinUI import SigninUI
from template.perfilUI import PerfilUI
from template.courseUI import CourseUI
from template.adminUI import AdminUI
from template.snfUI import ScreenNotFoundUI
from views import View

class IndexUI:
    def state():
        if "usuario_id" not in st.session_state or st.session_state.usuario_id == None:
            if "screen" not in st.session_state: st.session_state.screen = "login"
            
        IndexUI.screens()

    def screens():
        if "screen" in st.session_state:
            if st.session_state.screen == "perfil":
                PerfilUI.main()
            elif st.session_state.screen == "course":
                CourseUI.main()
            elif st.session_state.screen == "questao":
                CourseUI.question()
            elif st.session_state.screen == "login":
                LoginUI.main()
            elif st.session_state.screen == "signin":
                SigninUI.main()
            elif st.session_state.screen == "result":
                CourseUI.result()
            elif st.session_state.screen == "adm_hub":
                if "adm_id" in st.session_state:
                    if View.admin_listar_id(st.session_state.adm_id):
                        AdminUI.main()
                    else:
                        ScreenNotFoundUI.admin()
                else:
                    ScreenNotFoundUI.admin()

            else:
                ScreenNotFoundUI.main()
        else:
            PerfilUI.main()
            
    def main():
        View.setup_db()
        View.minimo_admin()
        IndexUI.state()

IndexUI.main()