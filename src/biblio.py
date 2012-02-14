import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash
import adherent

# configuration
DATABASE = 'data_biblio.db'
DEBUG = True

# create application :
app = Flask(__name__)
app.config.from_object(__name__)

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])
    
@app.before_request
def before_request():
    g.db = connect_db()
    
@app.teardown_request
def teardown_request(exception):
    g.db.close()
    

@app.route("/")
def accueil():
    return render_template('accueil.html')
    

@app.route('/admin/adherent/<action>')
def routeAdherent(action):
	adh = adherent.Adherent()
	return adh.render(action)

if __name__ == "__main__":
    app.run()
