class Node:
    def __init__(self, key=0, val =0):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):

        self.capacity = capacity
        self.cache = {} # key-value pair hashmap 

        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self._move_to_head(node)
        return node.val 


        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value 
            self._move_to_head(node)
        else:
            node = Node(key,value)
            self.cache[key] = node
            self._add_to_head(node)

            if len(self.cache) > self.capacity:
                removed = self._remove_tail()
                #删除hashmap中的key-val pair
                del self.cache[removed.key]


    
    def _add_to_head(self,node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node 
        self.head.next = node 
    
    def _remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev 

    def _move_to_head(self,node):
        self._remove_node(node)
        self._add_to_head(node)
    
    def _remove_tail(self):
        node= self.tail.prev 
        self._remove_node(node)
        return node




        
