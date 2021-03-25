from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column('user_id', db.Integer, unique=True, primary_key=True)
    name = db.Column(db.String(32))
   
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"{self.name}"

class Analytics(db.Model):
    
    id = db.Column('analytics_id', db.Integer, primary_key=True)
    views = db.Column(db.Integer)

    def __init__(self, views):
        self.views = views
    
    def __repr__(self):
        return f"{self.views}"


@app.route('/')
def index():
    if Analytics.query.first() == None:
        analytics = Analytics(0)
        db.session.add(analytics)
        db.session.commit()
    Analytics.query.first().views = Analytics.query.first().views + 1
    db.session.commit()

    return render_template("index.html", users=User.query.all(), num_page_views=Analytics.query.first())

if __name__ == "__main__":
    db.create_all()
    app.run(host='10.252.148.28', debug=True)
