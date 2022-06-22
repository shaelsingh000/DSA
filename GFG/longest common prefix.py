#User function Template for python3

class Solution:

    
    def longestCommonPrefix(self, arr, n):
        m = min(arr)
        
        for i in arr:
            j=0
            s=""
            try:
                while m[j]==i[j]:
                
                    s=s+m[j]
                    j=j+1
                m = s
            except:
                pass

        if len(m)!=0:
            return m
        else:
            return -1
            

#{ 
#  Driver Code Starts
#Initial Template for Python 3
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        n = int(input())
        arr = [x for x in input().strip().split(" ")]
        
        ob=Solution()
        print(ob.longestCommonPrefix(arr, n))
# } Driver Code Ends