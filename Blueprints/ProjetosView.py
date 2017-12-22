#!/usr/bin/python

from flask import Blueprint,render_template,request
from MongoConnector import MongoConnector, current_user, User, Projects, login_required

projetos = Blueprint("projetos",__name__)

@projetos.route("/projetos")
@login_required
def projetos_index():
    p = Projects.objects(manager_id=current_user.id)
    return render_template("projetos.html",projetos=p)

@projetos.route("/projetos/<id>/")
@login_required
def ver_projetos(id):
    projeto = ""
    gerente = ""
    tarefas = ""
    return render_template("ver_projeto.html",projeto=projeto,gerente=gerente,
                           tarefas=tarefas)

@projetos.route("/projetos/<id>/execucao")
@login_required
def execucao(id):
    tarefas = ""
    return render_template("execucao.html",tarefas=tarefas)

@projetos.route("/projetos/novo")
@login_required
def novo_projeto():
    pipeline = [{"$match":{"_id":current_user.id}},
                {"$lookup":{"from":"user",
                            "localField":"clients",
                            "foreignField":"_id",
                            "as":"clientes"}}]
    c = list(User.objects.aggregate(*pipeline))
    clientes = c[0].get("clientes")
    gerente = [{"_id":current_user.id,"name":current_user.name}]
    return render_template("novo_projeto.html",gerentes=gerente,clientes=clientes)

@projetos.route("/projetos/novo",methods=["POST"])
@login_required
def salvar_projeto():    
    try:
        p = Projects()
        for attr in request.form:
            setattr(p,attr,request.form[attr])
        p.budget = float(request.form["budget"])
        p.manager_id = current_user.id
        p.save()
        return render_template("novo_projeto.html",message="Projeto salvo com sucesso!",status=0)
    except Exception as e:
        print("Deu erro! ",e)
        return render_template("novo_projeto.html",message="Falhou ao salvar o projeto! %s"%e,status=1)
