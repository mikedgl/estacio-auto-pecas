import sqlite3

def create_connection():
    conn = sqlite3.connect("fornecedores.db")
    return conn

def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS fornecedores (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      razao_social TEXT, cnpj TEXT,
                      representante TEXT, cpf_representante TEXT,
                      celular TEXT, email TEXT, endereco TEXT)''')
    conn.commit()
    conn.close()

def insert_fornecedor(data):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO fornecedores 
                      (razao_social, cnpj, representante, cpf_representante, celular, email, endereco) 
                      VALUES (?, ?, ?, ?, ?, ?, ?)''', data)
    conn.commit()
    conn.close()


def find_all_fornecedores(razao=None, cnpj=None):
    conn = create_connection()
    cursor = conn.cursor()

    query = "SELECT id, razao_social, cnpj, celular, email FROM fornecedores"
    filters = []

    if razao and razao != "Razão Social":
        filters.append(f"razao_social LIKE '%{razao}%'")
    if cnpj and cnpj != "CNPJ":
        filters.append(f"cnpj = '{cnpj}'")

    if filters:
        query += " WHERE " + " AND ".join(filters)

    cursor.execute(query)
    records = cursor.fetchall()
    conn.close()

    return records

def delete_fornecedor(fornecedor_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM fornecedores WHERE id = ?", (fornecedor_id,))
    conn.commit()
    conn.close()

def update_fornecedor(fornecedor_id, data):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute('''UPDATE fornecedores
                      SET razao_social = ?, cnpj = ?, representante = ?, cpf_representante = ?, celular = ?, 
                          email = ?, endereco = ?
                      WHERE id = ?''', (*data, fornecedor_id))

    conn.commit()
    conn.close()

def find_fornecedor_by_id(fornecedor_id):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute('''SELECT * FROM fornecedores WHERE id = ?''', (fornecedor_id,))
    record = cursor.fetchone()

    conn.close()
    return record
