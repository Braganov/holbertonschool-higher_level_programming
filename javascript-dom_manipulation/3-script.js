/**
 * Tâche 3: Toggle classes
 * 
 * Ce script bascule la classe de l'élément header entre 'red' et 'green'
 * lorsque l'utilisateur clique sur l'élément avec l'id 'toggle_header'.
 * Il utilise la méthode classList.toggle qui ajoute la classe si elle n'est pas
 * présente et la supprime si elle est déjà présente.
 * 
 * Utilise:
 * - getElementById: Pour sélectionner l'élément déclencheur
 * - classList.toggle: Pour basculer une classe CSS
 */

// Ajoute un écouteur d'événements sur l'élément avec l'id 'toggle_header'
document.getElementById('toggle_header').addEventListener('click', function () {
  // Bascule entre les classes 'red' et 'green' sur l'élément header
  document.querySelector('header').classList.toggle('red');
  document.querySelector('header').classList.toggle('green');
});
