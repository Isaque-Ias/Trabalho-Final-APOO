import streamlit as st
from template.loginUI import LoginUI
from template.signinUI import SigninUI
from template.perfilUI import PerfilUI
from template.courseUI import CourseUI
from template.snfUI import ScreenNotFoundUI
from views import View

class IndexUI:
    def sidebar():
        if "usuario_id" not in st.session_state:
            IndexUI.menu_visitante()
        else:
            IndexUI.screens()

    def menu_visitante():
        op = st.sidebar.selectbox("Menu", ["Entrar", "Criar conta"])
        if op == "Entrar": LoginUI.main()
        if op == "Criar conta": SigninUI.main()

    def screens():
        if "screen" in st.session_state:
            if st.session_state.screen == "perfil":
                PerfilUI.main()
            elif st.session_state.screen == "course":
                CourseUI.main()
            else:
                ScreenNotFoundUI.main()
        else:
            PerfilUI.main()

    """
    def menu_cliente():
        op = st.sidebar.selectbox("Menu", ["Meus Dados", "Agendar Serviço"])
        if op == "Meus Dados": PerfilClienteUI.main()
        if op == "Agendar Serviço": AgendarServicoUI.main()

    def menu_profissional():
        op = st.sidebar.selectbox("Menu", ["Meus Dados", "Abrir Minha Agenda"])
        if op == "Meus Dados": PerfilProfissionalUI.main()
        if op == "Abrir Minha Agenda": AbrirAgendaUI.main()

    def menu_admin():
        op = st.sidebar.selectbox("Menu", ["Cadastro de Clientes", "Cadastro de Serviços", "Cadastro de Horários", "Cadastro de Profissionais", "Alterar Senha"])
        if op == "Cadastro de Clientes": ManterClienteUI.main()
        if op == "Cadastro de Serviços": ManterServicoUI.main()
        if op == "Cadastro de Horários": ManterHorarioUI.main()
        if op == "Cadastro de Profissionais": ManterProfissionalUI.main()
        if op == "Alterar Senha": AlterarSenhaUI.main()

    def sair_do_sistema():
        if st.sidebar.button("Sair"):
            del st.session_state["usuario_id"]
            del st.session_state["usuario_nome"]
            st.rerun()
    """
    def main():
        View.setup_db()
        IndexUI.sidebar()


IndexUI.main()