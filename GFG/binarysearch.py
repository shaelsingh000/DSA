#User function template for Python

class Solution:    
    def binarysearch(self, a, n, k):
        s=0
        e=n-1
        while(s<=e):
            mid = (s+e)//2
            if a[mid]==k:
                return mid
            elif a[mid]>k:
                e=mid-1
            else:
                s = mid+1
        return -1
               

#{ 
#  Driver Code Starts
#Initial template for Python

if __name__ == '__main__':
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int, input().strip().split(' ')))
        k=int(input())
        ob = Solution()
        print (ob.binarysearch(arr, n, k))


# } Driver Code Ends