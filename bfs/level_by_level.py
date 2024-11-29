from collections import deque

def process_by_level(start):
    """
    Performs level-order (or breadth-first) traversal of a hierarchical structure, 
    processing all elements at each level before moving to the next level.

    Parameters:
    - start: The starting node or element of the structure (e.g., root of a binary tree). 
             This element should have children or neighbors that can be iterated over 
             using the `get_children()` function.

    Returns:
    - results: A list of lists, where each inner list contains the processed results 
               of elements at the same level. Modify `process_element()` to define 
               how each element is processed.
    
    Usage:
    - This function is generic and can be used for level-order traversal of binary 
      trees, graphs, or any hierarchical structure where levels can be defined.
    """
    if not start:
        return  # Handle edge case where the starting element is None

    # Queue for BFS traversal, initialized with the starting element
    queue = deque([start])
    
    # List to store the final results (e.g., processed data from each level)
    results = []

    # Process elements level by level
    while queue:
        # Number of elements in the current level (determined by the queue size)
        level_size = len(queue)
        
        # Temporary list to store processed elements of the current level
        current_level = []

        # Process all elements at the current level
        for _ in range(level_size):
            element = queue.popleft()  # Remove the front element from the queue
            
            # Process the current element and store the result
            current_level.append(process_element(element))  # Replace with your logic
            
            # Add all next-layer elements (e.g., children or neighbors) to the queue
            for child in get_children(element):  # Adjust based on structure
                queue.append(child)

        # Add the processed results of the current level to the final results
        results.append(current_level)

    return results
