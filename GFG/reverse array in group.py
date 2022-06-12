#User function template for Python

class Solution:    
    #Function to reverse every sub-array group of size k.
    def reverseInGroups(self, arr, N, K):
        i=0
        ans=[]
        while i<N:
            j=i+K-1
            if j>=N: j=N-1
            while j>=i:
                ans.append(arr[j])
                j-=1
            i=i+K
        i=0
        while i<len(arr):
            arr[i]=ans[i]
            i+=1
        
#{ 
#  Driver Code Starts
#Initial template for Python

import math
def main():
    T=int(input())
    while(T>0):
        nk=[int(x) for x in input().strip().split()]
        N=nk[0]
        K=nk[1]
        arr=[int(x) for x in input().strip().split()]
        
        ob = Solution()
        ob.reverseInGroups(arr,N,K)
        for i in arr:
            print(i,end=" ")
        print()
        T-=1

if __name__=="__main__":
    main()




# } Driver Code Ends