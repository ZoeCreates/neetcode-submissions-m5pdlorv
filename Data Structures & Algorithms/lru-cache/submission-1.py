class Node:
    def __init__(self, key=0, val =0):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):


        self.capacity = capacity
        #存的是{ key : Node对象 } hashmap，注意：Value 不是数字 10，而是存有 key=1, val=10 的整个 Node 节点

        #为什么 cache 存了 key，Node 还要存 key？
# if len(self.cache) > self.capacity:
    # 1. 找到链表最尾部（最久未使用）的 Node 节点并从链表删除
  #  removed = self._remove_tail()

    # 2. 关键点：必须同时从哈希表中把这个 key 删掉！
    #    如果没有 removed.key，你就不知道刚才删掉的 Node 对应哈希表里的哪个 key！
        self.cache = {} 

        #使用双向链表（Doubly Linked List）的核心原因是：为了能以 $O(1)$ 的时间复杂度完成“任意位置节点的删除”,如果单向的话需要花O(n)
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
            #因为它的值被更新了，相当于又被使用了一次，所以必须把它提拔到链表最前面（head 后面），刷新它的活跃度！
            self._move_to_head(node)
        else:
            node = Node(key,value)
            self.cache[key] = node
            self._add_to_head(node)

            if len(self.cache) > self.capacity:
                removed = self._remove_tail()
                #删除hashmap中的key-val pair
                del self.cache[removed.key]


    
    #把新的节点加入link list
    def _add_to_head(self,node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node


    def _remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev 

    
    #把已经存在的节点放到link list最前面
    def _move_to_head(self,node):
        self._remove_node(node) #把 node 从它原来的位置摘除，让它的前一个节点和后一个节点直接相连
        self._add_to_head(node)
    
    def _remove_tail(self):
        node= self.tail.prev 
        self._remove_node(node)
        ## 3. 返回被删掉的节点对象
    #    因为外面（put 方法）还需要拿这个 node.key 去清空哈希表里的缓存：del self.cache[node.key]
        return node




        
