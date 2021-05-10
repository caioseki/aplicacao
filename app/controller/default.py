from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from app import app, db
from app.model.tables import Aluno

@app.route("/")
def index():
    aluno = Aluno.query.all()
    return render_template("index.html", aluno=aluno)

@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        aluno = Aluno(request.form['nome'], 
                      request.form['email'], 
                      request.form['numero'],
                      request.form['cep'],
                      request.form['logradouro'],
                      request.form['complemento']
                      )
        db.session.add(aluno)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template("add.html")
@app.route("/edit/<int:ra>", methods=['GET', 'POST'])
def edit(ra):
    aluno = Aluno.query.get(ra)
    if request.method == 'POST':
        aluno.ra = request.form['ra']
        aluno.nome = request.form['nome']
        aluno.email = request.form['email']
        aluno.numero = request.form['numero']
        aluno.cep = request.form['cep']
        aluno.logradouro = request.form['logradouro']
        aluno.complemento = request.form['complemento']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template("edit.html", aluno=aluno)

@app.route("/delete/<int:ra>")
def delete(ra):
    aluno = Aluno.query.get(ra)
    db.session.delete(aluno)
    db.session.commit()
    return redirect(url_for('index'))
