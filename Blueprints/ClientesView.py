#!/usr/bin/python

from flask import Blueprint,render_template,request
from MongoConnector import MongoConnector, login_required, current_user, User


clientes = Blueprint("clientes",__name__)


@clientes.route("/clientes")
@login_required
def clientes_index():
    pipeline = [{"$match":{"_id":current_user.id}},
                {"$lookup":{"from":"user",
                            "localField":"clients",
                            "foreignField":"_id",
                            "as":"clientes"}}]
    c = list(User.objects.aggregate(*pipeline))
    return render_template("clientes.html",clientes=c[0].get("clientes"))

@clientes.route("/clientes/<id>/")
@login_required
def ver_clientes(id):
    return render_template("ver_cliente.html")

@clientes.route("/clientes/novo")
@login_required
def novo_cliente():
    return render_template("novo_cliente.html")

@clientes.route("/clientes/novo",methods=["POST"])
@login_required
def salvar_cliente():
    try:
        user = User()        
        for attr in request.form:
            setattr(user,attr,request.form[attr])
        user.is_manager = bool(request.form["is_manager"])
        user.save()
        client_id = user.id
        u = User.objects(id=current_user.id).first()
        u.clients.append(client_id)
        u.save()
        return render_template("novo_cliente.html",message="Cliente cadastrado com sucesso!",status=0)
    except Exception as e:
        return render_template("novo_cliente.html",message="Cliente ao cadastrar gerente! %s"%e,status=1)
