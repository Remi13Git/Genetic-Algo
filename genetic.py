import random
import matplotlib.pyplot as plt

class Individu:
    def __init__(self):
        self.force = random.randint(0, 1)
        self.vitesse = random.randint(0, 1)
        self.defense = random.randint(0, 1)
        self.vie = random.randint(0, 1)
        self.endurance = random.randint(0, 1)
        self.score = self.calculer_score()

    def calculer_score(self):
        return self.force + self.vitesse + self.defense + self.vie + self.endurance

class Population:
    def __init__(self, taille):
        self.taille = taille
        self.individus = [Individu() for _ in range(taille)]
        self.trier_population()

    def trier_population(self):
        self.individus = sorted(self.individus, key=lambda x: x.score, reverse=True)

    def selectionner_parents(self, pourcentage):
        taille_selection = int(pourcentage * self.taille)
        return self.individus[:taille_selection]
    
    def crossover(self, parents):
        enfants = []
        for _ in range(self.taille - len(parents)):
            parent1, parent2 = random.sample(parents, 2)  # Sélection aléatoire de deux parents
            enfant = Individu()
            # Crossover : mélanger les caractéristiques des parents pour créer un nouvel individu
            enfant.force = parent1.force if random.random() < 0.5 else parent2.force
            print(enfant.force)
            enfant.vitesse = parent1.vitesse if random.random() < 0.5 else parent2.vitesse
            print(enfant.vitesse)
            enfant.defense = parent1.defense if random.random() < 0.5 else parent2.defense
            print(enfant.defense)
            enfant.vie = parent1.vie if random.random() < 0.5 else parent2.vie
            print(enfant.vie)
            enfant.endurance = parent1.endurance if random.random() < 0.5 else parent2.endurance
            print(enfant.endurance)
            enfant.score = enfant.force + enfant.vitesse + enfant.defense + enfant.vie + enfant.endurance
            print('Pré-mutation : ' + str(enfant.score))
            # Mutation : petite chance de mutation pour chaque caractéristique
            if random.random() < 0.2: 
                enfant.force = max(1, min(enfant.force + random.randint(-1, 1), 10))
            if random.random() < 0.2:
                enfant.vitesse = max(1, min(enfant.vitesse + random.randint(-1, 1), 10))
            if random.random() < 0.2:
                enfant.defense = max(1, min(enfant.defense + random.randint(-1, 1), 10))
            if random.random() < 0.2:
                enfant.vie = max(1, min(enfant.vie + random.randint(-1, 1), 10))
            if random.random() < 0.2:
                enfant.endurance = max(1, min(enfant.endurance + random.randint(-1, 1), 10))
            enfant.score = enfant.force + enfant.vitesse + enfant.defense + enfant.vie + enfant.endurance
            print('Post-mutation : ' + str(enfant.score))
            enfants.append(enfant)
        return enfants
    
    def creer_nouvelle_generation(self, pourcentage_selection=0.1):
        parents = self.selectionner_parents(pourcentage_selection)
        enfants = self.crossover(parents)
        self.individus = parents + enfants
        self.trier_population()
    


# Création de la population initiale
population = Population(taille=20)

# Nombre de générations à effectuer
nombre_de_generations = 40

# Initialisation d'une liste pour stocker les scores du meilleur individu à chaque génération
scores_meilleur_individu = []

# Boucle pour effectuer le processus sur chaque génération
for generation in range(nombre_de_generations):
    # Création d'une nouvelle génération
    population.creer_nouvelle_generation(pourcentage_selection=0.1)

    # Ajout du score du meilleur individu à la liste
    scores_meilleur_individu.append(population.individus[0].score)

    # Affichage des caractéristiques du meilleur individu de la génération actuelle
    meilleur_individu = population.individus[0]
    print(f"Génération {generation+1} - Meilleur individu :")
    print("Force:", meilleur_individu.force)
    print("Vitesse:", meilleur_individu.vitesse)
    print("Défense:", meilleur_individu.defense)
    print("Vie:", meilleur_individu.vie)
    print("endurance:", meilleur_individu.endurance)
    print("Score:", meilleur_individu.score)


    # Sélection des meilleurs individus pour la reproduction
    parents = population.selectionner_parents(pourcentage=0.1)
    

    # Crossover pour créer de nouveaux individus
    nouveaux_individus = population.crossover(parents)
    

    # Affichage des caractéristiques du premier nouvel individu
    premier_nouvel_individu = nouveaux_individus[0]
    print("\nPremier nouvel individu créé par crossover :")
    print("Force:", premier_nouvel_individu.force)
    print("Vitesse:", premier_nouvel_individu.vitesse)
    print("Défense:", premier_nouvel_individu.defense)
    print("Vie:", premier_nouvel_individu.vie)
    print("endurance:", premier_nouvel_individu.endurance)
    print("Score:", premier_nouvel_individu.score)

# Tracer le graphique
plt.plot(range(1, nombre_de_generations + 1), scores_meilleur_individu, marker='o')
plt.title("Évolution du score du meilleur individu")
plt.xlabel("Génération")
plt.ylabel("Score")
plt.grid(True)
plt.show()