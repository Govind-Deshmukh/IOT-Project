from flask import Flask, url_for,request,render_template,redirect,jsonify

from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length

from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

from flask_bootstrap import Bootstrap


app = Flask(__name__)
app.secret_key="MagamInfoTech"
app.config['SECRET_KEY'] = 'Thisissupposedtobesecret!'
bootstrap = Bootstrap(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])

@app.route('/hello')
def hello():
    return 'Hello, World!'

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        if form.username.data == 'admin' and form.password.data == '12345678':
            user = User.query.filter_by(username=form.username.data).first()
            login_user(user)
            return redirect(url_for('dashboard'))
        return '<h1>Invalid username or password</h1>'
        # user = User.query.filter_by(username=form.username.data).first()
        # if user:
        #     if check_password_hash(user.password, form.password.data):
        #         login_user(user, remember=form.remember.data)
        #         return redirect(url_for('dashboard'))

        # return '<h1>Invalid username or password</h1>'

    return render_template('login.html', form=form)

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    if request.method == "POST":
        print(request.form.get("logout"))
    logout_user()
    #print("hear")
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)