#User function Template for python3

class Solution:
    def rotate(self, N, D):
        D = D % 16
        bin_N = bin(N)[2:]
        bin_N = '{:>016}'.format(bin_N)
        return int(bin_N[D:] + bin_N[:D], 2), int(bin_N[-D:] + bin_N[:-D], 2)

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, d = input().strip().split(" ")
        n, d = int(n), int(d)
        ob = Solution()
        ans = ob.rotate(n, d)
        print(ans[0])
        print(ans[1])
# } Driver Code Ends