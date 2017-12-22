#!/usr/bin/python

from flask import Blueprint,render_template,request
from MongoConnector import MongoConnector

gerentes = Blueprint("gerentes",__name__)

@gerentes.route("/gerentes")
def gerentes_index():
    mc = MongoConnector()
    db = mc.get_connection()
    gerente = db.gerentes.find({})
    return render_template("gerentes.html",gerentes=gerente)

@gerentes.route("/gerentes/<id>/")
def ver_gerentes(id):
    return render_template("ver_gerente.html")

@gerentes.route("/gerentes/novo")
def novo_gerente():
    return render_template("novo_gerente.html")

@gerentes.route("/gerentes/novo",methods=["POST"])
def salvar_gerente():
    gerente = {}
    gerente["nome"] = request.form['nome']
    gerente["email"] = request.form['email']
    gerente["telefone"] = request.form['telefone']
    gerente["senha"] = request.form['senha']
    try:
        mc = MongoConnector()
        db = mc.get_connection()
        db.gerentes.insert(gerente)
        return render_template("novo_gerente.html",message="Gerente cadastrado com sucesso!",status=0)
    except Exception as e:
        db.session.rollback()
        return render_template("novo_gerente.html",message="Falhou ao cadastrar gerente! %s"%e,status=1)
