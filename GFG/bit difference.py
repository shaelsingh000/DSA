#User function Template for python3

class Solution:
    def countBitsFlip(self,a,b):
        x= a^b
        c=0
        if x==0:
            return 0
        while(x):
            x=x&(x-1)
            c=c+1
        return c

#{ 
#  Driver Code Starts
#Initial Template for Python 3


import math



def main():
    
    T=int(input())
    
    while(T>0):
        
        
        ab=[int(x) for x in input().strip().split()]
        a=ab[0]
        b=ab[1]
        ob=Solution()
        print(ob.countBitsFlip(a,b))
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends