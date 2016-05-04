Rapport de projet d'Apprentissage
=============================================

Liste des scrits :

		- Script1 : 
			Lancement d'une partie Human VS CPU en mode facile
		- Script1-2 : 
			Lancement d'une partie Human VS CPU en mode normal
		- Script1-3 : 
			Lancement d'une partie Human VS CPU en mode difficile
		- Script2 : 
			Lancement de 50 000 parties de 2 CPU en mode difficile, avec affichage du nombre de victoires
		- Script3 : 
			Lancement de 5 000 parties de 2 CPU avec des modes différents (Easy VS Medium, Easy VS Hard etc.)
			Enregistrement lors du mode Hard VS Hard du réseau de neurone dans un fichier sérialisé
		- Script4 :
			Jeu final, effectuer une partie Human VS CPU selon les 3 modes
			Le mode Hard utilise le fichier sérialisé créé avec le script 3
		- ScriptOptionnel :
			Lancement de 5 000 parties de 2 CPU en mode difficile, avec affichage des taux d'erreurs

Question 5

        L'ordinateur fait des erreurs car, la version "easy" utilise seulement une fonction
        random pour jouer.

Question 6

		Avec la version Médium, nous ne pouvons pas parler d'apprentissage. En effet, ce sont nous,
		codeurs, qui avons spécifié une action à réaliser selon une certaine situation. La machine n'a 
		pas appris d'elle-même afin de s'améliorer.
        
Question 8

		Le but de la méthode de faire jouer l'ordinateur contre lui-même est de faire de l'apprentissage.
		En effet, avec le réseau de neurone, on va privilégier le chemin par lequel il est passé lorsqu'il 
		a gagné. On va donc attribuer des récompenses aux synapses que la machine a emprunté lorsqu'elle a 
		gagnée.
		On va donc la faire jouer un grand nombre de fois afin qu'elle puisse apprendre d'elle-même et d'être
		de plus en plus forte.

		Dans le cas du Script 2, on peut remarquer qu'après un grand nombre de parties, la machine 1 remportera
		beaucoup plus de victoires que la machine 2, car cette dernière a découvert le "biais", c'est à dire 
		la technique pour gagner. Et vu que c'est elle qui joue en premier, elle sait se débrouiller pour 
		gagner.

Question 9

		En jouant contre l'ordinateur en mode Hard (et en 2ème joueur), il est impossible de gagner.
		L'ordinateur fera tout pour nous ammener à 13 batons, puis 9, puis 5 pour ensuite que l'on perde.
		En effet, 
			s'il reste 5 batons et que le joueur en choisi 1, l'ordinateur en choisira 3 (Le joueur perd)
			s'il reste 5 batons et que le joueur en choisi 2, l'ordinateur en choisira 2 (Le joueur perd)
			s'il reste 5 batons et que le joueur en choisi 3, l'ordinateur en choisira 1 (Le joueur perd)
		Plus tôt dans la partie,
			s'il reste 9 batons et que le joueur en choisi 1, l'ordinateur en choisira 3 (il restera 5 batons)
			s'il reste 9 batons et que le joueur en choisi 2, l'ordinateur en choisira 2 (il restera 5 batons)
			s'il reste 9 batons et que le joueur en choisi 3, l'ordinateur en choisira 1 (il restera 5 batons)

		Etc.


Question Optionnelle

		Pour gagner une partie en étant le premier joueur, nous devons faire en sorte de tomber sur les batons restants :
		13, 9 et 5. Si la première machine à chaque tour ne tombe pas sur un de ses chiffres après avoir joué (Multiples de 4 + 1),
		on comptabilise une erreur. A la fin de la partie, on obtient le taux d'erreur en divisant le nombre d'erreurs par le nombre
		de coup au total.
		Pour la deuxième machine, on ne compte pas forcément d'erreur puisqu'elle peut ne pas avoir le choix.

		On remarque bien en lançant le script Optionnel que plus les parties avancent et moins les machines font d'erreurs 
		(puisqu'elles apprennent de leurs parties précédentes).

		Une solution qui pourrait être mise en place pour améliorer le réseau de neurone final serait de "punir" certaines "synapses"
		lorsque la machine perd la partie. En effet, à l'heure actuelle, on récompense seulement lorsque la machine gagne.
		Le fait de punir certains chemins reviendrai à obtenir plus de chance d'emprunter un chemin qui fera gagner la machine.
