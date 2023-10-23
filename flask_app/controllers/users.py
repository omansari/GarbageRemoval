from flask import render_template, session, redirect, request, flash
from flask_bcrypt import Bcrypt
from flask_app import app
from flask_app.models.user import User

bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('index.html')
# this the route for the login/home page 
# homework: change the file. add new html files to put there where (test.html) (fix the database problem)

@app.route('/register', methods = ['POST'])
def register():
    if not User.validate_register(request.form):
        return redirect('/')

    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': bcrypt.generate_password_hash(request.form['password'])
    }
    
    id = User.save(data)
    session['user_id'] = id
    return redirect('/dashboard')

@app.route('/name', methods = ['GET'])
def get_name():
    #user = User.get_by_name(cls, data)
    #name = [user]
    name2 = "Omar Ansari"
    return name2

@app.route('/create/user', methods = ['POST'])
def create_user():

    if User.is_valid(request.form):
        User.save(request.form)
        return redirect('/results')

    return redirect('/dashboard')

@app.route('/results')
def results():
    return redirect('/dashboard', user = User.get_by_id(id))

@app.route('/login', methods = ['POST'])
def login():

    user = User.get_by_email(request.form)
    
    if not user:
        flash('Invaild email.', 'login')
        return redirect('/')
    
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash('Invaild password.', 'login')
        return redirect('/')

    session['user_id'] = user.id
    return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():

    if 'user_id' not in session:
        return redirect('/logout')

    data = {

        'id': session['user_id']

    }

    print(data)
    return render_template('dashboard.html', user = User.get_by_id(data))

@app.route('/testdashboard')
def testdashboard():

    if 'user_id' not in session:
        return redirect('/logout')

    data = {

        'id': session['user_id']

    }

    print(data)
    return render_template('dashboardtest.html', user = User.get_by_id(data))

@app.route('/reportjoincleanup')
def reportjoincleanup():

    if 'user_id' not in session:
        return redirect('/logout')

    data = {

        'id': session['user_id']

    }

    print(data)
    return render_template('reportjoincleanup.html', user = User.get_by_id(data))

@app.route('/scheduleing')
def scheduleing():

    if 'user_id' not in session:
        return redirect('/logout')

    data = {

        'id': session['user_id']

    }

    print(data)
    return render_template('scheduleing.html', user = User.get_by_id(data))


@app.route('/logout')
def logout():

    session.clear()
    return redirect('/')