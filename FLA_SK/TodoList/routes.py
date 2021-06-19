from os import error
from flask import redirect, request, render_template
from TodoList import app, db
from .models import Todo

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        email = request.form['email']
        city = request.form['city']
        try:
            user = Todo(name=name, phone=phone, email=email, city=city)
            db.session.add(user)
            db.session.commit()
            redirect('/')
        except error:
            return f'There is Somthing Wrong...! {error}'
    todo = Todo.query.all()
    return render_template('index.html', todo=todo)


@app.route('/delete/<int:id>')
def delete(id):
    user = Todo.query.get_or_404(id)
    try:
        db.session.delete(user)
        db.session.commit()
    except error:
        return f'There is Somthing Wrong...! {error}'
    return redirect('/')


@app.route('/update/<int:id>', methods=['POST', 'GET'])
def update(id):
    user = Todo.query.get_or_404(id)
    if request.method == 'POST':
        user.name = request.form['name']
        user.phone = request.form['phone']
        user.email = request.form['email']
        user.city = request.form['city']
        try:
            db.session.commit()
            return redirect('/')
        except error:
            return f'There is Somthing Wrong...! {error}'       
    return render_template('update.html', user=user)