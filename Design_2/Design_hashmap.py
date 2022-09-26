#Time Complexity: put- O(1), get - O(1), remove - O(1)
#Approach : Linear Chaining 

class MyHashMap(object):
    class ListNode:
        def __init__(self, key, val):
            self.key = key  #Initializing a linked list as key, val and the next assigned to None
            self.val = val
            self.next = None

    def __init__(self):
        self.hashmap = [None]*100000    #Initializing the primary list to None*10^4. Since using linked list as the secindary data structure, this will prevent collisions.
    
    def hashIndex(self, key):
        return key % 100    #Calculating the hash code to store the value in the list
    
    def findNode(self, head, key):  #This method will return the prev node
        curr = head #Assigining the current to head
        prev = None #Assigning the prev to None
        
        while curr != None and curr.key != key: #Continue till curr is not equal to None and the current key is not equal to None
            prev = curr #Assigning prev to curr
            curr = curr.next    #Assigning curr to prev.next
        
        return prev #Return the prev

    def put(self, key: int, value: int) -> None:    #Add element to the hashmap
        hash_index = self.hashIndex(key)    #Getting the hashindex to store the element
        
        if self.hashmap[hash_index] == None:    #If the has index is equal to none then push a dummy node at that index 
            self.hashmap[hash_index] = self.ListNode(-1, -1) #We're setting up a dummy node to maintain the modularity
            
        prev = self.findNode(self.hashmap[hash_index], key) #Assigning the prev with its index and with its key
            
        if prev.next == None:   #If next to prev is equal to None then put the value next to prev
            prev.next = self.ListNode(key, value)
        else:
            prev.next.val = value   #Updating the existing value to the linked list

    def get(self, key: int) -> int: #Get the value from the hashmap
        hash_index = self.hashIndex(key)    #Hashindex 
        
        if self.hashmap[hash_index] == None:    #If there is no element in the hashindex then return -1
            return -1
        prev = self.findNode(self.hashmap[hash_index], key) #Assigning the prev with its index and with its key
        if prev.next == None:   #If the next node is None then return -1
            return -1
        else:   #Else return the value in that index
            return prev.next.val
        

    def remove(self, key: int) -> None: #Remove the value from the hashmap
        hash_index = self.hashIndex(key)    #Hashindex
        
        if self.hashmap[hash_index] == None:    #If there is no element the return nothing
            return
        prev = self.findNode(self.hashmap[hash_index], key) #Assigning the prev with its index and with its key in the linked list
        
        if prev.next == None:   #If the next node is None the return nothing
            return None
        else:
            prev.next = prev.next.next  #Else assign prev.next to prev.next.next, by doing this the given element is not deleted exactly but it's not accessable
            


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
