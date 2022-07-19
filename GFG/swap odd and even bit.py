#User function Template for python3

class Solution:
    
    ##Complete this function
    #Function to swap odd and even bits.
    def swapBits(self,n):
        #Your code here# Get all even bits of x
        return ((n&(0xAAAAAAAA))>>1)|((n&(0x5555555))<<1)
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math



def main():
    
    T=int(input())
    
    while(T>0):
        
        
        n=int(input())
        ob=Solution()
        print(ob.swapBits(n))
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends