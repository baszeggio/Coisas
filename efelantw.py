from flask import Flask, request
import uuid
import psycopg

app = Flask(__name__)
connection_db = psycopg.connect("host=164.90.152.205 bdname=turma3f user=postgres password=")

@app.route("/pessoas", methods=["POST"])
def incluir_pessoa():
    dados_recebidos = request.get_json()
    id = uuid.uuid4()
    nome = dados_recebidos['nome']

    cursor = connection_db.cursor()
    cursor.execute('insert into pessoas (id, nome) values (%s, %s)', (id, nome))
    connection_db.commit()

    return {
        'id': id
    }

@app.route("/vendas", methods=["GET"])
def get_vendas():
    cursor = connection_db.cursor()
    cursor.execute('''select * from vendas
left join pessoas on vendas.id = pessoa.id
left join produtos on vendas.id produto - produtos.id''')

    lista = []
    for item in cursor:
        lista.append({
            'id': item[0],
            'pessoa' : (
                'id': item[1]
                'nome': item[4]
            ),
            'produto': (
                'id': item[2]
                'nome': item[6]
                'preco': item[7]
            )
        })
    return lista

@app.route("/pessoas/<id>", methods=["PUT"])
def atualizar_pessoas(id):
    dados_recebidos = request.get_json()
    nome = dados_recebidos['nome']

    cursor = connection_db.cursor()
    cursor.execute('update pessoas set nome = %s where id = %s', (nome, id))
    connection_db.commit()
    return {
        'id': id
    }
