import edt_analyser

class Menu:
	def __init__(self, titre, commands):
		self.titre = titre
		self.commands = commands


	def help(self):
		print(self.titre)
		print("Tapez q ou quit pour retourner au menu précédent")
		print("Tapez h ou help pour revoir ce message")
		for k,v in self.commands.items():
			print("Tapez", k, "pour", v['help'])


	def wait(self):

		print(self.titre)

		command = [""]

		while not(command[0] == 'q' or command[0] == 'quit'):
			print()			
			command = input(">> ").split()
			print()

			if command[0] == 'h' or command[0] == 'help':
				self.help()
			elif command[0] in self.commands:
				value = self.commands[command[0]]
				arguments = command[1:value['args']+1]
				value['fct'](*arguments)
			elif command[0] == 'q' or command[0] == 'quit':
				print("Retour au menu précédent")
			else:
				print("Cette commande n'existe pas, tapez h ou help pour plus d'informations")


class Interface:
	def __init__(self):
		self.edt = edt_analyser.Edt()
		option = edt_analyser.Option([18], [2,3], [0,1,2,4,5,6])
		option2 = edt_analyser.Option([15], [1], [0,1,2,4,5,6])
		self.edt.addOption(option)
		self.edt.addOption(option2)

		self.menuGroups = Menu("Interface de gestion des groupes",
								{
									'add' : {'fct' : lambda g : self.edt.addEdt(g), 'args' : 1, 'help' : "ajouter un groupe"},
									'remove' : {'fct' : lambda g : self.edt.removeEdt(g), 'args' : 1, 'help' : "enlever un groupe"},
									'info' : {'fct' : lambda : self.infoGroups(), 'args' : 0, 'help' : "afficher des informations sur les groupes"}
								})

		self.menuInterface = Menu("Interface de l'Edt Analyser",
								{
									'groups' : {'fct' : lambda : self.menuGroups.wait(), 'args' : 0, 'help' : "gérer les groupes"},
									'launch' : {'fct' : lambda : self.edt.compareAndPrint(), 'args' : 0, 'help' : "lancer le programme"}
								})

		self.menuInterface.wait()

		print("Au revoir !")


	def infoGroups(self):
		groupsAvailable = self.edt.groupAvailable()
		groupsAdded = list(self.edt.edt.keys())
		groupsAdded.sort()

		print("Groupes disponibles :")
		print(groupsAvailable)
		print("Groupes déjà ajoutés :")
		print(groupsAdded)


		
Interface()
