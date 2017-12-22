#!/usr/bin/python

from flask import Blueprint,render_template,request
from MongoConnector import MongoConnector, User
from flask_security import current_user

gerentes = Blueprint("gerentes",__name__)

@gerentes.route("/gerentes")
def gerentes_index():    
    gerente = User.objects(is_manager=True)
    return render_template("gerentes.html",gerentes=gerente)

@gerentes.route("/gerentes/<id>/")
def ver_gerentes(id):
    return render_template("ver_gerente.html")

@gerentes.route("/gerentes/novo")
def novo_gerente():
    return render_template("novo_gerente.html")

@gerentes.route("/profile")
def profile():
    u = User.objects(id=current_user.id).first()
    return render_template("novo_gerente.html",user=u)

@gerentes.route("/profile",methods=["POST"])
def profile_update():
    try:
        u = User.objects(id=current_user.id).first()        
        for attr in request.form:
            setattr(u,attr,request.form[attr])
        u.is_manager = bool(request.form["is_manager"])
        u.save()
        return render_template("novo_gerente.html",message="Usuario atualizado com sucesso!",status=0)
    except Exception as e:
        print("Erro!:", e)
        return render_template("novo_gerente.html",message="Falhou ao atualizar usuario! %s"%e,status=1)

@gerentes.route("/gerentes/novo",methods=["POST"])
def salvar_gerente():    
    try:
        user = User()        
        for attr in request.form:
            setattr(user,attr,request.form[attr])
        user.is_manager = bool(request.form["is_manager"])
        user.save()
        return render_template("novo_gerente.html",message="Gerente cadastrado com sucesso!",status=0)
    except Exception as e:
        print("Erro!:", e)
        return render_template("novo_gerente.html",message="Falhou ao cadastrar gerente! %s"%e,status=1)
