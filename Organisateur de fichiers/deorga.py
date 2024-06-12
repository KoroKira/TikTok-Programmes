import os  # Pour interagir avec le système d'exploitation
import shutil  # Pour les opérations de fichiers de haut niveau
import json  # Pour travailler avec des données JSON

# Définir le chemin pour le fichier journal
log_file = os.path.join(os.path.expanduser('~'), 'file_organizer_log.json')

# Fonction pour supprimer les dossiers vides
def remove_empty_directories(path):
    for root, dirs, files in os.walk(path, topdown=False):
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            try:
                os.rmdir(dir_path)
            except OSError:
                pass

# Vérifier si le fichier journal existe
if not os.path.exists(log_file):  # Vérifier si le fichier journal n'existe pas
    print("Aucun fichier journal trouvé. Impossible de revenir en arrière.")
else:
    # Lire les mouvements depuis le fichier journal
    with open(log_file, 'r') as f:  # Ouvrir le fichier journal en mode lecture
        movements = json.load(f)  # Charger les mouvements depuis le fichier journal

    # Restaurer les fichiers à leur emplacement d'origine
    for movement in movements:  # Parcourir les mouvements dans la liste
        source = movement['source']  # Obtenir le chemin source du mouvement
        destination = movement['destination']  # Obtenir le chemin de destination du mouvement
        if os.path.exists(destination):  # Vérifier si le fichier existe à la destination
            shutil.move(destination, source)  # Déplacer le fichier vers l'emplacement d'origine

    # Supprimer les dossiers créés
    desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
    downloads_path = os.path.join(os.path.expanduser('~'), 'Downloads')

    remove_empty_directories(desktop_path)
    remove_empty_directories(downloads_path)

    # Supprimer le fichier journal après la restauration
    os.remove(log_file)  # Supprimer le fichier journal

    print("Restauration terminée.")
