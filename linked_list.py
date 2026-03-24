class Node:
    '''
    Object for storing a single node of a linked list
    Model two attributes - data and the link to the next node in the list
    '''
    data = None
    next_node = None

    def __init__(self,data):
        self.data = data
        
    def __repr__(self):
        return "<Node data : %s>" %self.data
   
class LinkedList:
    '''
    Singly linked list
    '''
    head = None

    def __init__(self):
        self.head = None
        
    def isEmpty(self):
        return self.head == None
    
    def size(self):
        '''
        Returns the number of nodes in the list. Its Runtime is linear O(n)
        '''
        current = self.head
        count = 0
        
        while current:
            count+=1
            current = current.next_node
        return count

    def add(self,data):
        '''
        add() adds a new node containing data at the head of the list.
        this operation takes constant time which is our best case scenerio.
        '''
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node
        
    def search(self,target):
        '''
        search for the first node containing data that matches the target
        it retruns the node or none if not found
        runtime is linear.
        '''
        current = self.head

        while current:
            if current.data == target:
                return current.data 
            else:
                current = current.next_node
        return None
    
    def insert(self,index,data):
        '''
        Insert a new node containing data at index position.
        Insertion take constant time but finding the node at the insertion point takes linear time.
        Therefore it takes an overall linear time
        '''
        if index == 0:
            self.add(data)
        elif index>0:
            new = Node(data)
            position = index
            current = self.head
            current.next_node

            while position>1:
                current = Node.next_node
                position -= 1
                
            prev = current
            nextt = current.next_node
            
            prev.next_node = new
            new.next_node = nextt
        
    def remove(self,key):
        '''
        removes node containing data that matches the key.
        returns the key or none if not found.
        runtime is linear
        '''
        current = self.head
        prev = None
        found = False

        while current and not found:
            if current.data == key and current is self.head:
                found = True
                self.head = current.next_node
            elif current.data == key:
                found = True
                prev.next_node = current.next_node
            else:
                prev = current
                current = current.next_node 
        return current

        
        
        
        
    def __repr__(self):
        nodes = []
        current = self.head

        while current:
            if current is self.head:
                nodes.append(f"[Head : {current.data}]")
            elif current.next_node is None:
                nodes.append(f"[Tail : {current.data}]")
            else:
                nodes.append(f"[{current.data}]")
            
            current = current.next_node
                
        return "->".join(nodes)
         
        
n1 = Node(10)
n2 = Node(20)
n1.next_node = n2

l = LinkedList()
l.head = n1
l.add(5)
l.add(57)
l.add(98)
l.size()


print(l)
l.insert(3,54)
