import os
import subprocess

def upload_to_github(project_path, repo_url):
    """
    Initialise un dépôt git local, ajoute les fichiers, 
    et pousse vers le dépôt GitHub fourni.
    """
    try:
        # Aller dans le dossier du projet
        os.chdir(project_path)

        # Initialisation Git
        if not os.path.exists(os.path.join(project_path, ".git")):
            subprocess.run(["git", "init"], check=True)

        # Ajout de tous les fichiers
        subprocess.run(["git", "add", "."], check=True)

        # Commit
        subprocess.run(["git", "commit", "-m", "Ajout automatique du projet Severus Rogue"], check=False)

        # Ajout du remote si non existant
        remotes = subprocess.run(["git", "remote"], capture_output=True, text=True)
        if "origin" not in remotes.stdout:
            subprocess.run(["git", "remote", "add", "origin", repo_url], check=True)

        # Création de la branche main
        subprocess.run(["git", "branch", "-M", "main"], check=True)

        # Push
        subprocess.run(["git", "push", "-u", "origin", "main"], check=True)

        return f"✅ Projet envoyé sur GitHub avec succès : {repo_url}"

    except subprocess.CalledProcessError as e:
        return f"❌ Erreur Git : {e}"
    except Exception as e:
        return f"❌ Erreur inattendue : {e}"
