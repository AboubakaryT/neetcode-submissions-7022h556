class Node:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} #map key to node
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left

    def insert(self, Node):
        pre, nxt = self.right.prev, self.right
        Node.next = nxt
        Node.prev = pre
        pre.next = Node
        nxt.prev = Node
        return

    def remove(self,Node):
        prev, next = Node.prev, Node.next
        prev.next = next
        next.prev = prev


    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key]) #remove at current position
            self.insert(self.cache[key]) #insert at end
            return self.cache[key].val 
        return -1

    def put(self, key: int, value: int) -> None:
            if key in self.cache:
                self.remove(self.cache[key]) #remove at current position
                self.insert(self.cache[key]) #insert at end
                self.cache[key].val = value #update the value
            else:
                nodeToInsert = Node(key,value)
                self.cache[nodeToInsert.key] = nodeToInsert
                self.insert(nodeToInsert)
                if len(self.cache) > self.capacity:
                    lru = self.left.next #Refrence
                    self.remove(lru)#Remove at current positons
                    del self.cache[lru.key] #delete the key after
