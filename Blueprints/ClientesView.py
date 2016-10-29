#!/usr/bin/python

from flask import Blueprint,render_template,request
from Models.TerminusModel import Clientes as ClientesModel, db

clientes = Blueprint("clientes",__name__)

@clientes.route("/clientes")
def clientes_index():
    clientes = db.session.query(ClientesModel).all()
    return render_template("clientes.html",clientes=clientes)

@clientes.route("/clientes/<id>/")
def ver_clientes(id):
    return render_template("ver_cliente.html")

@clientes.route("/clientes/novo")
def novo_cliente():
    return render_template("novo_cliente.html")

@clientes.route("/clientes/novo",methods=["POST"])
def salvar_cliente():
    nome = request.form['nome']
    email = request.form['email']
    telefone = request.form['telefone']
    senha = request.form['senha']
    try:
        novo = ClientesModel()
        novo.nome = nome
        novo.email = email
        novo.telefone = telefone
        novo.senha = senha
        db.session.add(novo)
        db.session.commit()
        return render_template("novo_cliente.html",message="Cliente cadastrado com sucesso!",status=0)
    except Exception as e:
        db.session.rollback()
        return render_template("novo_cliente.html",message="Cliente ao cadastrar gerente! %s"%e,status=1)
