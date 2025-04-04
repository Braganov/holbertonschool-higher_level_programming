/**
 * Tâche 7: Star Wars movies
 * 
 * Ce script récupère la liste des films Star Wars à partir de l'API Star Wars
 * et affiche leurs titres dans une liste (élément avec l'id 'list_movies').
 * Il démontre la récupération et l'itération sur un tableau de données 
 * provenant d'une API.
 * 
 * Utilise:
 * - fetch: Pour effectuer une requête HTTP
 * - forEach: Pour itérer sur un tableau
 * - createElement: Pour créer des éléments de liste
 */

// Effectue une requête GET vers l'API Star Wars pour obtenir la liste des films
fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(response => {
    // Vérifie si la requête a réussi
    if (!response.ok) {
      throw new Error(`Erreur HTTP: ${response.status}`);
    }
    // Convertit la réponse en JSON
    return response.json()
  })
  .then(data => {
    // Parcourt chaque film dans les résultats
    data.results.forEach(movie => {
      // Crée un élément de liste pour chaque film
      const li = document.createElement('li');
      // Définit le titre du film comme contenu de l'élément
      li.textContent = movie.title;
      // Ajoute l'élément à la liste avec l'id 'list_movies'
      document.getElementById('list_movies').appendChild(li);
    })
  })
  .catch(error => {
    // Gère les erreurs éventuelles
    console.error(`Error: ${error}`);
  });
