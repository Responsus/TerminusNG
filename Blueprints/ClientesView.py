#!/usr/bin/python

from flask import Blueprint,render_template,request
from MongoConnector import MongoConnector

clientes = Blueprint("clientes",__name__)

@clientes.route("/clientes")
def clientes_index():
    mc = MongoConnector()
    db = mc.get_connection()
    cliente = db.clientes.find({})
    return render_template("clientes.html",clientes=cliente)

@clientes.route("/clientes/<id>/")
def ver_clientes(id):
    return render_template("ver_cliente.html")

@clientes.route("/clientes/novo")
def novo_cliente():
    return render_template("novo_cliente.html")

@clientes.route("/clientes/novo",methods=["POST"])
def salvar_cliente():
    cliente = {}
    cliente["nome"] = request.form['nome']
    cliente["email"] = request.form['email']
    cliente["telefone"] = request.form['telefone']
    cliente["senha"] = request.form['senha']
    try:
        mc = MongoConnector()
        db = mc.get_connection()
        db.clientes.insert(cliente)
        return render_template("novo_cliente.html",message="Cliente cadastrado com sucesso!",status=0)
    except Exception as e:
        db.session.rollback()
        return render_template("novo_cliente.html",message="Cliente ao cadastrar gerente! %s"%e,status=1)
