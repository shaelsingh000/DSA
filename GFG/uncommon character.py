#User function Template for python3

class Solution:
    def UncommonChars(self,A, B):
        s=""
        for i in A:
            if i not in B:
                s=s+i
        for i in B:
            if i not in A:
                s=s+i
        s=list(set(s))
        s=''.join(sorted(s))
        if len(s)!=0:
            return s
        return -1
        
        
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())

    for tcs in range(T):
        A = input()
        B = input()
        ob = Solution()
        print(ob.UncommonChars(A, B))

# } Driver Code Ends