 #!/usr/bin/python
 # -*- coding: iso-8859-15 -*-


from flask import render_template, g, url_for
from helpers import query_db

class Adherent():
	"""
	Gestion des adhérents
	"""
	def __init__(self,application):
		self.app = application

	def render(self,action):
		"""
		Composition des pages en fonction des actions
		"""
		if(action=='menu'):
			return render_template('adherent.html')
		if(action=='liste'):
			return self.show_entries()
		if(action.startswith('fiche=')==True):
			return self.show_entry(action)
			
		return render_template('adherent.html')
		
	def show_entries(self):
		"""
		Afficher la liste des adhérents
		"""
		cur = g.db.execute('select numero, nom, prenom,adr_rue, adr_CP, adr_ville from adherent order by numero')
		entries = []
		for row in cur.fetchall():
			texte = row[1].upper()+" "+row[2].capitalize()+"<adresse>"+row[3]+"-"+row[4]+" "+row[5].capitalize()+"</adresse>"
			entries.append(dict(title=row[0], text=texte))
		return render_template('liste_table.html',
								entries=entries, 
								liste='Adhérents', 
								parent=['menu','Gestion des adhérents'])
								
	def show_entry(self, requete):
		"""
		Afficher la fiche d'un adhérent
		"""
		
		numero = requete[6:]
		#cur = g.db.execute('select numero, nom, prenom,adr_rue, adr_CP, adr_ville from adherent where numero='+numero)
		#result = cur.fetchall()
		user = query_db('select * from adherent where numero=?',
                [numero], one=True)
		if user is None:
			return render_template('adherent.html')
		else:
			return render_template('adherent_fiche.html',
								entry=user, 
								parent=['liste','Liste des adhérents'])

