#!/usr/bin/python

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Terminus.db'
db = SQLAlchemy(app)

class Gerentes(db.Model):
    __tablename__ = 'gerentes'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80))
    especialidade = db.Column(db.String(80))
    email = db.Column(db.String(120), unique=True)
    telefone = db.Column(db.String(120))
    senha = db.Column(db.String(120))

class Projetos(db.Model):
    __tablename__ = 'projetos'
    id = db.Column(db.Integer, primary_key=True)
    gerente_id = db.Column(db.Integer,db.ForeignKey("gerentes.id"))
    cliente_id = db.Column(db.Integer,db.ForeignKey("clientes.id"))
    nome = db.Column(db.String(80))
    objetivo = db.Column(db.String(120))
    cenario_atual = db.Column(db.String(120))
    cenario_proposto = db.Column(db.String(120))
    data_inicio = db.Column(db.String(120))
    data_termino = db.Column(db.String(120))
    valor = db.Column(db.String(120))
    status = db.Column(db.Integer(),default=0)
    tarefas = db.relationship("Tarefas")

class Clientes(db.Model):
    __tablename__ = 'clientes'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80))
    email = db.Column(db.String(120))
    telefone = db.Column(db.String(120))
    senha = db.Column(db.String(120))

class Tarefas(db.Model):
    __tablename__ = 'tarefas'
    id = db.Column(db.Integer, primary_key=True)
    projeto_id = db.Column(db.Integer(),db.ForeignKey("projetos.id"))
    titulo = db.Column(db.String(80))
    descricao = db.Column(db.String(120))
    data_termino = db.Column(db.String(120))
    status = db.Column(db.Integer(),default=0)
    subtarefas = db.relationship("SubTarefas")

class SubTarefas(db.Model):
    __tablename__ = 'subtarefas'
    id = db.Column(db.Integer, primary_key=True)
    tarefa_id = db.Column(db.Integer, db.ForeignKey("tarefas.id"))
    titulo = db.Column(db.String(80), unique=True)
    descricao = db.Column(db.String(120), unique=True)
