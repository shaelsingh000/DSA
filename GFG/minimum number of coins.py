#User function Template for python3

class Solution:
    def minPartition(self, n):
        # code here
        coins = [2000,500,200,100,50,20,10,5,2,1]
        ans=[]
        i=0
        while n and i<10:
            if n>=coins[i]:
                ans.append(coins[i])
                n=n-coins[i]
            else:
                i+=1
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        
        ob = Solution()
        arr = ob.minPartition(N)
        for i in range(len(arr)):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends