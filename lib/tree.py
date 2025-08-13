class Tree:
    def __init__(self, root=None):
        self.root = root

    def get_element_by_id(self, id):
        # Start the search from the root node
        return self._search_node(self.root, id)
    
    def _search_node(self, node, id):
        # Base case: if node is None, return None
        if node is None:
            return None
        
        # Check if current node has the matching id
        if node.get('id') == id:
            return node
        
        # Recursively search through children
        for child in node.get('children', []):
            found = self._search_node(child, id)
            if found is not None:
                return found
        
        # If not found in this subtree, return None
        return None
