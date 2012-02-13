import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash
app = Flask(__name__)

@app.route("/")
def accueil():
    return render_template('accueil.html')
    
@app.route("/admin/adherent/")
def adherent():
	return render_template('adherent.html')

if __name__ == "__main__":
    app.run()
