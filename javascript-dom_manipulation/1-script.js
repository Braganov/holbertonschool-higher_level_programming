/**
 * Tâche 1: Click and turn red
 * 
 * Ce script modifie la couleur du texte de l'élément header en rouge (#FF0000)
 * quand l'utilisateur clique sur l'élément avec l'id 'red_header'.
 * 
 * Utilise:
 * - getElementById: Pour sélectionner un élément par son identifiant
 * - addEventListener: Pour attacher un gestionnaire d'événements à un élément
 * - querySelector: Pour sélectionner l'élément header à modifier
 */

// Sélectionne l'élément avec l'id 'red_header'
document.getElementById('red_header').addEventListener('click', function () {
  // Lorsque cet élément est cliqué, sélectionne l'élément header et change sa couleur en rouge
  document.querySelector('header').style.color = '#FF0000';
});
