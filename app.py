#!/usr/bin/python

from flask import Flask,render_template
from Blueprints.ProjetosView import projetos
from Blueprints.ClientesView import clientes
from Blueprints.GerentesView import gerentes
from Blueprints.TarefasView import tarefas
from Models.TerminusModel import db


app = Flask(__name__)
app.register_blueprint(projetos)
app.register_blueprint(clientes)
app.register_blueprint(gerentes)
app.register_blueprint(tarefas)

@app.route("/")
def index():
    aprovados = 0
    pendentes = 0
    reprovados = 0
    total = 0
    projetos = [
                {"id":1,"nome":"Projeto1","gerente":"Alisson Machado","data_entrega":"10/10/2014","status":"Em Andamento","progresso":"10%"},
                {"id":2,"nome":"Projeto2","gerente":"Alisson Machado","data_entrega":"10/10/2014","status":"Em Andamento","progresso":"10%"},
                {"id":3,"nome":"Projeto2","gerente":"Alisson Machado","data_entrega":"10/10/2014","status":"Em Andamento","progresso":"10%"}
                ]
    return render_template("index.html",aprovados=aprovados,pendentes=pendentes,reprovados=reprovados,total=total,projetos=projetos)


if __name__ == '__main__':
    db.create_all()
    app.run(host="0.0.0.0",port=5000,debug=True)
