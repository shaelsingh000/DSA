#User function Template for python3

class Solution:
    def rotateMatrix(self, M, N, Mat):
        left = 0
        right = N-1
        top = 0
        bottom = M-1
       
        while(left<right and top<bottom):
            prev = Mat[top+1][left]
           
            for i in range(left,right+1):
                (Mat[top][i],prev) = (prev,Mat[top][i])
               
            top+=1
               
            for i in range(top,bottom+1):
                (Mat[i][right],prev) = (prev,Mat[i][right])
               
            right-=1
           
            for i in range(right,left-1,-1):
                (Mat[bottom][i],prev) = (prev,Mat[bottom][i])
               
            bottom-=1
           
            for i in range(bottom,top-1,-1):
                (Mat[i][left],prev) = (prev,Mat[i][left])
               
            left+=1
           
        return Mat


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N,M=map(int,input().strip().split(" "))
        A=[]
        for i in range(N):
            B=list(map(int,input().strip().split(" ")))
            A.append(B)
        ob=Solution()
        ans=ob.rotateMatrix(N,M,A)
        for i in range(N):
            for j in range(M):
                print(ans[i][j],end=" ")
            print()    
# } Driver Code Ends