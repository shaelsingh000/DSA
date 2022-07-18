#User function Template for python3

class Solution:
    def romanToDecimal(self, S):
        total=0
        d={
            "I": 1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        num=0
        i=0
        while i<len(S):
            if i==len(S)-1 or d[S[i]]>=d[S[i+1]]:
                num = d[S[i]]
                i=i+1
            else:
                num = d[S[i+1]]-d[S[i]]
                i=i+2
            total= total+num
        return total
                

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for _ in range(t):
        ob = Solution()
        S = input()
        print(ob.romanToDecimal(S))
# } Driver Code Ends