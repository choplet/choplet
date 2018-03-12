
class Node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next
        
class LinkedList:
    def __init__(self, *args):
        self.first = None
        self.last = None
        self.length = 0
        for i in args:
            self.add(i)

    def __str__(self):
        if self.first != None:
            current = self.first
            out = 'LinkedList(' +str(current.value) + ", " 
            while current.next != None:
                current = current.next 
                out += str(current.value) + ", " 
            return out + ')'
        return 'LinkedList []'

    def clear(self):
        self.__init__()
    
    def add(self, x):
        self.length+=1
        if self.first == None:
            self.last = self.first = Node(x, None)
        else:
            self.last.next = self.last = Node(x, None)
            
            
    def insert(self,i,x):
        if i > self.length:
            self.add(i)
            return
        if self.first == None:
            self.last = self.first = Node(x, None)

            return
        if i == 0:
          self.first = Node(x,self.first)

          return
        curr=self.first
        count = 0
        while curr != None:
            count+=1
            if count == i:
              curr.next = Node(x,curr.next)
              if curr.next.next == None:
                self.last = curr.next
              break
            curr = curr.next

    
    def len(self):
            length =0
            if self.first != None:
                current = self.first
                while current.next != None:
                    current = current.next
                    length += 1
            return length+1
            
    def is_empty(self):
        return self.length == 0
    
    
    def remove_at(self,i):
        if i>=self.length:
            raise IndexError
            return
        self.length -= 1
        if (self.first == None):
          return
        curr = self.first
        count = 0
        if i == 0:
          self.first = self.first.next
          return
        while curr != None:
            if count == i:
              if curr.next == None:
                self.last = curr
              old.next = curr.next 
              break
            old = curr  
            curr = curr.next
            count += 1
      
    def get(self, i):
        length = 0
        current = self.first
        while i != length:
            if not current:
                raise IndexError
            length += 1
            current = current.next
        return current.value

            
'''          
L = LinkedList(1,2,3)
#rem = L.remove_at(0)
l = L.len()
#print(rem)
print(L)
print(l)
get = L.get(0)
print(get)
'''
