# instalar o Flask
# pip install flask

from flask import Flask, render_template

# cria a instancia/cópia do Flask
app = Flask(__name__)

#decorador - define a URL raiz
@app.route('/')
#Define a função
def home():
    return render_template("home.html")

@app.route('/cadastro')
def cadastro():
    return render_template("cadastro.html")

@app.route('/consulta')
def consulta():
    return render_template("consulta.html")

if __name__ == '__main__':
    app.run(debug=True)