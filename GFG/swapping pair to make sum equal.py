class Solution:
    def findSwapValues(self,a, n, b, m):
        x=sum(a)
        y=sum(b)
        c=0
        if x==y:
            return 0
        d={}
        for i in b:
            if i not in d:
                d[i]=1
            else:
                d[i]=d[i]+1
        d=abs(x-y)//2
        for i in a:
            if i+d:
                return 1
        
        return -1



#{ 
#  Driver Code Starts
if __name__ == '__main__': 
    
    
    t=int(input())
    for _ in range(0,t):
        l=list(map(int,input().split()))
        n=l[0]
        m=l[1]
        a = list(map(int,input().split()))
        b = list(map(int, input().split()))
        ob = Solution()
        print(ob.findSwapValues(a,n,b,m))
# } Driver Code Ends