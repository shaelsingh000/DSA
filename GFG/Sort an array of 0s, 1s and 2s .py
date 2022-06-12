#User function Template for python3

class Solution:
    def sort012(self,arr,n):
        i=0
        while i<n:
            if arr[i]==0:
                i+=1
            if arr[i]==2:
                i+=1
            if a
            
            
        


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        ob=Solution()
        ob.sort012(arr,n)
        for i in arr:
            print(i, end=' ')
        print()

# } Driver Code Ends