#!/bin/bash

# Chemin du fichier .gitignore source
SOURCE_GITIGNORE="/home/braga/holbertonschool-higher_level_programming/python-server_side_rendering/.gitignore"

# Vérifier que le fichier source existe
if [ ! -f "$SOURCE_GITIGNORE" ]; then
    echo "Fichier .gitignore source introuvable à $SOURCE_GITIGNORE"
    exit 1
fi

# Trouver tous les répertoires dans le projet (sauf les dossiers cachés comme .git)
find /home/braga/holbertonschool-higher_level_programming -type d -not -path "*/\.*" | while read -r dir; do
    # Ignore le répertoire qui contient déjà le .gitignore source
    if [ "$dir" == "/home/braga/holbertonschool-higher_level_programming/python-server_side_rendering" ]; then
        continue
    fi

    # Créer/écraser le fichier .gitignore dans le répertoire
    cp "$SOURCE_GITIGNORE" "$dir/.gitignore"
    echo "Créé .gitignore dans $dir"
done

echo "Opération terminée. Fichiers .gitignore ajoutés dans tous les dossiers."
