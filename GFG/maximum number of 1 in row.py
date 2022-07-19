#User function Template for python3

class Solution:
    def maxOnes (self, a, N, M):
        m=0
        i,j=0,0
        res=0
        
        while i<N:
            c=0
            for b in a[i]:
                if b == 1:
                    c=c+1
            if c>m:
                m=c
                res=i
            i=i+1
        return res
            


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        size = input().strip().split()
        r = int(size[0])
		c = int(size[1])
		line = list(map(int,input().split()))
		matrix = [ [0 for _ in range(c)] for _ in range(r) ]
        for i in range(r):
			for j in range(c):
				matrix[i][j] = line[i*c+j]
        ob = Solution()
        print(ob.maxOnes(matrix,r,c))

# } Driver Code Ends