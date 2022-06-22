
class Solution:
    def trappingWater(self, arr,n):
        res=0
        lmax=[]
        rmax=[0]*n
        lmax.append(arr[0])
        for i in range(1,n):
            lmax.append(max(lmax[i-1],arr[i]))
        rmax[n-1]=arr[n-1]
        for j in range(n-2,-1,-1):
            rmax[j]=max(arr[j],rmax[j+1])
        for k in range(1,n,1):
            res= res+(min(lmax[k],rmax[k])-arr[k])
        return res


#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math



def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            obj = Solution()
            print(obj.trappingWater(arr,n))
            
            
            T-=1


if __name__ == "__main__":
    main()



# } Driver Code Ends