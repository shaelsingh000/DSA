#User function Template for python3

class Solution:

    def longestSubstrDistinctChars(self, s):
        max = 0
        for i in range(len(S)): 
            substring = "" 
            for e in S[i:] : 
                if e not in substring: 
                    substring += e 
                else : 
                    break 
               
            length_of_substring = len(substring) 
           
            if length_of_substring > max : 
                max = length_of_substring
        return max


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        S = input()

        solObj = Solution()

        ans = solObj.longestSubstrDistinctChars(S)

        print(ans)

# } Driver Code Ends