class Node:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
        
        
class LRUCache:
    def __init__(self, capacity: int):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.size = 0
        self.ketToNode = dict()
    
    
    def addToTail(self, key, val):
        node = Node(key, val)
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node
        self.ketToNode[key] = node
        self.size += 1
        
        
    def delete(self, key):
        node = self.ketToNode[key]
        del self.ketToNode[key]
        prevNode = node.prev
        nextNode = node.next
        prevNode.next = nextNode
        nextNode.prev = prevNode
        self.size -= 1
        

    def get(self, key: int) -> int:
        if key not in self.ketToNode:
            return -1
        
        value = self.ketToNode[key].val
        self.delete(key)
        self.addToTail(key, value)
        return value
            
        
    def put(self, key: int, value: int) -> None:
        if key in self.ketToNode:
            self.delete(key)
            self.addToTail(key, value)
            return
        
        if self.size == self.capacity:
            self.delete(self.head.next.key)
        
        self.addToTail(key, value)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)