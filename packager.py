import os

def generate_cmake_package(folder_path):
    """
    Génère un fichier CMakeLists.txt dans le dossier sélectionné.
    Ce fichier servira à compiler un projet C++ ou Python plus tard.
    """
    try:
        # Créer un sous-dossier build si nécessaire
        build_dir = os.path.join(folder_path, "build")
        os.makedirs(build_dir, exist_ok=True)

        cmake_content = f"""# Auto-généré par la Boîte Magique de Severus Rogue
cmake_minimum_required(VERSION 3.10)
project(MagicBox)

set(CMAKE_CXX_STANDARD 17)

# Exemple de structure
add_executable(MagicBox main.cpp)
"""

        cmake_file = os.path.join(folder_path, "CMakeLists.txt")
        with open(cmake_file, "w", encoding="utf-8") as f:
            f.write(cmake_content)

        return f"✅ Fichier CMakeLists.txt créé avec succès dans {folder_path}"

    except Exception as e:
        return f"❌ Erreur lors de la génération du package : {e}"
