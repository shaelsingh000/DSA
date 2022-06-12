#User function Template for python3

class Solution:
    def minValue(self, a, b, n):
        a.sort()
        b.sort()
        b.reverse()
        s = 0
        for i in range(0,n):
            s = s+a[i]*b[i]
        return s        


#{ 
#  Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        b = [int(x) for x in input().strip().split()]
        ob=Solution()
        print(ob.minValue(a, b, n))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends