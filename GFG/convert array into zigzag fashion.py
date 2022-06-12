#User function Template for python3
class Solution:

    def zigZag(self,arr, n):
        i=1
        while i<n:
            try:
                if arr[i]<arr[i-1]:
                    arr[i],arr[i-1]=arr[i-1],arr[i]
                if arr[i]<arr[i+1]:
                    arr[i],arr[i+1]=arr[i+1],arr[i]
            except:
                pass
            i=i+2
            

#{ 
#  Driver Code Starts
#Initial Template for Python 3




if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.zigZag(arr, n)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends