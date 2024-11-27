from flask import Flask, make_response, jsonify, request
from db import carros

# Iniciar o Flask

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

# Adicionar as funções e decorators (rotas)

@app.route('/carros', methods=['GET'])   # Utilizar o decorator pra criar uma rota com o método GET
def get_carros(): # Criar a função 
  return make_response(  # Construindo uma resposta da API
    jsonify(             # jsonify pra deixar "bonito" a lista dos carros
      #mensagem='Lista de Carros',
      dados=carros
    )
  )

@app.route('/carros', methods=['POST'])
def create_carro():
  carro = request.json
  carros.append(carro)
  return make_response(
    jsonify(
      mensagem='Carro cadastrado com sucesso.',
      carro=carro
    )
  )


# Rodar a aplicação
app.run() 
