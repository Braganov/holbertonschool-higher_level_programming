/**
 * Tâche 8: Say Hello!
 * 
 * Ce script récupère un message de salutation en français depuis une API
 * et l'affiche dans l'élément avec l'id 'hello'.
 * 
 * Point particulier: Ce script est chargé dans la section <head> du document HTML,
 * et il faudrait normalement utiliser l'événement DOMContentLoaded pour s'assurer
 * que le DOM est complètement chargé avant d'accéder à ses éléments.
 * 
 * Utilise:
 * - fetch: Pour effectuer une requête HTTP
 * - Promises (.then/.catch): Pour gérer les opérations asynchrones
 */

// L'événement DOMContentLoaded devrait être utilisé ici pour s'assurer que le DOM est chargé
document.addEventListener('DOMContentLoaded', function() {
  // Effectue une requête GET vers l'API pour obtenir une salutation en français
  fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
    .then(response => {
      // Vérifie si la requête a réussi
      if (!response.ok) {
        throw new Error(`Erreur HTTP: ${response.status}`);
      }
      // Convertit la réponse en JSON
      return response.json();
    })
    .then(data => {
      // Affiche le message de salutation dans l'élément avec l'id 'hello'
      document.getElementById('hello').textContent = data.hello;
    })
    .catch(error => {
      // Gère les erreurs éventuelles
      console.error(`Error: ${error}`);
    });
});
