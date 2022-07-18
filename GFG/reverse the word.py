
# User function Template for python3

class Solution:
    
    #Function to reverse words in a given string.
    def reverseWords(self,S):
        a=S.split(".")
        a[:]= a[::-1]
        a = ".".join(a)
        return a


#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = str(input())
        obj = Solution()
        print(obj.reverseWords(s))

# } Driver Code Ends