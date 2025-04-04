/**
 * Tâche 5: Change the text
 * 
 * Ce script met à jour le texte de l'élément header à "New Header !!!"
 * lorsque l'utilisateur clique sur l'élément avec l'id 'update_header'.
 * Il démontre la modification du contenu textuel d'un élément.
 * 
 * Utilise:
 * - textContent: Pour modifier le contenu textuel d'un élément
 */

// Ajoute un écouteur d'événements sur l'élément avec l'id 'update_header'
document.getElementById('update_header').addEventListener('click', function () {
  // Change le contenu textuel de l'élément header
  document.querySelector('header').textContent = 'New Header !!!';
});
