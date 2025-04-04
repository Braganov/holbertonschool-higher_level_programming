/**
 * Tâche 6: Star Wars character
 * 
 * Ce script récupère les informations d'un personnage Star Wars (Leia Organa)
 * à partir de l'API Star Wars et affiche son nom dans l'élément avec l'id 'character'.
 * Il démontre l'utilisation de l'API Fetch pour effectuer des requêtes HTTP asynchrones.
 * 
 * Utilise:
 * - fetch: Pour effectuer une requête HTTP
 * - Promises (.then/.catch): Pour gérer les opérations asynchrones
 * - json(): Pour convertir la réponse en objet JavaScript
 */

// Effectue une requête GET vers l'API Star Wars pour obtenir les informations du personnage #5
fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then(response => {
    // Vérifie si la requête a réussi
    if (!response.ok) {
      throw new Error(`Erreur HTTP: ${response.status}`);
    }
    // Convertit la réponse en JSON
    return response.json()
  })
  .then(data => {
    // Extrait le nom du personnage et l'affiche dans l'élément avec l'id 'character'
    document.getElementById('character').textContent = data.name;
  })
  .catch(error => {
    // Gère les erreurs éventuelles
    console.error(`Error: ${error}`);
  });
