## A retenir

- Pourquoi estimation = fourchette
- Interval de confiance
- z-test
- possible autres tests


## Slides

### Intro et problèmatique

#### En gros : qu'est-ce qu'un test AB ?

- Technique d'optimisation de pages web
- Exemple de processus de décision "Data-Driven"
- On va "aider" l'intuition des experts métier par des mesures concrètes
- On ne fait que de l'optimisation locale

#### Comment fait-on un test AB ?

- On implémente deux variantes de la même fonctionnalité
- On expose chacune à une partie des visiteurs du site pendant **un certain temps**
- On **estime** le "taux de conversion" de chacune des variantes
- On choisi la meilleure

#### Une estimation ?

- Taux de conversion = propriété fantasmée du bouton !
  * Combien d'utilisateurs cliqueraient sur le bouton s'ils le voyaient tous.
  * Cela est impossible !
  
#### Une estimation ?
  
En conséquence :
- On calcule une estimation du taux de conversion, à partir d'un échantillon
- Si on répète le test avec un autre échantillon, on aura "à peu près" le même résultat!

Autrement dit :
TC^ = TC +/- \deltaTC

(dessin)

#### Laquelle est la meilleure ?

Supposez le résultat suivant :

TC^_1 = 0.3 +/- 0.2
TC^_2 = 0.2 +/- 0.1

(avec dessin)

Quelle variante choisir ?

*Enter* la théorie des probabilités ...


#### TRANSITION : PAS METTRE - Le but de cette présentation

- Formaliser le problème du test ABComprendre un test AB avec la théorie des probabilités
- Calculer "interval de confiance"
- Dire : peux-je être raisonablement sûr que tel bouton convertit plus que tel autre ?
- Quantifier tout ça

---

### Théorie des probabilités : kesako ? (1)

- On pense qu'on vit dans un monde déterministe ... mais souvent impossible à déterminer de résultat de quelque chose exactement (trop de paramètres) :
* lancer d'une pièce ?
* combien clics dans un bouton ?
* Charge sur un serveur

### Théorie des probabilités : kesako ? (2)

- Probabilité : description du monde qui prend en compte l'incertitude, qui la quantifie :
* pièce : heads/tails -> probabilité de 50% => si je répète l'expérience assez de fois, j'aurais 50% heads, 50% tails
* clics sur un bouton : si rien ne change par ailleurs, si je répète l'expérience assez de fois, 5% des personnes vont cliquer
* 90% des fois, la charge sur un serveur à telle heure est comprise entre tant et tant

### Qu'est-ce que la probabilité (3)

Interprétation fréquentiste de la probabilité : 

### Taux de conversion

(ramener le problème du calcul d'un taux de conversion à un problème connu : prédire le lancée d'une pièce)

#### Notre expérience

On a une population de visiteurs : tous les visiteurs possibles du site LeMonde.fr (N)
On a un bouton : on suppose que si tout le monde est présenté à ce bouton, *X* personnes vont cliquer.
p = X/N : paramètre de la population, impossible à déterminer.


On prend un échantillon : *n*, à qui on présente le bouton.
*x* personnes cliquent sur cet échantillon
On calcule une estimation *p^ = x/n*
Estimation : taux de conversion de notre expérience qui approche "à peu près" le vrai.

#### Ceci ressemble à une succession de lancers de pièces

- J'ai une pièce avec paramètre *p* (probabilité de H/T, le biais)
- Pour chaque personne, je lance la pièce et j'ai un résultat : succès, échec
- Je répète l'expérience *n* fois
- Je compte le nombre total de succès : *x*
- *x* est une **Variable aléatoire**
- Je calcule mon "estimateur" : p^ = x/n
- Comment quantifier l'erreur ? (savoir quel est l'écart entre p^ et p) 

#### Quel rapport entre p^ et p

(on peut montrer que :)

Graph [slide 6](http://fr.slideshare.net/amitsawhney/the-mathbehindabtesting)

* p^ est une estimation, centrée autour de p - une variable aléatoire !
* avec du bruit : erreur type de p

- nombre de clics : variable aléatoire !!
- taux conversion : propriété "fantasmée du bouton".

* Si on connaissait la courbe, on pourrait calculer les probabilités ...

#### C'est long à expliquer mais, dans notre cas :

- p^ ~ Normal(p,SE) = blablabla

- SE = blablabla grosse formule

- Exemple de calculs ...
- Fonction continue : pas de définition de probability d'une valeur déterminée, uniquement d'intervals

#### Interval de confiance ...

p in I(p^) = p^ +/- 1.96 * SE

"On est sûrs, à 95%, que cet interval contient le vrai paramètre"

#### Récap

- Estimation : moyenne, interval, incertitude.

Si l'interval contient zero ou s'approche bcp de zero, il faut écarter ce taux de conversion.


### Comparer deux estimations

#### Motivation

- Intervals superposés : erreur ...
- Pourquoi il ne faut pas croiser les intervals ...

- Je peux : être raisonnablement sûr que la différente dans les taux observés n'a pas été due au hazard (i.e.  que si je la répète demain j'ai une chance non négligeable d'avoir la même différentes)

Graph [slide 9](http://fr.slideshare.net/amitsawhney/the-mathbehindabtesting)
=> We take the wrong conclusion !


#### Vérification d'hypothèses

Méthodologie en stats. Dans notre cas, ça se formalise de la manière suivante :

Deux expériences : X_1 (p^_1, n_1), X_2 (p^_2, n_2)

- On observe une différence (p^_1 = 0.3, P^_2 = 0.2)

- Supposant qu'il n'y a pas de différence en vrai (p_1 = p_2), quelle est la probabilité d'obtenir ce résultat ? -> probabilité d'avoir un faux positif.

- On veut savoir si cette probabilité est moins que \alpha, notre seuil d'erreurs (5%)
-> Différence pas due au hazard !

#### Z-Test

- P_value : formule du SE un peu barbare => probabilité 
- p^_1 - p^2_2
- CLT : courbe normale => Interval de confiance


### On peut estimer d'autres choses encore

- puissance dun test : combien de clics/vues nous faut-il pour atteindre un résultat fiable ?
- Comparer plus de 2 taux de conversion (il ne faut pas faire de tests pair-wise ?) - Multi-armed bandit