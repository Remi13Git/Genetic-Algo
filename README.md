# Genetic Algo

Ce projet implémente un algorithme génétique simple en Python pour résoudre un problème d'optimisation. Il utilise des concepts tels que la sélection naturelle, la mutation et la reproduction pour trouver une solution optimale au fil des générations.

## Prérequis

- Python 3.11 doit être installé sur votre machine.

## Installation

1. Clonez ce dépôt sur votre machine locale :

   ```bash
   git clone https://github.com/Remi13Git/Genetic-Algo


## Paramètres

Vous pouvez obtenir des résultats différents en modifiant certaines variables directement dans le code :

- `population` : Taille de la population d'individus (solutions potentielles) dans chaque génération.
- `nombre_de_generations` : Nombre total de générations que l'algorithme va parcourir.
- `pourcentage_selection` : Pourcentage d'individus sélectionnés dans chaque génération pour la reproduction.
- `random.randint(-1, 1)` : Amplitude des mutations aléatoires appliquées aux individus pendant le processus de mutation.

### Exemple de modifications dans le code :

- Augmenter la taille de la population pour obtenir une plus grande diversité de solutions :
  ```python
  population = Population(taille=100)

## Lancer l'Application

Pour démarrer l'application, utilisez la commande suivante :

```bash
python3.11 genetic.py