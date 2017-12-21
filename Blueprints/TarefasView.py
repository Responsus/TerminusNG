#!/usr/bin/python

from flask import Blueprint,render_template,request,jsonify
from Models.TerminusModel import db, Projetos as ProjetosModel, Clientes as ClientesModel, Tarefas as TarefasModel

tarefas = Blueprint("tarefas",__name__)

@tarefas.route("/tarefas")
def tarefas_index():
    tarefas = db.session.query(tarefasModel).all()
    return render_template("tarefas.html",tarefas=tarefas)

@tarefas.route("/projetos/<id>/tarefas",methods=["POST"])
def salvar_tarefas(id):
    tarefa = TarefasModel()
    try:
        titulo = request.form["titulo"]
        descricao = request.form["descricao"]
        tarefa.titulo = titulo
        tarefa.descricao = descricao
        db.session.add(tarefa)
        projeto = db.session.query(ProjetosModel).filter(ProjetosModel.id==id).first()
        projeto.tarefas.append(tarefa)
        db.session.commit()
        return jsonify({"message":"Tarefa Cadastrada com Sucesso!","status":0})
    except Exception as e:
        db.session.rollback()
        return jsonify({"message":"Falhou ao cadastrar tarefa %s"%e,"status":1})

@tarefas.route("/tarefas/<id>/execucao")
def execucao(id):
    return render_template("execucao.html")

@tarefas.route("/tarefas/novo")
def novo_projeto():
    clientes = db.session.query(ClientesModel).all()
    gerentes = db.session.query(GerentesModel).all()
    return render_template("novo_projeto.html",gerentes=gerentes,clientes=clientes)

@tarefas.route("/tarefas/novo",methods=["POST"])
def salvar_projeto():
    nome = request.form['nome']
    cliente = request.form['cliente']
    gerente = request.form['gerente']
    objetivo = request.form['objetivo']
    cenario_atual = request.form['cenario_atual']
    cenario_proposto = request.form['cenario_proposto']
    data_inicio = request.form['data_inicio']
    data_termino = request.form['data_termino']
    valor = request.form['valor']
    projeto = tarefasModel()
    try:
        projeto = tarefasModel()
        projeto.nome = nome
        projeto.cliente_id = int(cliente)
        projeto.gerente_id = int(gerente)
        projeto.objetivo = objetivo
        projeto.cenario_atual = cenario_atual
        projeto.cenario_proposto = cenario_proposto
        projeto.data_inicio = data_inicio
        projeto.data_termino = data_termino
        projeto.valor = valor
        db.session.add(projeto)
        db.session.commit()
        return render_template("novo_projeto.html",message="Projeto salvo com sucesso!",status=0)
    except Exception as e:
        print("Deu erro! ",e)
        return render_template("novo_projeto.html",message="Falhou ao salvar o projeto! %s"%e,status=1)
