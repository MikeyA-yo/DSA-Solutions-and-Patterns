'''

Design a HashMap without using any built-in hash table libraries.

Implement the MyHashMap class:

MyHashMap() initializes the object with an empty map.
void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.
 

Example 1:

Input
["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
[[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
Output
[null, null, null, 1, -1, null, 1, null, -1]

Explanation
MyHashMap myHashMap = new MyHashMap();
myHashMap.put(1, 1); // The map is now [[1,1]]
myHashMap.put(2, 2); // The map is now [[1,1], [2,2]]
myHashMap.get(1);    // return 1, The map is now [[1,1], [2,2]]
myHashMap.get(3);    // return -1 (i.e., not found), The map is now [[1,1], [2,2]]
myHashMap.put(2, 1); // The map is now [[1,1], [2,1]] (i.e., update the existing value)
myHashMap.get(2);    // return 1, The map is now [[1,1], [2,1]]
myHashMap.remove(2); // remove the mapping for 2, The map is now [[1,1]]
myHashMap.get(2);    // return -1 (i.e., not found), The map is now [[1,1]]
'''
class MyHashMap:

    def __init__(self):
        self.hashmap = {}  # initialize an empty dictionary to store key-value pairs
        

    def put(self, key: int, value: int) -> None:
        self.hashmap[key] = value  # insert or update the value for the given key
        return self.hashmap  # returns the hashmap (not required for the problem)
        

    def get(self, key: int) -> int:
        if key in self.hashmap:  # check if the key exists in the hashmap
            return self.hashmap[key]  # return the value associated with the key
        else:
            return -1  # return -1 if key does not exist
        

    def remove(self, key: int) -> None:
        if key in self.hashmap:  # check if the key exists
            del self.hashmap[key]  # delete the key-value pair from the hashmap

'''
Walkthrough Example
Step 1: Initialize
obj = MyHashMap()
hashmap = {}
Step 2: Put values
obj.put(1, 10)
hashmap = {1: 10}
obj.put(2, 20)
hashmap = {1: 10, 2: 20}
Step 3: Get values
obj.get(1)
returns 10
obj.get(3)
returns -1 (key not found)
Step 4: Update value
obj.put(2, 50)
hashmap = {1: 10, 2: 50}
Step 5: Remove key
obj.remove(1)
hashmap = {2: 50}
Step 6: Get removed key
obj.get(1)
returns -1
Time and Space Complexity
put()    → Time: O(1), Space: O(1)
get()    → Time: O(1), Space: O(1)
remove() → Time: O(1), Space: O(1)

Overall Space Complexity: O(n)  # storing n key-value pairs
'''