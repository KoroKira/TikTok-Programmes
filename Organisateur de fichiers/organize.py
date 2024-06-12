import os  # Pour interagir avec le système d'exploitation
import shutil  # Pour les opérations de fichiers de haut niveau
import json  # Pour travailler avec des données JSON
import datetime  # Pour travailler avec des dates et des heures

# Définir les chemins pour le bureau et les téléchargements. 
# En suivant ce pattern on a les autres répertoires si besoin
desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
downloads_path = os.path.join(os.path.expanduser('~'), 'Downloads')

# Définir le chemin pour le fichier journal
log_file = os.path.join(os.path.expanduser('~'), 'file_organizer_log.json')

# Initialiser une liste pour les mouvements de fichiers pour logs
movements = []

# Fonction pour organiser les fichiers en fonction de leur extension
def organize_files(path):  # Prend le chemin du répertoire à organiser
    for item in os.listdir(path): # Parcourir les éléments dans le répertoire
        item_path = os.path.join(path, item) # Chemin complet de l'élément
        if os.path.isfile(item_path): # Vérifier si l'élément est un fichier
            file_extension = item.split('.')[-1] # Obtenir l'extension du fichier
            directory = os.path.join(path, file_extension.upper() + ' Files') 
            if not os.path.exists(directory): # Vérifier si le répertoire existe
                os.makedirs(directory) # Créer le répertoire s'il n'existe pas
            new_path = os.path.join(directory, item) # Nouveau chemin pour le fichier
            shutil.move(item_path, new_path) # Déplacer le fichier vers le nouveau chemin
            movements.append({'source': item_path, 'destination': new_path})

# Organiser les fichiers sur le bureau, donc on appelle les fonctions
organize_files(desktop_path)

# Organiser les fichiers dans les téléchargements aussi
organize_files(downloads_path)

# Enregistrer les mouvements dans le fichier journal comme ça on peut back up si besoin
with open(log_file, 'w') as f:
    json.dump(movements, f)

print("Organisation terminée.") 
