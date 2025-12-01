class UsuarioDAO(DAO):
    table = "emails"

    @classmethod
    def email_listar(cls, email):
        conn = cls.get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT * FROM users WHERE email == ?;
        """, (email,))
        
        return cursor.fetchone()

    @classmethod
    def listar_nome(cls, nome):
        conn = cls.get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT * FROM users WHERE name == ?;
        """, (nome,))
        
        return cursor.fetchone()

    @classmethod
    def salvar(cls, obj):
        conn = cls.get_connection()
        cursor = conn.cursor()

        user_data = obj.to_sqlite()

        cursor.execute('INSERT OR IGNORE INTO users (name, email, password, enrolled_math, enrolled_pt, xp_math, xp_pt, profile_pic, profile_pic_mime, is_beta) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', user_data)

        conn.commit()
        conn.close()

        if cursor.rowcount > 0:
            return cursor.lastrowid