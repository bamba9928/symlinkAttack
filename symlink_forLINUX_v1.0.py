import os
import subprocess
import pwd
import logging
import sys

def display_warning():
    """Affiche un avertissement concernant l'utilisation du script."""
    message = """
    ***************************************
     Bamba Dieng +221 77 249 05 30  <>  <>    bigrip2016@gmail.com  <> <>  Baol ma terre natale
    🌍 Basé au Sénégal
    🚀 Projets : Gestion d'applications web avec Django, développement d'IA légère pour le code
    ⚙️ Langages : Python, JavaScript, SQL, HTML, Bootstrap, CSS etc..
    🔍 Objectif : meilleur en programmation et en sécurité informatique
    💼 Toujours prêt à relever de nouveaux défis techniques   
    
    ⚠️ WARNING: Educational Purpose Only ⚠️

    This script is intended solely for educational and research purposes.  
    Any unauthorized or unethical use of this code is strictly prohibited.

    By proceeding, you agree to use it responsibly and in accordance with legal guidelines.
    ***************************************
    """
    print(message)

display_warning()

# Configuration du logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def create_symlink(target, link_name):
    """Créer un lien symbolique."""
    try:
        if not os.path.exists(target):
            logging.error(f"La cible {target} n'existe pas.")
            return
        if os.path.exists(link_name):
            logging.warning(f"Le lien symbolique {link_name} existe déjà.")
            return
        os.symlink(target, link_name)
        logging.info(f"Symlink créé : {link_name} -> {target}")
    except PermissionError:
        logging.error(f"Permission refusée pour créer le lien symbolique {link_name}.")
    except Exception as e:
        logging.error(f"Erreur lors de la création du symlink : {e}")

def run_command(command):
    """Exécuter une commande système."""
    try:
        # shell=True si vous voulez
        result = subprocess.run(command, shell=False, text=True, capture_output=True)
        if result.returncode == 0:
            logging.info("Résultat :\n" + result.stdout)
        else:
            logging.error("Erreur :\n" + result.stderr)
    except FileNotFoundError:
        logging.error(f"Commande non trouvée : {command}")
    except Exception as e:
        logging.error(f"Erreur lors de l'exécution de la commande : {e}")

def read_file(file_path):
    """Lire le contenu d'un fichier."""
    try:
        if not os.path.exists(file_path):
            logging.error(f"Le fichier {file_path} n'existe pas.")
            return
        with open(file_path, 'r') as file:
            content = file.read()
            logging.info(f"Contenu du fichier {file_path} :\n{content}")
    except PermissionError:
        logging.error(f"Permission refusée pour lire le fichier {file_path}.")
    except Exception as e:
        logging.error(f"Erreur lors de la lecture du fichier : {e}")

def list_users():
    """Lister les utilisateurs du système."""
    try:
        for user in pwd.getpwall():
            logging.info(f"Nom d'utilisateur : {user.pw_name}, UID : {user.pw_uid}, Home : {user.pw_dir}")
    except Exception as e:
        logging.error(f"Erreur lors de la récupération des utilisateurs : {e}")

def main():
    """Menu principal."""
    while True:
        print("\n=== Script d'Audit ===")
        print("1. Créer un lien symbolique")
        print("2. Exécuter une commande système")
        print("3. Lire un fichier")
        print("4. Lister les utilisateurs")
        print("5. Quitter")

        choice = input("Choisissez une option : ")

        if choice == '1':
            target = input("Chemin du fichier ou dossier cible : ")
            link_name = input("Chemin du lien symbolique à créer : ")
            create_symlink(target, link_name)

        elif choice == '2':
            command = input("Entrez la commande à exécuter : ").split()
            run_command(command)

        elif choice == '3':
            file_path = input("Chemin du fichier à lire : ")
            read_file(file_path)

        elif choice == '4':
            list_users()

        elif choice == '5':
            print("Au revoir !")
            break

        else:
            print("Option invalide. Réessayez.")

if __name__ == "__main__":
    main()
