import psycopg2
from config import config
from flask import Flask, render_template, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = \
    f'postgresql://{config.DB_USER}:{config.DB_PASSWD}@localhost:5432/' \
    f'{config.DB_NAME}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = config.SECRET_KEY
db = SQLAlchemy(app)


users = db.Table(
    'users_measures',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
    db.Column('measure_id', db.Integer, db.ForeignKey('measures.id'), primary_key=True),
)


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'User: {self.first_name}, {self.last_name}'


class Measure(db.Model):
    __tablename__ = 'measures'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.Text, nullable=False)
    users = db.relationship(
        'User',
        lazy='dynamic',
        secondary=users,
        backref=db.backref('measures', lazy='dynamic'),
    )

    def __repr__(self):
        return f'Measure: {self.name}'


@app.route('/')
@app.route('/home')
def index():
    measures = Measure.query.all()
    return render_template('index.html', measures=measures)


@app.route('/registration/<int:measure_id>', methods=['POST', 'GET'])
def measure_registration(measure_id):
    measure = Measure.query.get(measure_id)
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        user = User.query.filter_by(
            first_name=first_name,
            last_name=last_name
            ).first()
        try:
            if not user:
                user_add = User(
                    first_name=request.form['first_name'],
                    last_name=request.form['last_name'],
                )
                db.session.add(user_add)
                db.session.commit()
            if user in measure.users.all():
                flash('Already registered!')
            else:
                measure.users.append(user_add)
                db.session.add(measure)
                db.session.commit()

            return redirect('/')
        except Exception as error:
            return f'User add to db failed: {error}'
    else:
        return render_template('registration.html', measure_id=measure_id)


# @app.route('/registration', methods=['POST', 'GET'])
# def registration():
#     measure = Measure.query.get(id)
#     if request.method == 'POST':
#         user = User.query.filter_by(
#             first_name=request.form['first_name'],
#             last_name=request.form['last_name']
#             ).first()
#         try:
#             if not user:
#                 user_add = User(
#                     first_name=request.form['first_name'],
#                     last_name=request.form['last_name'],
#                 )
#                 db.session.add(user_add)
#                 db.session.commit()
#             if user in measure.user.all():
#                 flash('Already registered!')
#             else:
#                 measure.user.append(user_add)
#                 db.session.add(measure)
#                 db.session.commit()
#             return redirect('/')
#         except Exception as error:
#             return flash(f'User add to db failed: {error}')
#     else:
#         return render_template('registration.html')


@app.route('/measure-add', methods=['POST', 'GET'])
def measure_add():
    if request.method == 'POST':
        measure_add_form = Measure(
            name=request.form['measure_name'],
            description=request.form['description']
        )
        try:
            db.session.add(measure_add_form)
            db.session.commit()
            return render_template('measure-add.html')
        except Exception as error:
            return flash(f'Measure add to db failed: {error}')
    else:
        return render_template('measure-add.html')


@app.route('/about', methods=['GET', 'POST'])
def measures():
    measures = Measure.query.all()
    return render_template('about.html', measures=measures)


if __name__ == '__main__':
    app.run()
