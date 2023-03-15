// Define a function to expand the category tree recursively
function expandCategoryTree(categoryListNode) {
  // Find the child nodes of the category list node
  var categoryNodes = $(categoryListNode).find('> ul > li > a');
  
  // Loop through the child nodes and expand them
  categoryNodes.each(function() {
    // Check if the category node has a "Category:" prefix
    if ($(this).attr('title').startsWith('Category:')) {
      // Click on the category node to expand it
      $(this).click();
      
      // Find the child category list node and recursively expand it
      var childCategoryListNode = $(this).parent().find('> ul');
      expandCategoryTree(childCategoryListNode);
    }
  });
}

// Find the category tree root node and expand it
var categoryTreeRootNode = $('#mw-subcategories');
expandCategoryTree(categoryTreeRootNode);