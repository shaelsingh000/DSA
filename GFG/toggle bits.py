#User function Template for python3

class Solution:
    def toggleBits(self, N , L , R):
        c=R-L+1;
        mask=pow(2 , c)-1;
        mask=(mask<<(L-1));
        return (N ^ mask);

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N,L,R=map(int,input().split())
        
        ob = Solution()
        print(ob.toggleBits(N,L,R))
# } Driver Code Ends