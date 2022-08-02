
class Solution:
    def countDistinct(self, a, n, k):
        d = {}
        s = 0
        ans = []
        for i in range(k):
            d[a[i]] = d.get(a[i],0)+1
        for i in range(k,n):
            ans.append(len(d))
            d[a[i]] = d.get(a[i],0)+1
            d[a[s]]-=1
            if d[a[s]]==0:
                d.pop(a[s])
            s+=1
        ans.append(len(d))
        return ans
            
            


#{ 
 # Driver Code Starts
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n,k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        res = Solution().countDistinct(arr, n, k)
        for i in res:
            print (i, end = " ")
        print ()
# } Driver Code Ends