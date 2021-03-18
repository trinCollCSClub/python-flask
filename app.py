from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
db = SQLAlchemy(app)

class Analytics(db.Model):
    
    id = db.Column('analytics_id', db.Integer, primary_key = True)
    views = db.Column(db.Integer)

    def __init__(self, views):
        self.views = views
    
    def __repr__(self):
        return f"{self.views}"

@app.route('/')
def hello_world():
    if Analytics.query.first() == None:
        analytics = Analytics(0)
        db.session.add(analytics)
        db.session.commit()
    Analytics.query.first().views = Analytics.query.first().views + 1
    db.session.commit()
    return f"This page has been viewed {Analytics.query.first()} times"

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
