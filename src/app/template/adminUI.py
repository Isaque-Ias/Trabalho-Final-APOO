import streamlit as st
from views import View
from pathlib import Path
import pandas as pd
import json
from PIL import Image
import io
import base64

class AdminUI:
    CWD = Path.cwd()
    @staticmethod
    def fill(session_name, default=""):
        if session_name not in st.session_state:
            return default
        return st.session_state[session_name]
    
    @classmethod
    def main(cls):
        tab1, tab2, tab3, tab4 = st.tabs(["Visão Geral", "Gerenciar Questões", "Gerenciar Administradores", "Sair"])
        with tab1: cls.visao_geral()
        with tab2: cls.questoes()
        with tab3: cls.admins()
        with tab4: cls.sair()

    @staticmethod
    def visao_geral():
        mapping = {
            "0": "A",
            "1": "B",
            "2": "C",
            "3": "D",
            "4": "E",
        }
        questoes = View.questoes_listar()
        if len(questoes) == 0: st.write("Nenhuma questão cadastrada")
        else:
            rows = ""
            for obj in questoes:
                base64_string = obj.get_pic()
                if obj.get_text():
                    html_enunciado = obj.get_text()[:30] + "..."
                else:
                    html_enunciado = f'<img src="data:image/png;base64,{base64_string}" width="120">'
                
                alternativas = """<ul style='list-style-type:none;'>
    <li>a</li>
    <li>b</li>
    <li>c</li>
</ul>"""
                    
                rows += f"""<tr>
    <td>{obj.get_id()}</td>
    <td>{"Matemática" if obj.get_cat() == 0 else "Português"}</td>
    <td>{html_enunciado}</td>
    <td>{alternativas}</td>
    <td>{obj.get_added_by()}</td>
</tr>\n"""
                print(rows)
            code = f"""<table>
    <tr>
        <th>ID</th>
        <th>Categoria</th>
        <th>Enunciado</th>
        <th>Alternativas</th>
        <th>Criador</th>
    </tr>
    {rows}
</table>"""
            print(code)
            st.markdown(code, unsafe_allow_html=True)
                
    @classmethod
    def questoes(cls):
        tab1, tab2, tab3 = st.tabs(["Criar", "Editar", "Excluir"])
        with tab1: cls.questoes_add()

    @classmethod
    def questoes_add(cls):
        categoria = st.selectbox("Categoria", ["Matemática", "Português"])
        texto = st.text_area("Texto")
        imagem = st.file_uploader("Imagem", ["png", "jpg", "jpeg"], False)
        qa = st.text_input("Alternativa 1")
        qb = st.text_input("Alternativa 2")
        qc = st.text_input("Alternativa 3")
        qd = st.text_input("Alternativa 4")
        qe = st.text_input("Alternativa 5")
        alternativa_correta = st.number_input("Alternativa Correta", 1, 5)

        if st.button("Enviar"):
            fail = ""
            if categoria == "Matemática":
                categoria = 0
            else:
                categoria = 1

            final_image = ""
            mime_type = ""
            if imagem:
                image = Image.open(imagem)
                mime_type = image.format.lower()
                buffer = io.BytesIO()
                image.save(buffer, format=image.format)
                blob_image = buffer.getvalue()
                final_image = base64.b64encode(blob_image).decode("utf-8")
                
            json_alt = {}
            can_fail = False
            for idx, alt in enumerate([qa, qb, qc, qd, qe]):
                if alt:
                    if can_fail:
                        fail = "Preencha na ordem correta"
                    json_alt[idx] = alt
                else:
                    can_fail = True
            
            if alternativa_correta > len(json_alt):
                fail = "Alternativa deve estar entre o total de opções"

            if not texto and not imagem:
                fail = "Informe pelo menos um texto ou uma imagem"

            if len(json_alt) <= 1:
                fail = "Insira pelo menos duas alternativas"

            if fail:
                st.warning(fail)
            else:
                View.inserir_questao(categoria, json_alt, alternativa_correta, texto, final_image, mime_type, st.session_state.adm_id)
                st.success("Questão adicionada!")
                st.rerun()

    def admins():
        pass

    def sair():
        if st.button("Sair"):
            st.session_state.screen = "login"