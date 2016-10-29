#!/usr/bin/python

from flask import Blueprint,render_template,request
from Models.TerminusModel import Gerentes as GerentesModel, db
gerentes = Blueprint("gerentes",__name__)

@gerentes.route("/gerentes")
def gerentes_index():
    gerentes = db.session.query(GerentesModel).all()
    return render_template("gerentes.html",gerentes=gerentes)

@gerentes.route("/gerentes/<id>/")
def ver_gerentes(id):
    return render_template("ver_gerente.html")

@gerentes.route("/gerentes/novo")
def novo_gerente():
    return render_template("novo_gerente.html")

@gerentes.route("/gerentes/novo",methods=["POST"])
def salvar_gerente():
    nome = request.form['nome']
    email = request.form['email']
    telefone = request.form['telefone']
    senha = request.form['senha']
    try:
        novo = GerentesModel()
        novo.nome = nome
        novo.email = email
        novo.telefone = telefone
        novo.senha = senha
        db.session.add(novo)
        db.session.commit()
        return render_template("novo_gerente.html",message="Gerente cadastrado com sucesso!",status=0)
    except Exception as e:
        db.session.rollback()
        return render_template("novo_gerente.html",message="Falhou ao cadastrar gerente! %s"%e,status=1)
