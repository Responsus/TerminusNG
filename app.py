#!/usr/bin/python

from flask import Flask,render_template
from flask import request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from Blueprints.ProjetosView import projetos
from Blueprints.ClientesView import clientes
from Blueprints.GerentesView import gerentes
from Blueprints.TarefasView import tarefas

from MongoConnector import db, user_datastore, security


app = Flask(__name__)
app.config["SECRET_KEY"] = "r3sp0nsus"
app.config['SECURITY_REGISTERABLE'] = True
app.config['SECURITY_SEND_REGISTER_EMAIL'] = False
app.config['SECURITY_PASSWORD_SALT'] = '3487432897342893498'
app.config['MONGODB_SETTINGS']= {"db":'terminusng','host':'localhost'}

app.register_blueprint(projetos)
app.register_blueprint(clientes)
app.register_blueprint(gerentes)
app.register_blueprint(tarefas)

db.init_app(app)

security.init_app(app, user_datastore)

@app.route("/")
@login_required
def index():
    aprovados = 0
    pendentes = 0
    reprovados = 0
    total = 0
    projetos = [
                {"id":1,"nome":"Projeto1","gerente":"Alisson Machado","data_entrega":"10/10/2014","status":"Em Andamento","progresso":"10%"},
                {"id":2,"nome":"Projeto2","gerente":"Alisson Machado","data_entrega":"10/10/2014","status":"Em Andamento","progresso":"10%"},
                {"id":3,"nome":"Projeto2","gerente":"Alisson Machado","data_entrega":"10/10/2014","status":"Em Andamento","progresso":"10%"}
                ]
    return render_template("index.html",aprovados=aprovados,pendentes=pendentes,reprovados=reprovados,total=total,projetos=projetos)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()    
    print(form.validate_on_submit())
    if request.method == 'POST' and form.validate_on_submit():
        print("entrou no post")
        user = app.config['USERS_COLLECTION'].find_one({"_id": form.username.data})
        print(user)
        print(form.password.data)
        if user and User.validate_login(user['password'], form.password.data):
            user_obj = User(user['_id'])
            login_user(user_obj)
            flash("Logged in successfully!", category='success')
            return redirect(request.args.get("next") or url_for("write"))
        flash("Wrong username or password!", category='error')
    return render_template('login.html', title='login', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000,debug=True)
