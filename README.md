# Script d'Audit Système

Ce dépôt contient deux scripts Python pour effectuer des tâches d'audit système sur Windows et Linux. Ces scripts sont conçus à des fins éducatives et de recherche uniquement.

## 📜 Avertissement

**⚠️ WARNING: Educational Purpose Only ⚠️**

Ces scripts sont destinés uniquement à des fins éducatives et de recherche. Toute utilisation non autorisée ou contraire à l'éthique est strictement interdite. En utilisant ces scripts, vous acceptez de les utiliser de manière responsable et conformément aux lois en vigueur.

## 🗂 Contenu du Dépôt

- **Symlink_Windows.py** : Script pour Windows.
- **Symlink_Linux.py** : Script pour Linux.
- **README.md** : Documentation du projet.

## 🛠️ Fonctionnalités

Les deux scripts offrent les fonctionnalités suivantes :

- **Créer un lien symbolique :**
  - Crée un lien symbolique entre un fichier/dossier cible et un nouveau lien.
- **Exécuter une commande système :**
  - Exécute une commande système et affiche le résultat.
- **Lire un fichier :**
  - Affiche le contenu d'un fichier texte.
- **Lister les utilisateurs du système :**
  - Affiche la liste des utilisateurs du système.
- **Menu interactif :**
  - Un menu interactif permet de choisir et d'exécuter les différentes fonctionnalités.

## 🖥️ Script pour Windows (Symlink_Windows.py)

### Prérequis

- Python 3.x installé sur votre système Windows.
- Accès administratif pour certaines commandes système.

### Utilisation

1. Téléchargez le script **Symlink_Windows.py**.
2. Ouvrez un terminal (cmd ou PowerShell) et naviguez jusqu'au dossier contenant le script.
3. Exécutez le script avec la commande suivante :
   ```bash
   python Symlink_Windows.py
   ```
4. Suivez les instructions du menu pour sélectionner une option.

### Fonctionnalités spécifiques à Windows

- Utilisation de la commande `net user` pour lister les utilisateurs.

## 🔷 Script pour Linux (Symlink_Linux.py)

### Prérequis

- Python 3.x installé sur votre système Linux.
- Accès root ou sudo pour certaines commandes système.

### Utilisation

1. Téléchargez le script **Symlink_Linux.py**.
2. Ouvrez un terminal et naviguez jusqu'au dossier contenant le script.
3. Exécutez le script avec la commande suivante :
   ```bash
   python3 Symlink_Linux.py
   ```
4. Suivez les instructions du menu pour sélectionner une option.

### Fonctionnalités spécifiques à Linux

- Utilisation du module `pwd` pour lister les utilisateurs.

## ⚙️ Configuration

### Journalisation (Logging)

Les scripts utilisent le module `logging` pour enregistrer les actions et les erreurs. Les logs sont affichés dans le terminal avec le format suivant :

```
[YYYY-MM-DD HH:MM:SS] - LEVEL - Message
```

### Sécurité

- Les scripts évitent d'utiliser `shell=True` dans `subprocess.run` pour prévenir les injections de commandes.
- Les entrées utilisateur sont validées pour éviter des erreurs ou des comportements inattendus.

## 🚀 Exemples d'Utilisation

### Créer un lien symbolique

1. Sélectionnez l'option **1** dans le menu.
2. Entrez le chemin du fichier/dossier cible.
3. Entrez le chemin du lien symbolique à créer.

### Exécuter une commande système

1. Sélectionnez l'option **2** dans le menu.
2. Entrez la commande à exécuter (par exemple, `ls -l` sous Linux ou `dir` sous Windows).

### Lire un fichier

1. Sélectionnez l'option **3** dans le menu.
2. Entrez le chemin du fichier à lire.

### Lister les utilisateurs

1. Sélectionnez l'option **4** dans le menu.
2. La liste des utilisateurs du système sera affichée.

## 🗒 Licence

Ce projet est sous licence MIT. Pour plus de détails, consultez le fichier LICENSE.

## 🙏 Contribution

Les contributions sont les bienvenues ! Si vous souhaitez améliorer ce projet, veuillez suivre ces étapes :

1. Forkez ce dépôt.
2. Créez une nouvelle branche :
   ```bash
   git checkout -b feature/Amelioration
   ```
3. Committez vos changements :
   ```bash
   git commit -m 'Ajouter une amélioration'
   ```
4. Pushez la branche :
   ```bash
   git push origin feature/Amelioration
   ```
5. Ouvrez une **Pull Request**.

## 📧 Contact

Pour toute question ou suggestion, veuillez contacter [votre email ou nom d'utilisateur GitHub].

