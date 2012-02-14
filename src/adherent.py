 #!/usr/bin/python
 # -*- coding: iso-8859-15 -*-


from flask import render_template, g

class Adherent():
	"""
	Gestion des adhérents
	"""
	def __init__(self):
		pass

	def render(self,action):
		"""
		Composition des pages en fonction des actions
		"""
		if(action=='menu'):
			return render_template('adherent.html')
		if(action=='liste'):
			return self.show_entries()
			
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
		return render_template('liste_table.html', entries=entries, liste='Adhérents', parent='Gestion des adhérents')

