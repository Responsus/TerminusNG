#!/usr/bin/python

from flask import Blueprint,render_template,request
from Models.TerminusModel import (db, Gerentes as GerentesModel,
                                  Clientes as ClientesModel,
                                  Projetos as ProjetosModel,
                                  Tarefas as TarefasModel)

projetos = Blueprint("projetos",__name__)

@projetos.route("/projetos")
def projetos_index():
    projetos = db.session.query(ProjetosModel).all()
    return render_template("projetos.html",projetos=projetos)

@projetos.route("/projetos/<id>/")
def ver_projetos(id):
    projeto = db.session.query(ProjetosModel).filter(ProjetosModel.id==id).first()
    gerente = db.session.query(GerentesModel).join(ProjetosModel) \
                                             .filter(ProjetosModel.id==id) \
                                             .first()
    tarefas = db.session.query(TarefasModel).join(ProjetosModel).filter(ProjetosModel.id==id).all()
    return render_template("ver_projeto.html",projeto=projeto,gerente=gerente,
                           tarefas=tarefas)

@projetos.route("/projetos/<id>/execucao")
def execucao(id):
    tarefas = db.session.query(TarefasModel).join(ProjetosModel).filter(ProjetosModel.id==id).all()
    return render_template("execucao.html",tarefas=tarefas)

@projetos.route("/projetos/novo")
def novo_projeto():
    clientes = db.session.query(ClientesModel).all()
    gerentes = db.session.query(GerentesModel).all()
    return render_template("novo_projeto.html",gerentes=gerentes,clientes=clientes)

@projetos.route("/projetos/novo",methods=["POST"])
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
    projeto = ProjetosModel()
    try:
        projeto = ProjetosModel()
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
