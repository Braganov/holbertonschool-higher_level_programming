# JavaScript DOM Manipulation

Ce projet contient une série de tâches liées à la manipulation du DOM (Document Object Model) en JavaScript. L'objectif est d'apprendre à interagir avec des éléments HTML en utilisant JavaScript, effectuer des opérations comme changer les couleurs, ajouter des classes, basculer des attributs et récupérer des données à partir d'API.

## Tâches

0. **Color Me (Colorer):** 
   - Changer la couleur du texte de l'en-tête en rouge (#FF0000)
   - Utilisation de `document.querySelector` pour sélectionner l'élément HTML

1. **Click and turn red (Cliquer et devenir rouge):** 
   - Changer la couleur de l'en-tête en rouge lors du clic sur un élément
   - Implémentation d'écouteurs d'événements (event listeners)

2. **Add `.red` class (Ajouter la classe `.red`):** 
   - Ajouter une classe CSS à un élément lors du clic
   - Manipulation des classes avec `classList.add`

3. **Toggle classes (Basculer entre classes):** 
   - Basculer entre les classes `red` et `green` lors du clic
   - Utilisation de `classList.contains`, `add` et `remove`

4. **List of elements (Liste d'éléments):** 
   - Ajouter des éléments à une liste lors du clic
   - Création dynamique d'éléments DOM avec `createElement`

5. **Change the text (Changer le texte):** 
   - Mettre à jour le texte de l'en-tête lors du clic
   - Manipulation du contenu textuel avec `textContent`

6. **Star Wars character (Personnage Star Wars):** 
   - Récupérer et afficher le nom d'un personnage depuis l'API Star Wars
   - Utilisation de l'API Fetch pour les requêtes HTTP

7. **Star Wars movies (Films Star Wars):** 
   - Récupérer et afficher les titres de films depuis l'API Star Wars
   - Traitement de données JSON et création dynamique d'éléments

8. **Say Hello! (Dire Bonjour!):** 
   - Afficher un message de salutation en français depuis une API
   - Chargement de script dans la section `<head>` avec `DOMContentLoaded`

## Exigences

- Tous les fichiers sont interprétés sur le navigateur Chrome (version 57.0+)
- Le code doit être conforme à la norme semistandard
- L'utilisation de `var` n'est pas autorisée
- Les manipulations du DOM, les mises à jour de valeurs et les récupérations de données doivent être effectuées sans rechargement de page

## Comment tester

Chaque tâche est accompagnée d'un fichier HTML correspondant (par exemple, `0-main.html` pour la tâche 0). Pour tester une tâche :

1. Ouvrez le fichier HTML dans votre navigateur Chrome
2. Observez le comportement selon les spécifications de la tâche
3. Utilisez les outils de développement du navigateur (F12) pour inspecter les changements dans le DOM

## Concepts utilisés

- Sélection d'éléments DOM (`querySelector`, `getElementById`)
- Gestion d'événements (`addEventListener`)
- Manipulation de classes CSS (`classList`)
- Création et modification d'éléments DOM
- Requêtes API avec Fetch
- Traitement de données JSON
- Programmation asynchrone avec Promesses
