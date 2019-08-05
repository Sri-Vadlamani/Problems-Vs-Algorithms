### Description:
Autocomplete with Tries

### Data structure:
 Trie data structure is a tree with each node consisting of one letter as data and pointer to the next node. It uses Finite Deterministic automation. That means, it uses state to state transition.

### Time Complexity & Space Complexity:
TrieNode:
Insert a character: Time complexity - O(1) Space complexity - O(1)
Suffixes of a node: Time complexity: O(m*h) Space complexity: O(m*h) where m is maximum number of elements in one level and h is the height.

Trie:
Inserting and searching : Time complexity: O(n) where n is the length of the word
Space complexity: O(n)
