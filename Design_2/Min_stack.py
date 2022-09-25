#Time Complexity: push() - O(1), pop() - O(1), top() - O(1), getMin() - O(1)
#Space Complexity: O(n) - We're using a stack space for 'n' numbers

class MinStack:

    def __init__(self):
        self.stack = []     #Initialization of stack
        self.minStack = []  #Initialization of minStack
        

    def push(self, val: int) -> None:
        self.stack.append(val)      #Append val into the stack
        if len(self.minStack) == 0:
            self.minStack.append(val)      #If the minStack is empty append the val into the minStack 
        else:
            if self.minStack[-1]>val:   #Check if the incoming val is less than the val in the minStack
                self.minStack.append(val)   #If yes then append that val into the minStack
            else:
                self.minStack.append(self.minStack[-1]) #Else append the last element in minStack into the minStack again

    def pop(self) -> None:
        self.stack.pop()    #Pop the last element in the stack
        self.minStack.pop() #Pop the last element in the minStack

    def top(self) -> int:
        return self.stack[-1]   #Return the last element in the stack

    def getMin(self) -> int:
        return self.minStack[-1]    #Return the last element in the minStack


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()