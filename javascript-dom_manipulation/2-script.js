/**
 * Tâche 2: Add `.red` class
 * 
 * Ce script ajoute la classe CSS 'red' à l'élément header
 * lorsque l'utilisateur clique sur l'élément avec l'id 'red_header'.
 * Cette approche est préférable à la modification directe du style
 * car elle sépare la présentation (CSS) de la logique (JavaScript).
 * 
 * Utilise:
 * - getElementById: Pour sélectionner l'élément déclencheur
 * - classList.add: Pour ajouter une classe CSS à un élément
 */

// Ajoute un écouteur d'événements sur l'élément avec l'id 'red_header'
document.getElementById('red_header').addEventListener('click', function () {
  // Lorsque l'élément est cliqué, ajoute la classe 'red' à l'élément header
  document.querySelector('header').classList.add('red');
});
