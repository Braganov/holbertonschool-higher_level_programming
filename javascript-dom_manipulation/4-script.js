/**
 * Tâche 4: List of elements
 * 
 * Ce script ajoute un nouvel élément <li> avec le texte "Item" à la liste
 * lorsque l'utilisateur clique sur l'élément avec l'id 'add_item'.
 * Il démontre la création dynamique d'éléments DOM et leur insertion.
 * 
 * Utilise:
 * - createElement: Pour créer un nouvel élément DOM
 * - textContent: Pour définir le contenu textuel d'un élément
 * - appendChild: Pour ajouter un nœud enfant à un élément parent
 */

// Ajoute un écouteur d'événements sur l'élément avec l'id 'add_item'
document.getElementById('add_item').addEventListener('click', function () {
  // Crée un nouvel élément <li>
  const li = document.createElement('li');
  
  // Définit le texte de l'élément
  li.textContent = 'Item';
  
  // Ajoute l'élément à la liste (élément <ul> avec la classe 'my_list')
  document.querySelector('ul.my_list').appendChild(li);
});
