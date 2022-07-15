# A linked list (LL) node 
# to store a queue entry 
class Node: 
      
    def __init__(self, data): 
        self.data = data 
        self.next = None
        
class MyQueue:
    def __init__(self): 
        self.head = None
        self.tail = None
    #Function to push an element into the queue.
    def push(self, item): 
         
         #Add code here
        temp = Node(item)
        if self.head is None or self.tail is None:
            self.head=temp
            self.tail = temp
        else:
            self.tail.next=temp
            self.tail = self.tail.next
    
    #Function to pop front element from the queue.
    def pop(self):
         
         #add code here
        if self.head is None:
            return -1
        item= self.head.data
        self.head=self.head.next
        return item
#{ 
#  Driver Code Starts
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        s=MyQueue()
        q=int(input())
        q1=list(map(int,input().split()))
        i=0
        while(i<len(q1)):
            if(q1[i]==1):
                s.push(q1[i+1])
                i=i+2
            elif(q1[i]==2):
                print(s.pop(),end=" ")
                i=i+1
            elif(s.isEmpty()):
                print(-1)
                i=i+1
        print()   
# } Driver Code Ends