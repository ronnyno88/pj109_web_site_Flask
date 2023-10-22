from flask import Flask, render_template, jsonify

app = Flask(__name__)

VAGAS = [
  {'id': 1, 'nome': 'Analista de Sistemas', 'salario': 3000},
  {'id': 2, 'nome': 'Analista de Negócios', 'salario': 4000},
  {'id': 3, 'nome': 'Analista de Marketing', 'salario': 5000},
  {'id': 4, 'nome': 'Analista de Design', 'salario': 6000},
  {'id': 5, 'nome': 'Analista de TI', 'salario': 7000}
]

@app.route('/')
def hello_world():
  return render_template('home.html', vagas=VAGAS)


@app.route('/vagas')
def listaVagas():
  return jsonify(VAGAS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
