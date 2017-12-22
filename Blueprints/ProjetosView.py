#!/usr/bin/python

from flask import Blueprint,render_template,request
from MongoConnector import MongoConnector

projetos = Blueprint("projetos",__name__)

@projetos.route("/projetos")
def projetos_index():
    mc = MongoConnector()
    db = mc.get_connection()
    projetos = db.projetos.find({})
    return render_template("projetos.html",projetos=projetos)

@projetos.route("/projetos/<id>/")
def ver_projetos(id):
    projeto = ""
    gerente = ""
    tarefas = ""
    return render_template("ver_projeto.html",projeto=projeto,gerente=gerente,
                           tarefas=tarefas)

@projetos.route("/projetos/<id>/execucao")
def execucao(id):
    tarefas = ""
    return render_template("execucao.html",tarefas=tarefas)

@projetos.route("/projetos/novo")
def novo_projeto():
    clientes = "" 
    gerentes = ""
    return render_template("novo_projeto.html",gerentes=gerentes,clientes=clientes)

@projetos.route("/projetos/novo",methods=["POST"])
def salvar_projeto():
    projeto = {}
    projeto["nome"] = request.form['nome']
    projeto["cliente"] = request.form['cliente']
    projeto["gerente"] = request.form['gerente']
    projeto["objetivo"] = request.form['objetivo']
    projeto["cenario_atual"] = request.form['cenario_atual']
    projeto["cenario_proposto"] = request.form['cenario_proposto']
    projeto["data_inicio"] = request.form['data_inicio']
    projeto["data_termino"] = request.form['data_termino']
    projeto["valor"] = request.form['valor']
    try:
        mc = MongoConnector()
        db = mc.get_connection()
        db.projetos.insert(projeto)
        return render_template("novo_projeto.html",message="Projeto salvo com sucesso!",status=0)
    except Exception as e:
        print("Deu erro! ",e)
        return render_template("novo_projeto.html",message="Falhou ao salvar o projeto! %s"%e,status=1)
