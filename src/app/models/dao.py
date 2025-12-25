from abc import ABC, abstractmethod
import sqlite3
from pathlib import Path

class DAO(ABC):
    _objetos = []

    @staticmethod
    def get_connection():
        PATH = Path.cwd()
        DB_DIR = PATH / "src" / "app" / "db"
        DB_PATH = DB_DIR / "app.db"

        DB_DIR.mkdir(parents=True, exist_ok=True)
        
        conn = sqlite3.connect(DB_PATH)
        return conn

    @classmethod
    def setup_db(cls):
        conn = cls.get_connection()
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE,
                email TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL,
                enrolled_math INTEGER NOT NULL,
                enrolled_pt INTEGER NOT NULL,
                description TEXT,
                profile_pic BLOB,
                profile_pic_mime VARCHAR(127)
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS answers (
                question_id INTEGER NOT NULL,
                user_id INTEGER NOT NULL,
                PRIMARY KEY (question_id, user_id),
                FOREIGN KEY (question_id) REFERENCES questions(id),
                FOREIGN KEY (user_id) REFERENCES users(id)
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS admins (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS questions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                category INTEGER NOT NULL,
                title TEXT,
                text TEXT,
                picture BLOB,
                picture_mime_type VARCHAR(127),
                alternatives TEXT NOT NULL,
                correct_alternative INTEGER NOT NULL,
                added_by INTEGER,
                FOREIGN KEY (added_by) REFERENCES admins(id)
            )
        ''')

        conn.commit()

        conn.close()

    @classmethod
    def listar(cls):
        conn = cls.get_connection()
        cursor = conn.cursor()

        cursor.execute(f"SELECT * FROM {cls.table}")
        results = cursor.fetchall()
        
        conn.close()

        return results

    @classmethod
    def listar_id(cls, id):
        conn = cls.get_connection()
        cursor = conn.cursor()

        cursor.execute(f"SELECT * FROM {cls.table} WHERE id == ?", (id, ))
        results = cursor.fetchone()
        
        conn.close()

        return results

    @classmethod
    def listar_atributo(cls, nome, valor):
        conn = cls.get_connection()
        cursor = conn.cursor()

        cursor.execute(f"SELECT * FROM {cls.table} WHERE {nome} == ?", (valor, ))
        results = cursor.fetchone()
        
        conn.close()

        return results

    @classmethod
    def excluir_id(cls, id):
        conn = cls.get_connection()
        cursor = conn.cursor()

        cursor.execute(f"DELETE FROM {cls.table} WHERE id == ?", (id, ))
        result = cursor.rowcount
        
        conn.commit()
        conn.close()

        return result
    
    @classmethod
    @abstractmethod
    def editar_id(cls):
        pass

    @classmethod
    @abstractmethod
    def salvar(cls):
        pass