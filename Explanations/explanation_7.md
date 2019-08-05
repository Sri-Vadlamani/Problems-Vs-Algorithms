### Description:
HTTP Router using a Trie.

### Data structure:
 Trie data structure is a tree with each node consisting of one letter as data and pointer to the next node. It uses Finite Deterministic automation. That means, it uses state to state transition.

### Time Complexity & Space Complexity:
RouteTrieNode:
Insert a path: Time complexity - O(1)
RouteTrie:
Inserting and searching : Time complexity: O(n) where n is the length of the word

### Space Complexity:
The space complexity O(n) (lookup, add handler)
